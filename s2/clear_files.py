import os
import json

def clear_files(files):
    for i in files:
        if os.path.isfile(i):
            os.remove(i)
            
def empty_files(files):
    for i in files:
        open(i,'wt').close()

if __name__=="__main__":
    #clear_files(['log.txt','NewCorpus.txt','top25.txt',"Rising10.txt"])
    empty_files(['log.txt','NewCorpus.txt','top25.txt',"Rising10.txt","var.txt"])
    
