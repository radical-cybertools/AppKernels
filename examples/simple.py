from radical.ensemblemd.mdkernels import MDStepDescription

r1 = MDStepDescription()
r1.kernel = "NAMD"
r1.arguments = ["-a1", "-b2", "-c2"]

# Bind the MDStepDescription to the NAMD installation on the 'strampede' HPC cluster.
r1_bound = r1.bind(resource="stampede.tacc.utexas.edu", cores=16)

# In RADICAL Pilot, this can then be used like this:
#cud = radical.pilot.ComputeUnitDescription()
#cud.executable = r1_bound.executable
#cud.arguments  = r1_bound.arguments
