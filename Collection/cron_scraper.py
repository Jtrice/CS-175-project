import rget
import time
import json

def log(post):
    logfile = open("log.txt",'a')
    logfile.write(post)
    logfile.close()
    
def get_var():
    var = open("var.txt","r")
    exclude_new_ids = var.readline().split()
    exclude_top_25 = var.readline().split()
    var.close()
    if len(exclude_new_ids) > 1 and exclude_new_ids[0] != '':
        return (exclude_new_ids[:-1],exclude_top_25)
    else:
        return ([],[])

def set_var(exclude_new_ids,exclude_top_25):
    var = open("var.txt","w")
    var.write("\t".join(exclude_new_ids))
    var.write("\n")
    var.write("\t".join(exclude_top_25))
    var.close()

def scrape(user_agent="example"):
    exclude_new_ids,exclude_top_25 = get_var()
    batch_time = time.time()
    #ALL
    post_ids = rget.get_new("all",tab="new",num_posts=2000,
                            exclude_ids=exclude_new_ids,user_agent=user_agent,
                            out_file="NewCorpus.txt",stop_if_exclude=True,
                            dict_to_merge={"batch_time":batch_time})
    exclude_new_ids = (post_ids+exclude_new_ids)[:10]
    log("Front {}/2000 \t".format(len(post_ids)))
    #Front
    post_ids = rget.get_new("front",num_posts=25,
                            exclude_ids=exclude_top_25,user_agent=user_agent,
                            out_file="Top25.txt",stop_if_exclude=False,
                            dict_to_merge={"batch_time":batch_time})
    exclude_top_25 = exclude_top_25 + post_ids
    log("all/hot {}/25 \t".format(len(post_ids)))
    set_var(exclude_new_ids,exclude_top_25)
    #Rising
    post_ids = rget.get_new("all",tab="rising",num_posts=10,
                            exclude_ids=[],user_agent=user_agent,
                            out_file="Rising10.txt",stop_if_exclude=False,
                            dict_to_merge={"batch_time":batch_time})
    log("all/rising {}/10 \n".format(len(post_ids)))

if __name__ == "__main__":
    user_agent="testing praw script for finding hot posts""by Taylor Rogers"
    while True:
        scrape(user_agent=user_agent)
        print(time.time())
        time.sleep(300)
