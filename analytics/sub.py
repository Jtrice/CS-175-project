import matplotlib.pyplot as plt
import numpy as np
import read_post
import operator

def runningMean(x, N):
    return np.convolve(x, np.ones((N,))/N)[(N-1):][:(1-N)]
    
def analysis(file_name):
    incr = 1/12  #every five minutes in hour
    midnight1 = 1424246400 #midnight Tuesday Night
    midnight2 = 1424419200 #midnight Thursday Night
    f = open(file_name)
    number_posts = 0
    everything = {}
    subreddit_num_posts = {}
    index = {}
    times = {}
    for i in f:
        post = read_post.read_post(i)
        bt = post['batch_time']
        sub_id = post['subreddit_id']
        sub_name = post['subreddit']
        if bt <= midnight1 or bt >= midnight2:
            continue
        number_posts += 1
        if number_posts % 50000 == 0: 
            print(number_posts);
        if sub_id not in times.keys(): times[sub_id] = {}
        if bt not in times[sub_id].keys(): times[sub_id][bt] = 0
        times[sub_id][bt] += 1
        if bt not in everything.keys(): everything[bt] = 0
        everything[bt] += 1

        if sub_id not in index.keys(): index[sub_id] = sub_name
        elif index[sub_id] != sub_name: print("DUPLACTE")
        if sub_id not in subreddit_num_posts.keys(): subreddit_num_posts[sub_id] = 0
        subreddit_num_posts[sub_id] += 1

    #Create Plotable lists
    batchtime = [(i-midnight1)/3600 for i, j in sorted(everything.items())]
    allposts = {}
    for sub_id in times.keys():
        if sub_id not in allposts: allposts[sub_id] = []
        for bt in everything.keys():
            if bt not in times[sub_id].keys():
                allposts[sub_id].append(0)
            else:
                allposts[sub_id].append(times[sub_id][bt])

    #print
    traffic = 0
    for i,j in [(i,j) for i,j in sorted(subreddit_num_posts.items(),key=operator.itemgetter(1), reverse=True)][:100]:
        print(index[i]+' (' + str(j) + ')')
        traffic += j
    print(traffic)

    for i,j in [(i,j) for i,j in sorted(subreddit_num_posts.items(),key=operator.itemgetter(1), reverse=True)][:7]:
        sub_posts = allposts[i]
        wbatchtime = batchtime[1:]
        wposts = [((i-j)/incr)*k for i,j,k in zip(batchtime[1:],batchtime,sub_posts[1:])]

        plt.figure(1)
        plt.plot(wbatchtime[35:-25],runningMean(wposts[10:],51),label=(index[i]+' ('+str(j)+')'))
        #plt.plot(wbatchtime,wposts) 
        plt.title("Subreddits")
        plt.xlabel('Hours (5 minute increment)')
        plt.ylabel('Num of Posts')
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.show()
    print(number_posts)
    print()

if __name__ == "__main__":
    analysis("Data/NewCorpus.txt")
