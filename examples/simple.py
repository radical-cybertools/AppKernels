from radical.ensemblemd.mdkernels import MDStepDescription

r1 = MDStepDescription()
r1.kernel = "NAMD"
r1.arguments = ["-a1", "-b2", "-c2"]

# Bind the MDStepDescription to the 'strampede' HPC cluster.
r1_bound = r1.bind(resource="stampede.tacc.utexas.edu", cores=16)
print r1_bound.executable
print r1_bound.arguments
print r1_bound.resource
print r1_bound.input_data
print r1_bound.output_data