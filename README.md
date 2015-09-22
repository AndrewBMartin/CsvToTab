# CsvToTab
Convert GMPL csv files to AMPL tab files

Convert all the csv files associated with a GMPL model
in a particular directory to AMPL format .tab files
in a new directory!

It's assumed that you already have a directory - the 
old directory - with all your csv files in it, 
and you want to write them to a new directory - the
new directory - as tab files.

If the new directory supplied does not exist, it
is created. If there's a problem with the old or new
directory name, e.g. it's not a valid directory
name, CsvToTab will fail.

CsvToTab will create tab versions of every csv file in the
old directory.
    
For the purposes of AMPL headers, if there are n
headers in the GMPL csv then n - 1 are assumed to 
be keys, and 1 is assumed to be a value.
