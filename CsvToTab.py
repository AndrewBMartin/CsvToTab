import os
import csv
import glob


def CsvToTab(old_dir, new_dir):
    """
    Convert all the csv files associated with a GMPL model
    to AMPL format .tab files.
    
    Assumed that you already have a directory - the 
    old directory - with all
    your csv files in it, and you want to write them
    to a new directory as tab files.
    
    If the new directory supplied does not exist, it
    is created.
    
    Will create tab versions of every csv file in the
    old directory.
    
    For the purposes of AMPL headers, if there are n
    headers in the GMPL csv then n - 1 are assumed to 
    be keys, and 1 is assumed to be a value.
    """
    
    # Create new directory.
    # If the new directory already exists pass.
    # If the directory name given is not a valid
    # directory name then an error will be raised
    # when trying to open a file in the new directory.
    try:
        os.mkdir(new_dir)
    except Exception, e:
        pass
    
    # Collect all csv files in the old directory
    files = glob.glob(os.path.join(old_dir, "*.csv"))
    for f in files:
        with open(f, "rb+") as read_file:
            rf = csv.reader(read_file)
            with open(os.path.join(new_dir, os.path.basename(f)), "wb+") as write_file:
                wf = csv.writer(write_file, delimiter="\t")
                
                # Make AMPL header
                headers = rf.next()
                keys = len(headers) - 1
                vals = 1
                wf.writerow(["ampl.tab", keys, vals])
                wf.writerow(headers)
                
                # Write CSV data as TAB data
                rows = list(rf)
                wf.writerows(rows)
                
        print "{0} has been converted from CSV to AMPL tab".format(f)
