# Conservation Area

This repo renders the [conservation area pages](https://digital-land.github.io/conservation-area/) on the digital land site.

### Getting started

Install requirements

    make init

To build all pages (using the latest [dataset.csv](https://github.com/digital-land/conservation-area-collection/blob/main/index/dataset.csv)) run

    make build

Fetch latest dataset from the [conservation-area-collection](https://github.com/digital-land/conservation-area-collection).

    make collect

To build pages from `dataset.csv` in `/data`

    make render
