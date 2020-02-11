class Polygons():
    """ A datastructure to store the polygon information from the json file"""

    def __init__(self, path):
        self.names = []
        self.polygons= []

        # TODO: should we let the data in a dictionary structure?

    def create_data_from_path(self, path):
        """ Function to read JSON file  """

        # TODO: read in data and store it in self.names and

    def create_data_from_mask(self, polygons):
        """ Function to create the polygons from the mask """

        # TODO: create the quadtree and store it in self.data (I don't think we will get this task done)

    def write_data_to_file(self, path):
        """ Function to write the data to an json file """

        # TODO:
        #       - check path if it's correct
        #       - check if self.data is empty (because of lazy_init) and call create_data_from_polygons(polygons)
        #       - write data from quadtree to the file
