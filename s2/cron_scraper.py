import rget
import time
import json

def scrape(user_agent="example"):
    logfile = open("log.txt",'a')
    var = open("var.txt","r+")
    x = json.load(var)
    exclude_new_ids = x[0]
    exclude_top_25 = x[1]
    if exclude_top_25 == ['']: exclude_top_25 = []
    var.seek(0); var.truncate()

    batch_time = time.time()
    post_ids = rget.get_new("all",tab="new",num_posts=500,
                            exclude_ids=exclude_new_ids,user_agent=user_agent,
                            out_file="NewCorpus.txt",stop_if_exclude=True,
                            dict_to_merge={"batch_time":batch_time})
    exclude_new_ids = (post_ids+exclude_new_ids)[:10]
    logfile.write("all/new {} / 500 \n".format(len(post_ids)))
    
    post_ids = rget.get_new("all",tab="hot",num_posts=25,
                            exclude_ids=exclude_top_25,user_agent=user_agent,
                            out_file="Top25.txt",stop_if_exclude=False,
                            dict_to_merge={"batch_time":batch_time})
    exclude_top_25 = exclude_top_25 + post_ids
    logfile.write("all/hot {} / 25 \n".format(len(post_ids)))
    json.dump([exclude_new_ids,exclude_top_25],var)
    var.close()
    logfile.close()

if __name__ == "__main__":
    user_agent="testing praw script for finding hot posts""by Taylor Rogers"
    scrape()
