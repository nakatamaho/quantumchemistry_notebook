import sys
import os

argvs = sys.argv
argc = len(argvs)
if (argc != 3):
    print ("splitxyz.py <inputfile> <outputbasename>")
    quit()

filename=argvs[1]
outbasename=argvs[2]    

counter=0
with open(filename) as fin:
    line=fin.readline()
    while line:
        atoms=line
        iatoms=int(atoms)
        comment=fin.readline()
        _counter = str(counter).zfill(4)  #xyz file counter
        filenamewoxyz = os.path.splitext(os.path.basename(filename))[0]
        outfilename = outbasename + "." + _counter + ".xyz"
        print("output: %s " % outfilename)
        with open(outfilename, 'w') as f:
            f.write(atoms)
            f.write(comment)        
            for _lines in range(iatoms):
                _line=fin.readline()
                f.write(_line)
        counter=counter+1
        line = fin.readline()
