import improc
from improc.QuadTree import QuadTree
import numpy as np
import h5py


path_load = 'C:/Users/phili/PycharmProjects/untitled2/data/hdf5_image/B01_0361_annotations_si_spacing64.hdf5'
image = improc.load(path_load, True)

test_file = np.load("", allow_pickle=True)["arr_0"]
print(image.mask.data.check(test_file))
