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
    be keys, and 1 is assumed to be a value. If the file
    is a single column of data then the column is 
    recorded as values.
    """
    
    # Create directory
    try:
        os.mkdir(new_dir)
    except Exception, e:
        print "directory exitsts"
        
    # Get all csv files in the old directory
    files = glob.glob(os.path.join(old_dir, "*.csv"))
    
    keys = ""
    rows = []
    headers = []
    vals = ""
    
    # Go through each file. Read its contents.
    # Determine its header. Then write to
    # a tab file.
    for file in files:
        # Separate the filename from its path and .csv extension.
        # Add the .tab extension.
        new_location = "{0}.{1}".format(os.path.splitext(
                              os.path.basename(file))[0], "tab")
        
        with open(file, "rb+") as read_file:
            rf = csv.reader(read_file)
            headers = rf.next()
            keys = len(headers) - 1
            vals = 1
            rows = list(rf)
            
        with open(os.path.join(new_dir, new_location ), "wb+") as write_file:
            wf = csv.writer(write_file, delimiter="\t")
            
            # Single column file
            if keys == 0:
                wf.writerow(["ampl.tab 1"])
            # Multiple column file
            else:
                wf.writerow(["ampl.tab {0} {1}".format(keys, vals)])
                
            wf.writerow(headers)
            wf.writerows(rows)
        print "{0} converted to AMPL tab".format(file)
