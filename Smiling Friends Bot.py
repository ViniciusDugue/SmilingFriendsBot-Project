'''
    old bot
    user_agent="<console:Smiling:1.0>",
    client_id="RZTiClG0PcB0DWUY06dj8g",
    client_secret="BTQgFQ3McPhvrujs0NEGqWtAyBerPA",
    username="SmilingFriendsBot",
    password="dwbehappy"
'''
import praw
import random
'''PIL is pillows, which allows us to edit and add text to a gif'''
'''python reddit API Wrapper- a python package that allows for accesssing reddits API(application programming interface)
'''
reddit = praw.Reddit(   #these are parameters that we need to run the Reddit bot
    user_agent="<console:Smiling:1.0>",
    client_id="zsBwv6UL6TxKO4aybk7kfA",
    client_secret="7MCGw8mNjNRzNJaZWjHoYrRiyMOHtw",
    username="smilingtestbot",
    password="dwbehappy"
)
# communities that need happiness sounding, programming, college, smiling friends, showerthoughts
subreddit = reddit.subreddit("SmilingFriends")

smiling_memes = ['https://www.youtube.com/watch?v=L3HQMbQAWRc&ab_channel=sk8r123sk8r', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ']
for submission in subreddit.new(limit=5):
    print(submission.title)
    for comment in submission.comments:
        if hasattr(comment,"body"):
            comment_lowercase =comment.body.lower()
            if " sad " in comment_lowercase:
                redditor1 = comment.author
                print("----------")
                print(f'{comment.body}: {redditor1.name}') # prints comment body and author name
                random_index = random.randint(0, len(smiling_memes)-1)
                comment.reply(f'Heres something to brighten up your day :) {smiling_memes[random_index]}')
                #comment doesnt print actual comment, prints the comment object data. use comment.body