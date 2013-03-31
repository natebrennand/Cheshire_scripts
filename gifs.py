

from credentials import username
import praw
from sys import argv

scrape = praw.Reddit(user_agent="imgur photo scraper by {}".format(username))
submissions = scrape.get_subreddit('gifs').get_top(limit = 50)

for y in submissions:
	print str(y.url),
