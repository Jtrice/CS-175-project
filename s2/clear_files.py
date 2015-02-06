import os
import json

def clear_files(files):
    for i in files:
        if os.path.isfile(i):
            os.remove(i)

if __name__=="__main__":
    clear_files(['log.txt','NewCorpus.txt','top25.txt'])
    f = open("var.txt",'wt')
    json.dump([[],[]],f)
