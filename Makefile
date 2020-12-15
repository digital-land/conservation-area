init:
	pip3 install -r requirements.txt

collect:
	wget -O data/dataset.csv https://raw.githubusercontent.com/digital-land/conservation-area-collection/main/index/dataset.csv

render:
	digital-land --pipeline-name conservation-area render --dataset-path data/dataset.csv --key-fields "organisation,conservation-area"

local:
	digital-land --pipeline-name conservation-area render --dataset-path data/dataset.csv --local --key-fields "organisation,conservation-area"

build: clean collect render

serve:
	python -m http.server --directory docs

clean:
	rm -r ./docs/
	mkdir docs
