from sys import argv
from os.path import exists

script, to_file_num = argv
to_file = "ex"+to_file_num+".py"
print "Copying from ex1.py to %s" % (to_file)
indata = open("ex1.py").read()
out_file = open(to_file, 'w')
out_file.write(indata)
out_file.close()
print "...complete"
