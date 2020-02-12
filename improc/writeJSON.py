
import json

def writeJSON(path, image):
    """ creates a json file and writes the polygon data

    Parameters
    ----------
    path : A string that is the path to the json file that will be written
    image : An image object, from which the data will be stored

    Returns
    -------

    """

    # Check for correct path
    if not isinstance(path, str) or not path.endswith('.json'):
        raise TypeError("invalid path or file: {0!r}".format(path))

    # Check if image object has polygon data
    if not image.polygons.data:
        image.polygons.create_data_from_mask(image.mask)

    # write data to file
    image.polygons.write_data_to_file(path)
