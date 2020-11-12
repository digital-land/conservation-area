#!/usr/bin/env python3


def slugify(s):
    return s.lower().replace(" ", "-").replace("/", "")


def suffix_only(i):
    return i.split(":")[1]


def is_empty(v):
    if v is None or v == "":
        return True
    return False


def create_conservation_area_identifier(record):
    if is_empty(record["conservation-area"]) or is_empty(record["name"]):
        return record["id"]
    identifier = f"{suffix_only(record['organisation'])}:{slugify(record['name'])}:{slugify(record['conservation-area'])}"
    return identifier