import yaml

class post:
	#frontPageID is a list of strings that are the front page ID's
	#need to run a script to get the frontPage Id's in a list
	#and then initialize each post as a post(line.readline(),FrontPageID's)
	def __init__(self, data,FrontPageID):
	#features all put into the private variable
		info = yaml.load(data)
		self.id = info['id']
		self.title = info['title']
		self.num_comments = info['num_comments']
		self.gilded = info['gilded']
		self.upvotes = info['ups']
		self.author = info['author']
		self.subreddit = info['subreddit']
		## time the post is created
		self.created = info['created']
		self.batch_time = info['batch_time']
		#front page status
		self.front_page = False
		for i in range(len(FrontPageID)):
			if (self.id == FrontPageID[i]):
				self.front_page = True
	#these technically aren't necessary you could access these with post.id instead of post.get_id()
	#python is very lax
	#def get_id(self):
	#	return self.id
	#def get_title(self):
	#	return self.title
	#def get_num_comments(self):
	#	return self.num_comments
	
front_Page_IDS = []
	
frontPage = open('NewCorpus.txt')

line = frontPage.readline()
while(line):
	s = yaml.load(line)
	print(s['id'])
#	print(0)
	line = frontPage.readline()
frontPage.close()

def p():
	line = frontPage.readline()


#s = yaml.load(f_line)

#front_Page_IDS.append(s['id'])

#while(line):
#	s = line.split(', ')
#	print(len(s))
#	line = f.readline()

#
#s = post(line)


	

