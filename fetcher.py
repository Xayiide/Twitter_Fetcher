from twython import Twython

API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET = "", "", "", ""

with open('keys', 'r') as f:
    API_KEY = f.readline().strip('\n')
    API_SECRET = f.readline().strip('\n')
    ACCESS_TOKEN = f.readline().strip('\n')
    ACCESS_TOKEN_SECRET = f.readline().strip('\n')

twitter = Twython(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
twitter.verify_credentials()
# print(dir(twitter))


def input_name():
    user = str(input("User to stalk: "))
    if user[0] != '@':
        user = '@' + user
    return user


def retrieve_user_tweets():
    user = input_name()
    print(user)
    amount = int(input("Amount of tweets: "))
    print(amount)
    timeline = twitter.get_user_timeline(screen_name=user)
    num = min(len(timeline), amount)
    for i in range(num):
        print("\n")
        print("Time: " + timeline[i]['created_at'])
        print("Text: " + timeline[i]['text'])
        print("Favs: " + str(timeline[i]['favorite_count']) + " Rts: " + str(timeline[i]['retweet_count']))
        print("Place: " + str(timeline[i]['geo']))
        urls = timeline[i]['entities']['urls']
        hashtags = timeline[i]['entities']['hashtags']
        mentions = timeline[i]['entities']['user_mentions']
        print("Containing: " + str(urls) + str(hashtags) + str(mentions))



def retrieve_user_info():
    user = input_name()
    timeline = twitter.get_user_timeline(screen_name=user)
    print("\n\n")    
    short = timeline[0]['user'] 
    print("Name: " + short['name'])
    print("Following: " + str(short['friends_count']))
    print("Followers: " + str(short['followers_count']))
    print("Tweets: " + str(short['statuses_count']))
    print("UID: " + str(short['id']))
    print("Favs: " + str(short['favourites_count']))
    print("Bio: " +  short['description'])
    print("Url: " + short['url'])
    print("Location: " + short['location'])
    print("Since: " + short['created_at'])





def menu():
    ans = True
    while ans:
        print("\n\n")
        print("1: Retrieve user's tweets")
        print("2: Get user's info")
        print("3: Get user's statistics")
        print("4: Get bot's info")
        print(" 0: Exit")
        ans = input("> ")

        if ans == '1':
            print("Retrieve!")
            retrieve_user_tweets()
        elif ans == '2':
            print("Info!")
            retrieve_user_info()
        elif ans == '3':
            print("Statistics!")
        elif ans == '4':
            print("Bots!")
        elif ans == '0':
            ans = False
            print("Bye!")
        else:
            print("Not a valid choice!")



menu()
