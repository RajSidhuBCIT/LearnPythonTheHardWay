from sys import argv
from os.path import exists

script, fromFile, toFile = argv

print(f"Copying from {fromFile} to {toFile}")

inFile = open(fromFile)
inData = inFile.read()

print("The input file is ", len(inData), " bytes long")

print("Does the outfile exist? ", exists(toFile))
print("Ready, hit RETURN to continue or CTRL-C to exit.")
input("< ")

outFile = open(toFile, 'w')
outFile.write(inData)

print("all done")

outFile.close()
inFile.close()