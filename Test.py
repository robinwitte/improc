import improc
from improc.QuadTree import QuadTree
import numpy as np


path_load = 'data/hdf5_image/B01_0361_annotations_si_spacing64.hdf5'
image = improc.load(path_load, True)

test = np.array([[500,250],[0,0],[3,25]])

#array = np.ones((1000,1000))
#print(array)


#tree = QuadTree()

#tree.store_data(array, 100, (0,0), (99,99))


#path_load = 'data/json/B01_0361_annotations.json'
#path_load = 'data/hdf5_image/B01_0361_annotations_si_spacing64.hdf5'


#image = improc.load(path_load, True)


#test = [(100,100,0), (120,143,5), (1000, 300, 200)]

#print(image.check(test))
