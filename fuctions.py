# Imports.
import rasterio
import json
import matplotlib.pyplot as plt
import numpy as np


def get_attributes(file):
    """get_attributes
    This fuctions obtains atributes of de tff file

    Args:
        file (tiff): tiff file

    Returns:
        JSON: "Size File" ,
        "Number of Brands",
        "Coordinate Reference System",
        "Georeferenced Bounding Box"
    """
    dataset = rasterio.open(file)

    number_brands = {i: dtype for i, dtype in zip(
        dataset.indexes, dataset.dtypes)}

    attributes = json.dumps({
        "Size File": [dataset.width, dataset.height],
        "Number of Brands": str(number_brands),
        "Coordinate Reference System": str(dataset.crs),
        "Georeferenced Bounding Box": [dataset.bounds]
    })
    return attributes


def get_thumbnail(file):
    """get thumbnail
    This fuctions obtains thumbail of de tff 

    Args:
        file (tiff): tiff file

    Returns:
        PNG: png image
    """
    dataset = rasterio.open(file)
    band_blue = dataset.read(3)
    band_green = dataset.read(2)
    band_red = dataset.read(1)
    img = np.dstack((band_red, band_green, band_blue, ))
    plt.imshow(img)
    plt.savefig("thumbnail.png")
    return plt.imread(r"thumbnail.png")


def get_NDVI(image):
    """get ndvi

    Args:
        file (tiff): tiff file

    Returns:
        PNG: png image
    """

    # Load File
    dataset = rasterio.open(image)

    # NDVI Calculate
    band_red = dataset.read(3)
    band_nir = dataset.read(4)
    ndvi = (band_nir.astype(float) - band_red.astype(float)) / \
        (band_nir + band_red)

    # Create NDVI Image
    kwargs = dataset.meta
    kwargs.update(
        dtype=rasterio.float32,
        count=1)
    with rasterio.open('ndvi.tif', 'w', **kwargs) as dst:
        dst.write_band(1, ndvi.astype(rasterio.float32))

    plt.imsave("ndvi_cmap.png", ndvi, cmap=plt.cm.summer)
    img = plt.imread(r"ndvi_cmap.png")
    return img
