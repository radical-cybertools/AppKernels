from radical.ensemblemd.mdkernels import MDTaskDescription

r1 = MDTaskDescription()
r1.kernel     = "SYNAPSE_PROFILE"
r1.executable = "application"
r1.arguments  = ["-a1", "-b2", "-c2"]

# Bind the MDStepDescription to the NAMD installation on the 'strampede' HPC cluster.
r1_bound = r1.bind(resource="stampede.tacc.utexas.edu")

import pprint
pprint.pprint (r1_bound.as_dict())

# In RADICAL Pilot, this can then be used like this:
#cud = radical.pilot.ComputeUnitDescription()
#cud.executable = r1_bound.executable
#cud.arguments  = r1_bound.arguments

