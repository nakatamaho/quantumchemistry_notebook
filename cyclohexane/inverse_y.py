import sys
import os

argvs = sys.argv
argc = len(argvs)
if (argc != 2):
    print ("splitxyz.py <inputfile> ")
    quit()

filename=argvs[1]

counter=0
with open(filename) as fin:
    line=fin.readline()
    while line:
        atoms=line
        iatoms=int(atoms)
        comment=fin.readline()
        print(atoms.strip())
        print(comment.strip())
        for _lines in range(iatoms):
            _line=fin.readline()
            __line = _line.split()
            ___line = __line[0] + " " + __line[1] + " " +  str(-float(__line[2])) + " " + __line[3] 
            print(___line)
        line = fin.readline()
        if not line:
            break
        if line == "\n":
            break
