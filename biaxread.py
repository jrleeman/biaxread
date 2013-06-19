import numpy as NP
import sys

def ReadBiax(f_name):

	filename = f_name
	
	datafile = open(filename,'r')
	
	col_width = 12 # Columns are 12 char wide in header
	
	# First line of the file is the number of records
	num_recs = datafile.readline()
	num_recs = int(num_recs.strip('number of records = '))
	print "\nNumber of records: %d" %num_recs
	
	# Second line is column numbers, we don't care so just count them
	num_cols = datafile.readline()
	num_cols = num_cols.split('col')
	num_cols = len(num_cols)
	print "Number of columns: %d" %num_cols
	
	# Third line is the column headings
	col_headings_str = datafile.readline()
	col_headings_str = col_headings_str[5:-1]
	col_headings = []
	for i in xrange(len(col_headings_str)/12):
	    heading = col_headings_str[12*i:12*i+12].strip()
	    col_headings.append(heading)
	
	# Fourth line is column units
	col_units_str = datafile.readline()
	col_units_str = col_units_str[5:-1]
	col_units=[]
	for i in xrange(len(col_units_str)/12):
	    heading = col_units_str[12*i:12*i+12].strip()
	    col_units.append(heading)
	col_units = [x for x in col_units if x != '\n']  #Remove newlines
	
	# Fifth line is number of records per column
	col_recs = datafile.readline()
	col_recs = col_recs.split('recs')
	col_recs = [int(x) for x in col_recs if x != '\n']
	
	# Show column units and headings
	print "\n\n-------------------------------------------------"
	print "|%15s|%15s|%15s|" %('Name','Unit','Records')
	print "-------------------------------------------------"
	for column in zip(col_headings,col_units,col_recs):
		print "|%15s|%15s|%15s|" %(column[0],column[1],column[2])
	print "-------------------------------------------------"
	
	# Read the data into a numpy recarray
	dtype=[]
	dtype.append(('row_num','float'))
	for name in col_headings:
		dtype.append((name,'float'))
	dtype = NP.dtype(dtype)
	
	data = NP.zeros([num_recs,num_cols])
	
	i=0
	for row in datafile:
		row_data = row.split()
		for j in xrange(num_cols):
			data[i,j] = row_data[j]
		i+=1
	data_rec = NP.rec.array(data,dtype=dtype)
	
	datafile.close()
	
	return data_rec
	