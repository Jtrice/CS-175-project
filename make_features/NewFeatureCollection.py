import ast

class post:
	#FrontPageID is a list of the front page ID's
	#need to run a script to get the frontPage Id's in a list
	#and then initialize each post as a post(dictionary,FrontPageID's)
	def __init__(self, data,FrontPageID):
	#features all put into the private variable
		self.id = data['id']
		self.title = data['title']
		self.num_comments = data['num_comments']
		self.gilded = data['gilded']
		self.upvotes = data['ups']
		self.author = data['author']
		self.subreddit = data['subreddit']
		## time the post is created
		self.created = data['created']
		self.batch_time = data['batch_time']
		#front page status
		self.front_page = False
		for i in range(len(FrontPageID)):
			if (self.id == FrontPageID[i]):
				self.front_page = True


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
	#this gets the front page id's and puts them into a list
	FrontPageIDS = []
	#frontPage = open("Data/top25.txt", "r", encoding="utf-8")
	frontPage = open("top25.txt", "r", encoding="utf-8")
	fline = frontPage.readline()
	while fline:
		dictionary = read_post(fline)
		#add the id's into a list of Id's
		FrontPageIDS.append(dictionary['id'])
		fline = frontPage.readline()
	print('Front Page done')
	frontPage.close()
	
	#this makes a post object 
	
	#f = open("Data/NewCorpus.txt", "r", encoding="utf-8")
	f = open("NewCorpus.txt", "r", encoding="utf-8")
	line = f.readline()
	POSTS = []
	while line:
		dictionary = read_post(line)
		#makes the post here and appends them into a list of posts
		POSTS.append(post(dictionary,FrontPageIDS))
		line = f.readline()
		#print(dictionary['title'][:50])
	print('done')
	f.close()