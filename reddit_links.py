
# usuage: python reddit_links <subreddit> <# of links>

from credentials import username
import praw
from sys import argv

if len(argv) == 3:
	subreddit = str(argv[1])
	num_links = int(argv[2])
else:
	subreddit = 'aww'
	num_links = 25

scrape = praw.Reddit(user_agent="imgur photo scraper by {}".format(username))
submissions = scrape.get_subreddit(subreddit).get_top(limit = num_links)

filename = str(subreddit+'_'+str(num_links)+'.applescript')
with open(filename,'w+') as f:
	f.write('open ')
	for y in submissions:
		f.write( str(y.url) + ' ')
	f.write('\n')	

