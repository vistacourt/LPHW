from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)


# in_file = open(from_file)
indata = open(from_file).read()


print "%d bytes long" % len(indata)

print "file exists? %r" % exists(to_file)
print raw_input("Ready?")

out_file = open(to_file, 'w')
out_file.write(indata)

out_file.close()
in_file.close()
