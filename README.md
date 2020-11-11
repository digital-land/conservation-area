# Conservation Area Geographies

This repo renders the conservation area geogrpahy pages on the digital land site.

### Getting started

Install requirements

    make init

To build all pages (using the latest [dataset.csv](https://raw.githubusercontent.com/digital-land/conservation-area-geography-collection/master/index/dataset.csv)) run

    make build

Fetch latest dataset from the [conservation-area-geography-collection](https://github.com/digital-land/conservation-area-geography-collection/tree/national-dataset).

    make collect

To build pages from `dataset.csv` in `/data`

    make render
