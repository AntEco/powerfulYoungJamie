from urllib.parse import quote_plus

import praw

JOESCOMMANDS = ["pull that shit up jamie", "jamie pull that up", "pull that up jamie"]
REPLY_TEMPLATE = '[Let me google that for you](http://lmgtfy.com/?q={})'

def main():
    reddit = praw.Reddit(user_agent='JreBot v0.1',
        client_id='AiQKE4vZ4T831w',
        client_secret='hDsRBZyZU5AL4y0EfmqG7qFdJqs',
        username='PowerfulYoungJamie',
        password='The Joe Rogan')

    subreddit = reddit.subreddit("RedditDiamond")
    for submission in subreddit.stream.submissions():
    	process_submission(submission)


def process_submission(submission):

    if len(submission.title.split()) > 10:
            return
        
    normalized_title = submission.title.lower()
    for questionPhrase in JOESCOMMANDS:
        if questionPhrase in normalized_title:
            url_title = quote_plus(submission.title)
            reply_text = REPLY_TEMPLATE.format(url_title)
            print('Replying to: {}'.format(submission.title))
            submission.reply(reply_text)
            break

if __name__ == '__main__':
    main()
