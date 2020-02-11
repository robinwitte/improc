
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
    
    # TODO:
    #       - detemine if its a hdf5 file or a json file
    #       - create image object and store data (image = Image(path, lazy_init, True/False))
