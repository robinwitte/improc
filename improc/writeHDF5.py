
def writeHDF5(path, image):
    """ creates a hdf5 file and writes the mask data

    Parameters
    ----------
    path : A string that is the path to the hdf5 file that will be written
    image : An image object, from which the data will be stored

    Returns
    -------

    """

    # TODO:
    #       - check if path is a correct path
    #       - create file
    #       - write data from the quadtree in image.mask in chunks to the file
    #       - maybe implement Error Messages
