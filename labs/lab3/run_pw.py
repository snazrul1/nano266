#!/usr/bin/env python

"""
This is a very simple python starter script to automate a series of PWSCF
calculations. If you don't know Python, get a quick primer from the official
Python documentation at https://docs.python.org/2.7/. The script is deliberately
simple so that only basic Python syntax is used and you can get comfortable with
making changes and writing programs.

Author: Shyue Ping Ong
"""

import os
import shutil
import numpy as np

# Load the Si.pw.in.template file as a template.
with open("PbTiO3.pw.in.template") as f:
    template = f.read()

# Set default values for various parameters
k = 4 # k-point grid of 4x4x4
alat = 7.49 # The lattice parameter for the cell in Bohr.

# Loop through different alat.
for t in [0.45,0.55]:
    # This generates a string from the template with the parameters replaced
    # by the specified values.
    s = template.format(alat=alat, k=k, t=t)

    # Let's define an easy jobname.
    jobname = "PBTiO3_%s_%s_%s" % (alat, k, t)

    # Write the actual input file for PWSCF.
    with open("%s.pw.in" % jobname, "w") as f:
        f.write(s)

    #Print some status messages.
    print("Running with t = %s alat = %s, k = %s..." % (t, alat, k))
    # Run PWSCF. Modify the pw.x command accordingly if needed.
    os.system("pw.x -inp {jobname}.pw.in > {jobname}.out".format(jobname=jobname))

    print("Done. Output file is %s.out." % jobname)

# This just does cleanup. For this lab, we don't need the files that are
# dumped into the tmp directory.
shutil.rmtree("tmp")
