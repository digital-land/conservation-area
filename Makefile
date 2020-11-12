init:
	pip3 install -r requirements.txt

collect:
	wget -O data/dataset.csv https://raw.githubusercontent.com/digital-land/conservation-area-geography-collection/master/index/dataset.csv

render:
	python render.py

render/local:
	python render.py --local

build: clean collect render

clean:
	rm -r ./docs/
	mkdir docs
