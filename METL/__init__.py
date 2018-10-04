# -*- coding: utf-8 -*-
from .utils import get_data, download_all, make_all_again
from .utils import jis2utf 
from .utils import save_images_hdf5, load_images_hdf5
from .utils import save_labels_pickle, load_labels_pickle
#from .utils import list2OnehotMartix
from .utils import for_sklearn
from .utils import make_ETL1, make_ETL3, make_ETL4, make_ETL5
from .utils import make_ETL6, make_ETL7, make_ETL8G, make_ETL9G
from .utils import InMemoryZip

__version__ = '0.0.1'
__author__ = 'Shin Asakawa'
__license__ = 'Apache License, Version 2.0'
__email__ = 'asakawa@ieee.org'
__copyright__ = 'Copyright 2018 {0}'.format(__author__)
