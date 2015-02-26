from pattern.web import *

"""Google"""
"""
g = Google()

for result in g.search('Olin College'):
    print result.url
    #link = URL().download()
    #print result.text #in HTML
    print plaintext(result.txt) #not in HTML
"""


"""Wikipedia"""
"""
w = Wikipedia()

for article_title in w.index():
    print article_title

olin_article = w.search('Olin College')
print olin_article.sections
"""


"""Twitter"""
"""
s = Twitter().stream('#fail')

for i in range(10):
    time.sleep(1)
    s.update(bytes=1024)
    print s[-1].text if s else ''

#check current trending topic
from pattern.web import *
print Twitter().trends()
"""


"""Facebook"""
"""
f = Facebook(license='CAAE...')

me = f.profile()
print me 
# >>> (u'100004596638210', u'Kim Jee Hyun', u'08/13/1994', u'f', u'en_US', 0)
my_friends=f.search(me[0], type=FRIENDS, count=10000) #number of friends
for friend in my_friends:
    friend_news = f.search(friend.id, type=NEWS, count=10000)
    for news in friend_news:
        print news.text
        print news.author
"""
