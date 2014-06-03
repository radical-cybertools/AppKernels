from radical.ensemblemd.mdkernels import MDStepDescription

r1 = MDStepDescription()
r1.kernel = "NAMD"
r1.arguments = ["-a1", "-b2", "-c2"]

# Return a RADICAL-Pilot ComputeUnitDescription of the MD step that can
# run on 16-cores on 'stampede'.
cud = r1.as_compute_unit_description(resource="stampede.tacc.utexas.edu", cores=16)
