include makerules/makerules.mk
include makerules/render.mk

DATASET_PATH := data/dataset.csv
DATASET := conservation-area

collect:
	wget -O $(DATASET_PATH) https://raw.githubusercontent.com/digital-land/$(DATASET)-collection/main/dataset/$(DATASET).csv

local: clean
	@-mkdir ./docs/
	digital-land --pipeline-name $(DATASET) render --dataset-path $(DATASET_PATH) --local

build: clean collect render
