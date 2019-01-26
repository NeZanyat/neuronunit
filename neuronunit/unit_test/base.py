"""Common imports for many unit tests in this directory"""

import unittest
import sys
import os
import warnings
import pdb
try:  # Python 2
    from urllib import urlretrieve
except ImportError:  # Python 3
    from urllib.request import urlretrieve

import matplotlib as mpl
mpl.use('Agg')  # Avoid any problems with Macs or headless displays.

from sciunit.utils import NotebookTools, import_all_modules
import neuronunit
from neuronunit.models import ReducedModel
from neuronunit import neuroelectro, bbp, aibs, tests as nu_tests

OSX = sys.platform == 'darwin'
NU_BACKEND = os.environ.get('NU_BACKEND', 'jNeuroML')
