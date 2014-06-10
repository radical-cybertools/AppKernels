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
        from radical.ensemblemd.mdkernels import MDTaskDescription

        r1 = MDStepDescription()
        r1.kernel = "NAMD"
        r1.arguments = ["-a1", "-b2", "-c2"]

        r1_bound = r1.bind(resource="stampede.tacc.utexas.edu", cores=16)
        print r1_bound.executable
        print r1_bound.arguments
        print r1_bound.resource
        print r1_bound.input_data
        print r1_bound.output_data


