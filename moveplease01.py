#!/usr/bin/env python3
import shutil
import os
os.chdir('/home/student/Randall_PythonCodeSDE/')
shutil.move('raynor.obj', 'ceph_storage/') #move former to latter folder
xname = input('What is the new name for kerrigan.obj? ') #prompt usr for new file name
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


