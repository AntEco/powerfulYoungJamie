import praw

reddit = praw.Reddit(user_agent='JREsmoove v0.1',
client_id='DjnggMIzZFtkRQ',
client_secret='noCULv4ERlbodrfykF7PKCXodN4',
username='smoove',
password='Three-333')

subreddit = reddit.subreddit("RedditDiamond")

for submission in subreddit.hot(limit=10):
    print(submission.title)