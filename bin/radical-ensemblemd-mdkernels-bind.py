#!/usr/bin/env python

import sys
import pprint
import radical.ensemblemd.mdkernels as mdk

if len(sys.argv) != 3:
    print """

    usage: %s <kernel> <resource>

    """ % sys.argv[0]
    sys.exit(-1)


td = mdk.MDTaskDescription()
td.kernel=(sys.argv[1])

print '------------------------'
print 'INPUT:'
pprint.pprint(td.as_dict())
print '------------------------'
print 'OUTPUT:'
pprint.pprint(td.bind (sys.argv[2]).as_dict())
print '------------------------'

