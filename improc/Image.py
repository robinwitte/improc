class Image():
    """ A datastructure to store the image information

    Attributes
    ----------
    self.mask : a Mask object
    self.polygons : a Polygons object

    Parameters
    ----------
    path : A string that is the path to the hdf5 or json file
    lazy_init : flag to determine if the mask and the polygons both will be stored in the image object
    hdf5 : flag if its a path to hdf5 or to json
    """

    def __init__(self, path, lazy_init, hdf5):
        self.mask = Mask()
        self.polygons = Polygons()

        if hdf5:
            self.mask.create_data_from_path(path)
        else:
            self.polygons.
        self.polygons= []

        # TODO: should we let the data in a dictionary structure?
