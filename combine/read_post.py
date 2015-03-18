import ast

def read_post(line):
    """Creates a dictionary from a string converted reddit post """
    line = line.replace("\\\\',","$b*$b*',") #I did this for one post.   
    line = line.replace("\\'","$q*") #replaces \' with $q ex can't becomes can$q*t
    line = line.replace("\\",'$b*')  #replaces remaining backslashes with $
    line = line.replace('<',"'").replace('>',"'")
    line = line.replace("Subreddit(subreddit_name='","('")
    line = line.replace("Redditor(user_name='","('")
    dict = {}
    for k,v in ast.literal_eval(line).items():
        #Reverts the data damage
        if type(k) is str: k = k.replace('$q*',"'").replace('$b*','\\')
        if type(v) is str: v = v.replace('$q*',"'").replace('$b*','\\')
        dict[k] = v
    return dict
    
if __name__ == '__main__':
    file_name = "Data/NewCorpus.txt"
    f = open(file_name)
    line = f.readline()
    while line:
        dictionary = read_post(line)
        line = f.readline()
        print(dictionary['title'][:50])
    print('done')
