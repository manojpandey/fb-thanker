import requests
import time
import random

base_url = 'https://graph.facebook.com/v2.3/'

# token = 'CAACEdEose0cBABIQfdrh2RjoHnLZByf7NcEsWADZAyArUQPlxmyhDQ46jrxMNnG5bmnExhqHdtpMEZA8lNDdtPQV1YlrLPm1fjJnDIYBDNCQISLgfaw3jsFgvuYsUMIH6e1qVZACZBkkMYMfGwnDnSfzSURwZACSR7vqdTSZCf8ITBkYfNemLUO51J82qfFfO96QolIL9JgysFMpUEQD8ZB2' #oauth access token
token = ' <access token> '

time_since = "" # unix time (starting)
time_until = "" # unix time (end)
post_limit =  # total number of posts (optional)

sample_messages = ["Thank you so much, ", "Thanks for the wishes, ", "Thank you, "]

def like_post(idz, name):
    print "Liking the post by " + name
    requests.post(base_url + idz + "/likes", params = {'access_token': token})

def comment_post(idz, msg, name):
    print "Commenting on the post by " + name 
    requests.post(base_url + idz + "/comments", params = {'access_token': token, 'message' : msg})

def main():

    temp = "me/feed?since=" +  time_since + "&until=" + time_until + "&limit=" + str(post_limit)
    response = requests.get(base_url + temp, params = {'access_token': token})
    flag = True
    count = 0
    while flag:
        jsonData = response.json()
        allPosts = jsonData["data"] 

        for post in allPosts:
            count += 1
            name = post["from"]["name"]
            name = name.split(' ')[0]
            sender_id = post["from"]["id"]
            post_id = post["id"]
            comment = random.choice(sample_messages) + name + " :)"
            print "posted by: " + name
            if count > post_limit:
                flag = False
                break
            # sending post requests
            like_post(post_id, name)
            comment_post(post_id, comment, name)

    print "Liked and wished thanks on " + str(count-1) + " posts ! :D"

if __name__ == '__main__':
    main()