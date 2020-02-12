import json
from shapely.geometry import Polygon

class Polygons():
    """ A datastructure to store the polygon information from the json file"""

    def __init__(self):
        self.names = []
        self.polygons= []
        self.data=[]


    def create_data_from_path(self, path):
        """ Function to read JSON file  """

        with open(path, 'r') as json_file:
            self.data = json.load(json_file)
        self.names, self.polygons, _ = [[d[k] for d in self.data] for k in sorted(self.data[0].keys())]
        self.polygons = [Polygon(polygon) for polygon in self.polygons]


    def create_data_from_mask(self, mask):
        """ Function to create the polygons from the mask """

        print("Polygons.create_data_from_mask: not implemented yet")
        # TODO: create the polygons and store it in self.data, self.names and self.polygons (I don't think we will get this task done)


    def write_data_to_file(self, path):
        """ Function to write the data to an json file """

        with open(path, 'w') as json_file:
            json.dump(self.data, json_file)
