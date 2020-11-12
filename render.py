#!/usr/bin/env python3

import os
import sys
import csv
import json

from collections import Counter, OrderedDict

from bin.convert_geojson import wkt_to_json_geometry
from bin.jinja_setup import setup_jinja
from bin.create_id import create_conservation_area_identifier

# handle large field sizes
csv.field_size_limit(sys.maxsize)

docs = "docs"
dataset_csv = "data/dataset.csv"
# dataset_csv = "data/small.csv"


def render(path, template, **kwargs):
    path = os.path.join(docs, path)
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(path, "w") as f:
        print(f"creating {path}")
        f.write(template.render(**kwargs))


env = setup_jinja()
env.globals["urlRoot"] = "/conservation-area-geography/"
index_template = env.get_template("index.html")
area_template = env.get_template("area.html")


def create_geometry_file(area):
    area_dir = f"docs/{area['id']}"
    if not os.path.exists(area_dir):
        os.mkdir(area_dir)
    try:
        geojson = wkt_to_json_geometry(area["geometry"])
        with open(f"{area_dir}/geometry.geojson", "w") as f:
            json.dump(geojson, f)
    except Exception as e:
        print(e)


def by_organisation(areas):
    by_organisation = {}
    for area in areas:
        by_organisation.setdefault(area["organisation"], [])
        by_organisation[area["organisation"]].append(area)
    return OrderedDict(sorted(by_organisation.items()))


def generate_pages():
    conservation_areas = []
    for idx, o in enumerate(csv.DictReader(open(dataset_csv)), start=1):
        # temporary ids using row number and resource
        o["id"] = f"{idx}:{o['resource']}"
        # attempt to create a more readable id
        o["id"] = f"{create_conservation_area_identifier(o)}:{idx}"
        create_geometry_file(o)
        del o["geometry"]  # don't need to send to template
        conservation_areas.append(o)
        render(f"{o['id']}/index.html", area_template, con_area=o)

    # id_counts = Counter([x["id"] for x in conservation_areas])
    # print(sorted(id_counts.items(), key=lambda x: x[1]))
    cas = {
        "count": len(conservation_areas),
        "organisation": by_organisation(conservation_areas),
    }
    render(
        "index.html",
        index_template,
        conservation_areas=cas,
    )


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--local":
        # env.globals["staticPath"] = "/static"
        env.globals["urlRoot"] = "/"

    generate_pages()