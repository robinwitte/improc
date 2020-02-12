import numpy as np

class QuadTree():
    """
    A datastructure to compress the data of an image in being able to check pixel-values efficiently

    Attributes
    ----------
    self.starting_pixel : Point-Object containing the coordinates of lower-left pixel that is in the area of this part
    self.width : (horizontal) width of the area spanned by this Quadtree
    self.height : (vertical) height of the area spanned by this Quadtree

    self.NW : QuadTree Object containing information about upper-left child
    self.NE : QuadTree Object containing information about upper-right child
    self.SW : QuadTree Object containing information about lower-left child
    self.SE : QuadTree Object containing information about lower-right child

    value_NW : If there is no NW-child and the upper-left area contains only one pixel-value, this is the value
    value_NE : If there is no NE-child and the upper-right area contains only one pixel-value, this is the value
    value_SW : If there is no SW-child and the lower-left area contains only one pixel-value, this is the value
    value_SE : If there is no SE-child and the lower-right area contains only one pixel-value, this is the value

    Parameters
    ----------
    data : An object containing the (part of the) image we want to make a QuadTree of
    """

    starting_pixel = None
    width = 0
    height = 0

    NW = None
    NE = None
    SW = None
    SE = None

    value_NW = None
    value_NE = None
    value_SW = None
    value_SE = None


    def __init__(self, data, max_depth):
        self.data = data    #maybe omit, if this copies all the data (too time-consuming)
        self.starting_pixel = data[0, 0]
        self.width, self.height = data.shape    #assuming data has an attribute shape
        self.split(data, max_depth)


    def split(self, data, max_depth):
        #TODO :
        #   This method has to do the split of the data. Determine where to split each quadrants in order to get a
        #   good compression of the data, and then overwrite NW, NE, SW, SE. If one of those areas consists of only one
        #   pixel value, set the corresponding value-attribute to this value. Maybe we need a maximum depth for performance
        #   too. Could do optimal split by DP, or maybe there is a greedy approach. Have to assume there are always large
        #   areas with only one value.

        pass

    def check(self, name, points):

        #TODO :
        #   This method should check whether a set of points is contained in a certain polygon named name.
        #   Maybe we only need the pixel-value corresponding to the polygon. Then, we do this recursively, and always pass
        #   the set of points corresponding to one of the quadrants (e.g. half the points have coordinates in upper-left,
        #   then pass the set containing these points to check method of upper-left tree, not individually).


        pass