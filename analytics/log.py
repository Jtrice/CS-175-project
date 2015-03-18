import matplotlib.pyplot as plt
import numpy as np

def runningMean(x, N):
    return np.convolve(x, np.ones((N,))/N)[(N-1):][:(1-N)]
    
def logs_per_hour():
    hours = 48
    f = open('log.txt')
    all = []
    front = []
    rising = []
    for i in f.readlines():
        subreddit = i.split('\t')
        all.append(int(subreddit[0].split(' ')[1].split('/')[0]))
        front.append(int(subreddit[1].split(' ')[1].split('/')[0]))
        rising.append(int(subreddit[2].split(' ')[1].split('/')[0]))
    xaxis = []; t = 0; 
    for x in range(len(all)): xaxis.append(t); t += hours/len(all)
    
    plt.figure(1)
    plt.plot(xaxis[7:-7],runningMean(all,15))
    plt.title("All Traffic (Moving Avg)")
    plt.xlabel('Hours (5 minute increment)')
    plt.ylabel('Num of Posts')
    
    plt.figure(2)
    plt.plot(xaxis[11:-10],runningMean(front[1:],21))
    plt.title("New Front Page Posts (Moving Avg)")
    plt.ylabel("Num of Posts")
    plt.xlabel('Hours (5 minute increment)')
    
    plt.show()

if __name__ == "__main__":
    logs_per_hour()
