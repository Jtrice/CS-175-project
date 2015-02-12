import os
def clear_files(files):
    for i in files:
        os.remove(i)

if __name__ == "__main__":
    clear_files(["NewCorpus.txt","Top25.txt","Rising10.txt","log.txt"])
