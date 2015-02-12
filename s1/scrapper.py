import rget
import time

def scrape(starttime=None, endtime=None, delay=60*2, user_agent="example"):
    if starttime==None: starttime = time.time()
    if endtime==None: endtime=starttime+(86400*2)
    now = time.time()
    if starttime > now: 
        print("Waiting till {} since epoch".format(starttime))
        time.sleep(starttime - now)

    logfile = open("log.txt",'wt')
    exclude_new_ids = []
    exclude_top_25 = []
    while(time.time() < endtime):
        print("Working ...")
        if time.time() < (endtime+starttime)/2:
            batch_time = time.time()
            post_ids = rget.get_new("all",tab="new",num_posts=500,
                                    exclude_ids=exclude_new_ids,user_agent=user_agent,
                                    out_file="NewCorpus.txt",stop_if_exclude=True,
                                    dict_to_merge={"batch_time":batch_time})
            exclude_new_ids = post_ids[:10]
            print("Found {}/500 new posts in all/new".format(len(post_ids)))
            logfile.write("all/new {} / 500 \n".format(len(post_ids)))

        post_ids = rget.get_new("front",num_posts=25,
                                exclude_ids=exclude_top_25,user_agent=user_agent,
                                out_file="Top25.txt",stop_if_exclude=False,
                                dict_to_merge={"batch_time":batch_time})
        exclude_top_25 = exclude_top_25 + post_ids
        print("Found {}/25 new posts in all/hot".format(len(post_ids)))
        logfile.write("all/hot {} / 25 \n".format(len(post_ids)))

        post_ids = rget.get_new("all",tab="rising",num_posts=10,
                                exclude_ids=[],user_agent=user_agent,
                                out_file="Rising10.txt",stop_if_exclude=False,
                                dict_to_merge={"batch_time":batch_time})
        print("Sleeping ...")
        time.sleep(delay)
    logfile.close()

if __name__ == "__main__":
    user_agent="testing praw script for finding hot posts""by Taylor Rogers"
    #Feb 11
    midnight_epoch = 1423814400
    scrape(starttime=midnight_epoch)

