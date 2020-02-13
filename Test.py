import improc
from improc.QuadTree import QuadTree
import numpy as np
import h5py


path_load = '../../inputs/points/B01_1201_annotations_spacing64.npz'
image = improc.load(path_load, True)

test_file = np.load("", allow_pickle=True)["arr_0"]
print(image.mask.data.check(test_file))
