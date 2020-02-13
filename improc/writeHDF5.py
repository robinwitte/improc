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

    chunk_vl, chunk_vr = np.array_split(dset, 2, axis=1)
    chunk_ul, chunk_bl = np.array_split(chunk_vl, 2, axis=0)
    chunk_ur, chunk_br = np.array_split(chunk_vr, 2, axis=0)
    chunks = [chunk_ul, chunk_ur, chunk_bl, chunk_br]

    """
    => uncomment this 3 splits are needed.
    
    chunk_vl, chunk_vm, chunk_vr = np.array_split(dset,3, axis=1)
    chunk_ul,chunk_ml, chunk_bl = np.array_split(chunk_vl, 3, axis=0)
    chunk_mu,chunk_mm, chunk_mb = np.array_split(chunk_vr, 3, axis=0)
    chunk_ur,chunk_mr, chunk_br = np.array_split(chunk_vr, 3, axis=0)

    chunks= [chunk_ul,chunk_mu, chunk_ur, 
             chunk_ml,chunk_mm, chunk_mr,
             chunk_bl,chunk_mb, chunk_br]
    """

    if save_files == True:
        for index,chunk in enumerate(chunks):
            imgplot = plt.imshow(chunk)
            plt.savefig(f"image{index}.png")

    return chunks
