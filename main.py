
# Fast Api imports.
from fastapi import FastAPI, File, UploadFile
from starlette.responses import StreamingResponse
# Io Imports
import io

# Fuctions imports.
from fuctions import get_attributes, get_NDVI, get_thumbnail


app = FastAPI()


@app.post("/attributes")
async def attributes(file: UploadFile = File(...)):
    """Attributes
    This endpoint recive a image an return some attributes

    Returns:
        JSON: image_size(width and height), number of brands,
        coordinate reference system and georeferenced bounding box 
    """

    return get_attributes(file.file._file)


@app.post("/thumbnail")
def thumbnail(file: UploadFile = File(...)):
    """Thumbnail
    This endpoint return a thumbnail PNG of de image.

    Returns:
        PNG 
    """
    img = get_thumbnail(file.file._file)
    # return StreamingResponse(io.BytesIO(img.tobytes()), media_type="image/png")


@app.post("/ndvi")
def ndvi(file: UploadFile = File(...)):
    """NDVI
    This endpoint return a PNG image. 

     Returns:
        PNG
    """
    ndvi = get_NDVI(file.file._file)

    return StreamingResponse(io.BytesIO(ndvi.tobytes()), media_type="image/png")
