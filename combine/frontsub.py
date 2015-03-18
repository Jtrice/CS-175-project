import matplotlib.pyplot as plt
import numpy as np
import read_post
import operator
top25 = ['t5_2qh33', 't5_2qh0u', 't5_2qt55', 't5_2qqjc', 't5_2qh1o', 't5_2qh03', 't5_2qh1e', 't5_2qh13', 't5_2ti4h', 't5_2qh1i', 't5_2qh3l', 't5_2qzb6', 't5_2szyo', 't5_2qh3s', 't5_2to41', 't5_2qh55', 't5_mouw', 't5_2tycb', 't5_2sokd', 't5_2qnts', 't5_2tecy', 't5_2qh6e', 't5_2qh87', 't5_2qgzy', 't5_2t7no', 't5_2raed', 't5_2sbq3', 't5_2qh72', 't5_2qh4i', 't5_2s5oq', 't5_2u3ta', 't5_2qm4e', 't5_2qh1u', 't5_2ul7u', 't5_2qh7a', 't5_2qh7d', 't5_2rmfx', 't5_2qgzt', 't5_2qh53', 't5_2tk95', 't5_2qh49', 't5_2s3nb', 't5_2qhx4']
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
        if sub_id not in top25: continue
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
