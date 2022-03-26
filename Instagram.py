from SocialMedia import SocialMedia

class Instagram(SocialMedia):
	def __init__(self, name):
		super().__init__(name)
		self.posts = []

	def getPosts(self):
		return self.posts

	def publishNewPost(self,body):
		if(len(body) <= 2200):
			self.posts.append(body)
			return True
		else:
			return False


print("Enter User Name :")
userName = input()

instagram = Instagram(name = userName)
print("User Name is : " + instagram.getName())

print("Enter post body(must be less than 2200 characters.) :")
postBody = input()

if instagram.publishNewPost(body = postBody):
	print(instagram.getPosts())
	print("Post is Added")
else:
	print("Post is not Added")
