"""
Downloading Ebook from gutenberg
http://www.gutenberg.org/
"""

from pattern.web import *
"""
oliver_twist_full_text = URL('http://www.gutenberg.org/ebooks/730.txt.utf-8').download()
oliver_twist = open('oliver_twist.txt','w')
oliver_twist.write(oliver_twist_full_text)
"""

emma_full_text = URL('http://www.gutenberg.org/files/158/158.txt').download()
emma = open('emma.txt','w')
emma.write(emma_full_text)