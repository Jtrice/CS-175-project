import ast
import re
import collections
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from time import time
from nltk.corpus import stopwords

class post:
	#FrontPageID is a list of the front page ID's
	#need to run a script to get the frontPage Id's in a list
	#and then initialize each post as a post(dictionary,FrontPageID's)
	def __init__(self, data,FrontPageID):
	#features all put into the private variable
		self.id = data['id']
		self.title = data['title']
		self.title_weights = 0
		self.num_comments = data['num_comments']
		self.gilded = data['gilded']
		self.upvotes = data['ups']
		self.author = data['author']
		self.subreddit = data['subreddit']
		## time the post is created
		self.created = data['created']
		self.batch_time = data['batch_time']
		#front page status
		self.front_page = 0
		for i in range(len(FrontPageID)):
			if (self.id == FrontPageID[i]):
				self.front_page = 1
					
	def title_feature_score(self,score):
		self.title_weights = score
		



			###Features : Subreddits, content, bag of words from title, 	


				
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
	
	t0 = time()
	
	frontPage = open("top25.txt", "r", encoding="utf-8")
	fline = frontPage.readline()
	
	FSUBREDDITS = []
	FTOPWORDS = []
	FrontPageDict = {}
	while fline:
		dictionary = read_post(fline)
		#add the id's into a list of Id's
		FrontPageIDS.append(dictionary['id'])
		FSUBREDDITS.append(dictionary['subreddit'])
		FTOPWORDS.append(dictionary['title'])
		
		
		
		fline = frontPage.readline()
	frontPage.close()
	print('Front Page done')
	
	print("done in %0.3fs" % (time() - t0))
	
	
	
	
	FEATURES = collections.Counter(FSUBREDDITS).most_common(29)
	
	
	FTOPWORDS = (" ").join(FTOPWORDS)
	FALL = re.findall(r'\w+', FTOPWORDS)
	filtered_words = []
	stops = stopwords.words('english')
	
	for w in FALL:
		if w.lower() not in stops:
			filtered_words.append(w)
            

	BAGOFWORDS = collections.Counter(filtered_words).most_common(30)
	
	t1 = time()
	
	#this makes a post objects
	f = open("NewCorpus.txt", "r", encoding="utf-8")
	line = f.readline()
	POSTS = []
	Titles = [] #used to get title weights
	
	while line:
		dictionary = read_post(line)
		Titles.append(dictionary['title'])
		POSTS.append(post(dictionary,FrontPageIDS))
		line = f.readline()
		
	f.close()
	
	
	#getting weights for the titles
	vectorizer = TfidfVectorizer(min_df=1)
	Title_matrix = vectorizer.fit_transform(Titles)
	
	LINE1 = ['TFID_VALUE']
	for i in range(len(FEATURES)):
		LINE1.append(FEATURES[i][0])
	LINE1.append('OTHER')
	
	for i in range(len(BAGOFWORDS)):
		LINE1.append(BAGOFWORDS[i][0])
	LINE1.append('MADE FRONTPAGE')
	
	print("NOW CSV in %0.3fs" % (time() - t0))
	print(len(POSTS))
	
	with open('data.csv', 'w') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',')
		spamwriter.writerow(LINE1)
		for i in range(len(POSTS)):
			OUTPUT = []
			Score = float(sum(Title_matrix.sum(1)[i]))
			OUTPUT.append(Score)
		
			c = 1
		#	POSTS[i].title_feature_score(Score)
			for j in range(len(FEATURES)):
				if (POSTS[i].subreddit == FEATURES[j][0]):
					c = 0
					OUTPUT.append(1)
					#print(POSTS[i].subreddit)
				else:
					OUTPUT.append(0)
			OUTPUT.append(c)
			for j in range(len(BAGOFWORDS)):
				if(BAGOFWORDS[j][0] in POSTS[i].title):
					OUTPUT.append(1)
				else:
					OUTPUT.append(0)
			OUTPUT.append(POSTS[i].front_page)
			if(POSTS[i].front_page == 1):
				print(i)
			spamwriter.writerow(OUTPUT)
			
			
			
	
		
		
	print('full posts')
	print("done in %0.3fs" % (time() - t1))
	
	