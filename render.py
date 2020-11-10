#!/usr/bin/env python3

import os
import sys
import csv
import json

from bin.convert_geojson import wkt_to_json_geometry
from bin.jinja_setup import setup_jinja

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
index_template = env.get_template("index.html")
area_template = env.get_template("area.html")


def create_geometry_file(area, idx):
    area_dir = f"docs/{area['id']}"
    if not os.path.exists(area_dir):
        os.mkdir(area_dir)
    try:
        geojson = wkt_to_json_geometry(area["geometry"])
        with open(f"{area_dir}/geometry.geojson", "w") as f:
            json.dump(geojson, f)
    except Exception as e:
        print(e)


conservation_areas = []
for idx, o in enumerate(csv.DictReader(open(dataset_csv)), start=1):
    o["id"] = f"{idx}:{o['resource']}"  # temporary ids using row number and resource
    create_geometry_file(o, idx)
    del o["geometry"]  # don't need to send to template
    conservation_areas.append(o)
    render(f"{idx}:{o['resource']}/index.html", area_template, con_area=o)

render("index.html", index_template, conservation_areas=conservation_areas)