import numpy as np

class QuadTree(object):

    def __init__(self, data, max_depth, top_left = None, bottom_right = None):

        if top_left == None:
            top_left = (0,0)
            bottom_right = (data.shape[1]-1, data.shape[0]-1)

        self.top_left = top_left
        self.bottom_right = bottom_right

        if np.all(data == data[0,0], (0,1)):
            self.NW,self.NE, self.SW, self.SE = None,None,None,None
            self.data = None
            self.value = data[0,0]

        elif max_depth <= 0 or data.size < 4:
            self.NW,self.NE, self.SW, self.SE = None,None,None,None
            self.data = data
            self.value = None

        else:
            cut_x = ((bottom_right[0]-top_left[0]) // 2)+1
            cut_y = ((bottom_right[1]-top_left[1]) // 2)+1

            self.NW = QuadTree(data[0:cut_y, 0:cut_x],
                               max_depth - 1,
                               self.top_left, (self.top_left[0]+cut_x-1, self.top_left[1]+cut_y-1))
            self.NE = QuadTree(data[0:cut_y, cut_x:bottom_right[0]+1],
                               max_depth - 1,
                               (self.top_left[0]+cut_x, self.top_left[1]), (self.bottom_right[0], self.top_left[1]+cut_y-1))
            self.SW = QuadTree(data[cut_y:bottom_right[1]+1, 0:cut_x],
                               max_depth - 1,
                               (self.top_left[0], self.top_left[1]+cut_y), (self.top_left[0]+cut_x-1, self.bottom_right[1]))
            self.SE = QuadTree(data[cut_y:bottom_right[1]+1, cut_x:bottom_right[0]+1],
                               max_depth - 1,
                               (self.top_left[0]+cut_x, self.top_left[1]+cut_y), self.bottom_right)
            self.data = None
            self.value = None

    def check(self, x, y, value):
        if self.value != None:
            return value == self.value
        if isinstance(self.data, np.ndarray):
            return value == self.data[y - self.top_left[1], x - self.top_left[0]]
        if x <= self.NW.bottom_right[0]:
            if y <= self.NW.bottom_right[1]:
                return self.NW.check(x,y,value)
            else:
                return self.SW.check(x,y,value)
        if y <= self.NW.bottom_right[1]:
            return self.NE.check(x,y,value)
        else:
            return self.SE.check(x,y,value)
