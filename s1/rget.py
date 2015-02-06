"""
Project: Reddit Scrapper
Author: Taylor Rogers
Date: 2/5/2015
"""
import praw
import time

def get_new(subreddit,
            tab=None,
            num_posts=25,
            exclude_ids=[],
            user_agent="example",
            out_file="corpus.txt",
            stop_if_exclude=False,
            dict_to_merge={}):

    """Searches,loads,and writes out a # of reddit posts from subreddit/tab.
    Then it returns a list of all posts """
    outfile = open(out_file,'a')
    reddit = praw.Reddit(user_agent=user_agent)
    sub = reddit.get_subreddit(subreddit)
    if not(tab) or tab == "hot": gen = sub.get_hot(limit=num_posts)
    elif tab == "new": gen = sub.get_new(limit=num_posts)
    elif tab == "rising": gen = sub.get_rising(limit=num_posts)
    elif tab == "controversial": gen = sub.get_controversial(limit=num_posts)
    elif tab == "top": gen = sub.get_top(limit=num_posts)
    else: raise ValueError("tab must be equal to hot, new, rising, controversial, top, or be None")
    ids = []
    for i in gen:
        if i.id not in exclude_ids:
            tempdict = vars(i); tempdict.update(dict_to_merge)
            outfile.write(str(tempdict)+"\n")
            ids.append(i.id)
        elif stop_if_exclude:
            break
    outfile.close()
    return ids

if __name__ == "__main__":
    user_agent="testing""by Person"
    print(get_new("all",tab="new",user_agent=user_agent))
