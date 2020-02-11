class Mask():
    """ A datastructure to store the mask information from the hdf5 file efficiently"""

    def __init__(self):
        self.names = []
        self.data = []

        # TODO: which informations are also in the hdf5 file and shoud be stored in the mask object

    def create_data_from_path(self, path):
        """ Function to create the quadtree while reading the file """

        # TODO: read in data in chunks, create the quadtree and store it in self.data and self.names

    def create_data_from_polygons(self, polygons):
        """ Function to create the quadtree from the polygons data """

        # TODO: create the quadtree and store it in self.data (I don't think we will get this task done)

    def write_data_to_file(self, path):
        """ Function to write the data from the quadtree to an hdf5 file """

        # TODO:
        #       - check path if it's correct
        #       - check if self.data is empty (because of lazy_init) and call create_data_from_polygons(polygons)
        #       - write data from quadtree to the file
