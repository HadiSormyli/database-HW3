from SocialMedia import SocialMedia

class Twitter(SocialMedia):
	def __init__(self, name):
		super().__init__(name)	
		self.tweets = []


	def getTweets(self):
		return self.tweets

	def createNewTweet(self,body):
		if(len(body) <= 280):
			self.tweets.append(body)
			return True
		else :
			return False
		

print("Enter User name :")
userName = input()

twitter = Twitter(name = userName)
print("User Name is : " + twitter.getName())

print("Enter tweet body(must be less than 280 characters) : ")
tweetBody = input()

if twitter.createNewTweet(body = tweetBody):
	print("Tweet is Added")
	print(twitter.getTweets())
else:
	print("Tweet is not Added")