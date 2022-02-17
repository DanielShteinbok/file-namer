#!/usr/bin/env python
import os
import sys

os.chdir(sys.argv[1])
filenames = os.listdir()
# sort files by modification date, assign the list of ordered file names to filenames_sorted
# Oldest file goes first
filenames_sorted = [filestat[1] for filestat in sorted([(os.lstat(filename), filename) for filename in filenames], key=lambda filestat: filestat[0].st_mtime_ns)]

current_file_prefix = "unknown"
file_count = 1

for filename in filenames_sorted:
    # TODO handle multiple '.' in filename
    prefix, suffix = filename.split(".")
    if filename[0] != '2': #should work for the rest of the millenium; would be pretty cool if IPL had this as a problem
        current_file_prefix = prefix
        file_count = 1
    os.rename(filename, current_file_prefix + "_" + str(file_count) + "." + suffix)
    file_count += 1
