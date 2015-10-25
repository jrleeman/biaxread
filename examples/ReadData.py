from biaxtools import lookdata

print "Reading binary data example P4462:"
binary_data = lookdata.read_binary('p4462_data')
print "Done"

print "Reading ASCII data example P4462:"
binary_data = lookdata.read_ascii('p4462_data.txt')
print "Done"
