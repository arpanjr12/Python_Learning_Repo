#Write a program to find out whether a given post is talking about “Harry” or not


enter_post=input("enter your post: ")


# if("Harry","harry" in enter_post):
#     print("yes ! this post is talking about harry")

if("Harry".lower() in enter_post.lower()):
    print("yes ! this post is talking about harry")

else:
    print("this post is not talking about harry")