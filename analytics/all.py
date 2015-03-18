import matplotlib.pyplot as plt
import numpy as np
import read_post

def runningMean(x, N):
    return np.convolve(x, np.ones((N,))/N)[(N-1):][:(1-N)]
    
def analysis(file_name):
    incr = 1/12  #every five minutes in hour
    midnight1 = 1424246400 #midnight Tuesday Night
    midnight2 = 1424419200 #midnight Thursday Night
    f = open(file_name)
    number_posts = 0
    times = {}
    for i in f:
        post = read_post.read_post(i)
        pt = post['batch_time']
        if pt <= midnight1 or pt >= midnight2:
            continue
        number_posts += 1
        if number_posts % 50000 == 0: 
            print(number_posts);
        if pt not in times.keys(): times[pt] = 0
        times[pt] += 1
    print(number_posts)
    batchtime = [(i-midnight1)/3600 for i, j in sorted(times.items())]
    allposts = [j for i, j in sorted(times.items())]
    wbatchtime = batchtime[1:]
    wposts = [((i-j)/incr)*k for i,j,k in zip(batchtime[1:],batchtime,allposts[1:])]

    plt.figure(1)
    #plt.plot(wbatchtime[35:-25],runningMean(wposts[10:],51))
    plt.plot(wbatchtime[10:],wposts[10:]) 
    plt.title("All Traffic (Moving Avg)")
    plt.xlabel('Hours (5 minute increment)')
    plt.ylabel('Num of Posts')
    plt.show()
if __name__ == "__main__":
    analysis("Data/NewCorpus.txt")
