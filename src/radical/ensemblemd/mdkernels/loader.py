__copyright__ = "Copyright 2014, http://radical.rutgers.edu"
__license__   = "MIT"
__author__    = "Ole Weidner <ole.weidner@rutgers.edu>"

import os
import glob
from logger import logger
from radical.utils.singleton import Singleton

# -----------------------------------------------------------------------------
#
class _KernelDict(object):
    """Singleton class to initialize the kernel configuration dictionary.
    """
    __metaclass__ = Singleton

    def __init__(self):
        """Create or get a new instance (singleton).
        """
        # keneldict holds all configuration
        self._kerneldict = dict()

        cwd = os.path.dirname(os.path.realpath(__file__))
        config_files = glob.glob("{0}/configs/*.json".format(cwd))

        for f in config_files:
            logger.debug(f)

    def get(self):
        """Return the kernel dictionary.
        """
        return self._kerneldict

# -----------------------------------------------------------------------------
#
kerneldict = _KernelDict().get()
