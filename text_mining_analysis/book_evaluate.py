"""
Evaluate the change in sentiment of each chapter of the book
"""

from pattern.en import*
import re
import matplotlib.pyplot as plt

emma = open('emma.txt','r')
sns = open('sense_and_sensibility.txt','r')
ot = open('oliver_twist.txt','r')
je = open('jane_eyre.txt','r')



def format_text(text):
	"""
	input text file with type file
	return list of chapters of list of sentences
	"""
	def file2str(file):
		"""
		input text file with type file
		convert text file to str
		return text file with type str
		"""
		strfile=file.read()
		return strfile

	#def lowercase(text):
	#	return text.lower()

	def split_chapter(text):
		return text.split('CHAPTER')

	def get_sentences(text):
		"""
		input a text file in str
		convert text (str) to list
		return list of sentences (str)
		"""
		return re.split(r'\s*[!?.]\s*',text)

	def rm_n(L):
		"""
		input list of sentences
		remove \n from sentences in a list
		return list of sentences without \n
		"""
		newL=[]
		for string in L:
			newL.append(string.replace('\n',' ').replace('\r',' '))
		return newL

	formatted_text=[]
	#for chapter in split_chapter(lowercase(file2str(text))):
	#	formatted_text.append(rm_n(get_sentences(chapter)))
	for chapter in split_chapter(file2str(text)):
		formatted_text.append(rm_n(get_sentences(chapter)))

	return formatted_text

def sentiment_lvls(L):
	"""
	Input list of sentences
	Return list of sentiment levels
	"""
	def sentiment_lvl_1(sentence):
		"""
		input 1 sentence (str)
		evaluate sentiment level
		return (positive sentiment polarity, subjectivity of sentence) of the sentence
		"""
		return sentiment(sentence)

	L_sentiment=[]
	L_sentiment_chp=[]
	for chapter in L:
		for sentence in chapter:
			L_sentiment_chp.append(sentiment_lvl_1(sentence))
		L_sentiment.append(L_sentiment_chp)
	return L_sentiment

def filter(L):
	"""
	remove list element with subjectivity of sentence=0
	return new list
	"""
	L_sentiment=[]
	L_sentiment_chp=[]
	for chp in L:
		for sentimentlvl in chp:
			if sentimentlvl[1]!=0:
				L_sentiment_chp.append(sentimentlvl[0])
		avg_sentiment=float(sum(L_sentiment_chp))/len(L_sentiment_chp) #average sentiment value for each chapter
		L_sentiment.append(avg_sentiment)
	return L_sentiment #List

def plot(L):
	"""
	input list of values
	plot graph values
	"""

	x=filter(L)
	plt.xlabel('Chapter')
	plt.ylabel('Sentiment Level')

	plt.plot(list(range(len(x))),x)
	plt.show()

plot(sentiment_lvls(format_text(emma)))


