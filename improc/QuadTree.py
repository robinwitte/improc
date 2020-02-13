import numpy as np
import h5py

class QuadTree():
    """
    A datastructure to compress the data of an image in being able to check pixel-values efficiently

    Attributes
    ----------
    self.starting_pixel : Point-Object containing the coordinates of lower-left pixel that is in the area of this part

    self.x_start : x-coordinate of starting pixel
    self.y_start : y-coordinate of starting pixel
    self.width : (horizontal) width of the area spanned by this Quadtree
    self.height : (vertical) height of the area spanned by this Quadtree
    self.data : contains data as image if necessary (only at bottom level)

    self.NW : QuadTree Object containing information about upper-left child
    self.NE : QuadTree Object containing information about upper-right child
    self.SW : QuadTree Object containing information about lower-left child
    self.SE : QuadTree Object containing information about lower-right child

    self.value : If this represents homogeneous field, contains value of this field

    Parameters
    ----------
    data : An object containing the (part of the) image we want to make a QuadTree of
    """

    #starting_pixel = None
    x_start = 0
    y_start = 0
    width = 0
    height = 0
    data = None
    value = None

    NW = None
    NE = None
    SW = None
    SE = None


    def __init__(self, data, max_depth, x_start = 0, y_start = 0, previously = False):
        self.data = data    #maybe omit, if this copies all the data (too time-consuming)
        #self.starting_pixel = data[0, 0] don´t need this any more
        self.width, self.height = data.shape    #assuming data has an attribute shape
        self.x_start = x_start
        self.y_start = y_start
        self.split(data, max_depth, previously)


    def split(self, data, max_depth, previously):
        """

        :param data: assume this is a numpy array
        :param max_depth: if this is 0, don´t split further
        :return: nothing, writes in attributes for children
        """
        small_enough = (self.width < 5000 & self.height < 5000)
        if max_depth != 0:
            cut_x = self.width // 2
            cut_y = self.height // 2
            self.NW = QuadTree(data[0:cut_y, 0:cut_x], max_depth - 1, x_start=self.x_start, y_start=self.y_start, previously = small_enough)
            self.NE = QuadTree(data[0:cut_y, cut_x + 1: self.width], max_depth - 1, x_start=cut_x + 1 + self.x_start, y_start=self.y_start, previously = small_enough)
            self.SW = QuadTree(data[cut_y + 1:self.height, 0:cut_x], max_depth - 1, x_start=self.x_start, y_start=cut_y + 1 + self.y_start, previously = small_enough)
            self.SE = QuadTree(data[cut_y + 1:self.height, cut_x + 1:self.width], max_depth - 1, x_start=cut_x + 1 + self.x_start, y_start=cut_y + 1 + self.y_start, previously = small_enough)
            if small_enough & (not previously):
                self.bottom_up(data)
            elif not small_enough:
                self.bottom_up(data)
        else:
            self.data = data

        #TODO : is image big enough to do the split max_depth-times

    def bottom_up(self, data):
        """
        :param data:
        :param max_depth:
        :return:
        """
        if self.NW == None:
            #now, we are at one of the leaves
            mean = np.mean(data)
            #mean == 0 => all values are 0
            #mean == 1 => all values are equal to 1. More Polygons: mean 2, 3, 4, ...
            if mean.is_integer():
                self.value = int(mean)
                return int(mean)
            else:
                return None

        else:
            NW_val = self.NW.bottom_up(self.NW.data)
            NE_val = self.NE.bottom_up(self.NE.data)
            SW_val = self.SW.bottom_up(self.SW.data)
            SE_val = self.SE.bottom_up(self.SE.data)

            #then, we can merge
            if len({NW_val, NE_val, SW_val, SE_val}) == 1 and NW_val is not None:
                self.value = NW_val
                self.NW = None
                self.NE = None
                self.SW = None
                self.SE = None
            return self.value


    def check(self, points):

        val = self.value
        if val is not None:
            ret = val == 1
            n = points.shape[0]
            return np.full(n, ret)
        else:
            if self.data is not None:
                return [self.data[p[1],p[0]] == 1 for p in points]
            arr = np.full(points.shape[0], False)
            NW_array = []
            NE_array = []
            SW_array = []
            SE_array = []
            if self.NW is not None:
                NW_array = self.NW.check(points[(points[:, 0] <= self.x_start + self.width // 2) & (points[:, 1] <= self.y_start + self.height // 2)])
            if self.NE is not None:
                NE_array = self.NE.check(points[(points[:, 0] > self.x_start + self.width // 2) & (points[:, 1] <= self.y_start + self.height // 2)])
            if self.SW is not None:
                SW_array = self.SW.check(points[(points[:, 0] <= self.x_start + self.width // 2) & (points[:, 1] > self.y_start + self.height // 2)])
            if self.SE is not None:
                SE_array = self.SE.check(points[(points[:, 0] > self.x_start + self.width // 2) & (points[:, 1] > self.y_start + self.height // 2)])
            arr[(points[:, 0] <= self.x_start + self.width // 2) & (points[:, 1] <= self.y_start + self.height // 2)] = NW_array
            arr[(points[:, 0] > self.x_start + self.width // 2) & (points[:, 1] <= self.y_start + self.height // 2)] = NE_array
            arr[(points[:, 0] <= self.x_start + self.width // 2) & (points[:, 1] > self.y_start + self.height // 2)] = SW_array
            arr[(points[:, 0] > self.x_start + self.width // 2) & (points[:, 1] > self.y_start + self.height // 2)] = SE_array
            return arr
