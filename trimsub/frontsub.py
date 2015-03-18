import matplotlib.pyplot as plt
import numpy as np
import read_post
import operator

def get_top25_subreddits():
    top25 = {}
    f = open("Data/Top25.txt")
    for line in f.readlines():
        d = read_post.read_post(line)
        if d["subreddit"] not in top25.keys(): top25[d["subreddit"]] = 0
    return top25.keys()

def trim():
    top25 = get_top25_subreddits()
    f = open("Data/NewCorpus.txt")
    out = open("Out/Corpus.txt",'wt')
    index = 0
    for i in f:
        post = read_post.read_post(i)
        if post["subreddit"] in top25:
            out.write(i)
        index += 1
        if index % 10000 == 0:
            print(index)
if __name__ == "__main__":
    trim()
