#!/usr/bin/env python3
""" Demonstrating Subprocesses"""
__author__= 'Eva Linehan (eva.linehan18@imperial.ac.uk)'
__version__ = 0.01
__date__ = 'Nov 2018'
__licence__ = 'OS Practical'

import subprocess

p = subprocess.Popen("/usr/bin/env Rscript --verbose fmr.R", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = p.communicate()
print(stdout.decode())
print("Script ran successfully")