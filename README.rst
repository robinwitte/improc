========
Improc
========

Improc reads and writes big 2-dimensional data. It has a Data-Structure Image which stores a mask-image and corresponding polygons.
It can translate the mask-information to the polygon-information (and vice-versa) and store it in a hdf5 or an json file.


Example
=======

Here's an example of some basic features that Improc provides.

.. code-block:: python

    import numpy as np
    import improc

    # Read in hdf5 data
    test_path = 'testfile.hdf5'
    image = improc.load(test_path, lazy_init = True) # if lazy_init is False: it will create the polygon data as well

    # Read in json data
    test_path = 'testfile.json'
    image = improc.load(test_path, lazy_init = True) # if lazy_init is False: it will create the mask data as well

    # Check points
    test_points = np.array([[100,100],[250,250]])
    image.check(test_points)

    # Save polygon data
    test_path = 'testfile.json'
    improc.writeJSON(test_path, image)

    # Save mask data
    test_path = 'testfile.hdf5'
    improc.writeHDF5(test_path, image)


Status at the end of the project
=======

Reading json and hdf5 does work.

Checking of points does work, even if the implementation should be optimized.

The translation from polygon, to mask data worked at a point,
but we changed the QuadTree implementation on the last day and didn't have time to change the translation method.

Writing the hdf5 file and translate the mask data in polygon data was not implemented yet.
