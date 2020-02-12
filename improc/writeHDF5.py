import h5py
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

""" creates a hdf5 file and writes the mask data

Parameters
----------
path : A string that is the path to the hdf5 file that will be written
image : An image object, from which the data will be stored

Returns
-------

"""


# TODO:
#       - check if path is a correct path
#       - create file
#       - write data from the quadtree in image.mask in chunks to the file
#       - maybe implement Error Messages

#def writeHDF5(path:str, image):


def writeHDF5(path: str, save_files=True):

    f = h5py.File(path, 'r')

    keys =list(f.keys())

    dset = f[keys[0]]

    x = round(dset.shape[0] / 10)
    y = round(dset.shape[1] / 10)

    chunk1 = dset[:x, :y]
    chunk2 = dset[x + 1:(2 * x), y + 1:(2 * y)]
    chunk3 = dset[(2 * x) + 1:(3 * x), (2 * y) + 1:(3 * y)]
    chunk4 = dset[(3 * x) + 1:(4 * x), (3 * y) + 1:(4 * y)]
    chunk5 = dset[(4 * x) + 1:(5 * x), (4 * y) + 1:(5 * y)]
    chunk6 = dset[(5 * x) + 1:(6 * x), (5 * y) + 1:(6 * y)]
    chunk7 = dset[(6 * x) + 1:(7 * x), (6 * y) + 1:(7 * y)]
    chunk8 = dset[(7 * x) + 1:(8 * x), (7 * y) + 1:(8 * y)]
    chunk9 = dset[(8 * x) + 1:(9 * x), (8 * y) + 1:(9 * y)]
    chunk10 = dset[(9 * x) + 1:, (9 * y) + 1:]

    chunks = [chunk1, chunk2, chunk3, chunk4, chunk5, chunk6, chunk7, chunk8, chunk9, chunk10]

    plt.savefig("try.png")

    if save_files == True:
        for index,chunk in enumerate(chunks):
            imgplot = plt.imshow(chunk)
            plt.savefig(f"image{index}.png")

    return chunks
