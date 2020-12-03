init:
	pip3 install -r requirements.txt

collect:
	wget -O data/dataset.csv https://raw.githubusercontent.com/digital-land/conservation-area-collection/main/index/dataset.csv

render:
	python render.py

local:
	python render.py --local

build: clean collect render

clean:
	rm -r ./docs/
	mkdir docs
