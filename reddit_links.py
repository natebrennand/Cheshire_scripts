
from credentials import username
import praw
from sys import argv

if len(argv) != 3:
	print 'usuage:\n\tpython reddit_links <subreddit> <# of links>'
	exit(1)

scrape = praw.Reddit(user_agent="imgur photo scraper by {}".format(username))
submissions = scrape.get_subreddit(str(argv[1])).get_top(limit = int(argv[2]))

filename = str(argv[1]+'_'+argv[2]+'.applescript')
with open(filename,'w+') as f:
	f.write('open ')
	for y in submissions:
		f.write( str(y.url) + ' ')
	f.write('\n')	

