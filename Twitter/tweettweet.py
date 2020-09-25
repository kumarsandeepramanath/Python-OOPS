import tweepy
auth = tweepy.OAuthHandler('JxR9EVjNzvMNlCL4b8iG5bdkC','DppTBQhC55R9O1eJd6XcXO6Uzy8zRR8LqqGSUZAAtuodI5QcDm')
auth.set_access_token('1309470949280944128-BRBUOe3xTtp84UMjComkfUjpqvToeF', 'hMAAmkXhR18mBMgQbgAORbALAafL0XWfNXY29nYY5tOLi')

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

print(api.me().name)
print(api.me().screen_name)
print(api.me().followers_count)


search_string = 'python'
number_of_tweets = 2

for tweet in tweepy.Cursor(api.search,search_string).items(number_of_tweets):
    try :
        tweet.favorite()
        print('I liked that tweet')

    except tweepy.TweepError as er:
        print('In except block')
        print(er.reason)
    except StopIteration:
        break
