from improc.Image import Image

def load(path, lazy_init = False):
    """

    Parameters
    ----------
    path : A string that is the path to the hdf5 or json file
    lazy_init : flag to determine if the mask and the polygons both will be stored in the image object

    Returns
    -------
    image object
    """

    # Check for correct path
    if not isinstance(path, str) or (not path.endswith('.json') and not path.endswith('.hdf5')):
        raise TypeError("invalid path or file: {0!r}".format(path))

    hdf5 = False
    if path.endswith('.hdf5'):
        hdf5 = True

    return Image(path, lazy_init, hdf5)
