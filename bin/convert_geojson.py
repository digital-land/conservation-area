#!/usr/bin/env python3


def wkt_to_json_geometry(wkt):
    prefix = "MULTIPOLYGON ((("
    if not wkt.startswith(prefix):
        raise ValueError(f"cannot parse wkt: {wkt[0:20]}")

    values = wkt[len(prefix) : -len(")))")]
    coords = [
        [float(lon), float(lat)]
        for lon, lat in (point.split() for point in values.split(","))
    ]

    result = {
        "type": "MultiPolygon",
        "coordinates": [[coords]],
    }

    return result
