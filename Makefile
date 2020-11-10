init:
	pip3 install -r requirements.txt

collect:
	wget -O data/dataset.csv https://raw.githubusercontent.com/digital-land/conservation-area-geography-collection/national-dataset/index/dataset.csv

render:
	python render.py

clean:
	rm -r ./docs/
	mkdir docs
