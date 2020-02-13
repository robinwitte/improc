from improc.Mask import Mask
from improc.Polygons import Polygons

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
        #width

        if hdf5:
            self.mask.create_data_from_path(path)
            if not lazy_init:
                self.polygons.create_data_from_mask(self.mask)
        else:
            self.polygons.create_data_from_path(path)
            if not lazy_init:
                self.mask.create_data_from_polygons(self.polygons)

    def check(self, checks):
        #cs = self.mask.chunksize
        # y chunk is missing (after (x//cs): + ((self.width+cs)*(y//cs))
        #return [self.mask.data[(x//cs)].check(x-(x//cs)*cs, y-(y//cs)*cs, value) for (x,y,value) in checks]
        return self.mask.data.check(checks)
