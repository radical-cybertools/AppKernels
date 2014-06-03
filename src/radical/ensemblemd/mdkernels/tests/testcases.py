""" Tests cases
"""
import os
import sys
import unittest


#-----------------------------------------------------------------------------
#
class MDKernelTestCases(unittest.TestCase):
    # silence deprecation warnings under py3

    def setUp(self):
        # clean up fragments from previous tests
        pass

    def tearDown(self):
        # clean up after ourselves 
        pass

    def failUnless(self, expr):
        # St00pid speling.
        return self.assertTrue(expr)

    def failIf(self, expr):
        # St00pid speling.
        return self.assertFalse(expr)

    #-------------------------------------------------------------------------
    #
    def test__one(self):
        """ Test ONE.
        """
        from radical.ensemblemd.mdkernels import MDStepDescription

        r1 = MDStepDescription()
        r1.kernel = "NAMD"
        r1.arguments = ["-a1", "-b2", "-c2"]

        cud = r1.as_compute_unit_description(resource="stampede.tacc.utexas.edu", cores=16)


