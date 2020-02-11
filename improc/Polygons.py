import json

class Polygons():
    """ A datastructure to store the polygon information from the json file"""

    def __init__(self):
        self.names = []
        self.polygons= []
        self.data=[]


    def create_data_from_path(self, path):
        """ Function to read JSON file  """

        with open(path) as json_file:
            self.data = json.load(json_file)
        self.names, self.polygons, _ = [[d[k] for d in self.data] for k in sorted(self.data[0].keys())]


    def create_data_from_mask(self, mask):
        """ Function to create the polygons from the mask """

        # TODO: create the quadtree and store it in self.data (I don't think we will get this task done)

    def write_data_to_file(self, path):
        """ Function to write the data to an json file """

        # TODO:
        #       - check path if it's correct
        #       - check if self.data is empty (because of lazy_init) and call create_data_from_polygons(polygons)
        #       - write data from quadtree to the file
