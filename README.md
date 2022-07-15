# Sentinel 2

This is a small project that process file ".tiff" and extrac some information

## Install.

Windows
py -m pip install -r requirements.txt

MacOS/Linux
python -m pip install -r requirements.txt

## Run project.

uvicorn main:app --reload

# Execution process.

For it to work you must send a ".tiff" file.

## "/attributes".

Recive a file and return a json with 'Size File ', "Number of Brands", "Coordinate Reference System", "Georeferenced Bounding Box"

## "/thumbnail".

Recive a file and return a thumbnail PNG image.

## "/ndvi".

Recive a file and processing the information to generate a PNG image with normalized difference vegetation index.
