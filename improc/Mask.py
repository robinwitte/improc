from rasterio import features
from rasterio import transform
from improc.QuadTreeBad import QuadTree
import math

class Mask():
    """ A datastructure to store the mask information from the hdf5 file efficiently"""

    def __init__(self):
        self.names = []
        self.data = []
        self.max_depth_of_tree = 5
        self.chunksize = 4000

        # TODO: which informations are also in the hdf5 file and shoud be stored in the mask object
        # TODO: get max_depth_of_tree and chunksize from user input

    def create_data_from_path(self, path):
        """ Function to create the quadtree while reading the file """

        # TODO: read in data in chunks, create the quadtree and store it in self.data and self.names

    def create_data_from_polygons(self, polygons):
        """ Function to create the quadtree from the polygons data """

        # Create array of values in the mask (has to be same length as number of polygons)
        # TODO: choose the right values for the mask
        values = list(range(1,len(polygons.polygons)+1))
        # Create List of tuples (polygon, value)
        tuples = list(zip(polygons.polygons, values))

        # get maximum x and maximum y values
        #max_x = int(math.ceil(max([polygon.bounds[2] for polygon in polygons.polygons])))
        #max_y = int(math.ceil(max([polygon.bounds[3] for polygon in polygons.polygons])))
        max_x = 10000
        max_y = 10000

        for i_y in range(max_y // self.chunksize +1):
            for i_x in range(max_x // self.chunksize +1):
                shiftx = i_x * self.chunksize
                shifty = i_y * self.chunksize
                self.add_new_chunk(features.rasterize(tuples, out_shape = (self.chunksize, self.chunksize), transform = transform.from_origin(shiftx, shifty, 1, -1)))


    def write_data_to_file(self, path):
        """ Function to write the data from the quadtree to an hdf5 file """

        # TODO:
        #       - check path if it's correct
        #       - check if self.data is empty (because of lazy_init) and call create_data_from_polygons(polygons)
        #       - write data from quadtree to the file

    def add_new_chunk(self, data):
        self.data.append(QuadTree(data, self.max_depth_of_tree))
