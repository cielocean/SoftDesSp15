""" Exploring learning curves for classification of handwritten digits """

import matplotlib.pyplot as plt
import numpy
from sklearn.datasets import *
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression


data = load_digits()
print data.DESCR
num_trials = 500
train_percentages = range(5,95,5)
test_accuracies = numpy.zeros(len(train_percentages))

# train a model with training percentages between 5 and 90 (see train_percentages) and evaluate
# the resultant accuracy.
# You should repeat each training percentage num_trials times to smooth out variability
# for consistency with the previous example use model = LogisticRegression(C=10**-10) for your learner
for i in range(num_trials):

	for j in range(len(train_percentages)):
		X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, train_size=train_percentages[j]/100.0)
		model = LogisticRegression(C=10**-10)
		model.fit(X_train, y_train)
		test_accuracies[j] += model.score(X_train,y_train)

test_accuracies = test_accuracies/num_trials

fig = plt.figure()
plt.plot(train_percentages, test_accuracies)
plt.xlabel('Percentage of Data Used for Training')
plt.ylabel('Accuracy on Test Set')
plt.show()

# """Load and display 10 of the examples"""
# digits = load_digits()
# print digits.DESCR
# fig = plt.figure()
# for i in range(10):
#     subplot = fig.add_subplot(5,2,i+1)
#     subplot.matshow(numpy.reshape(digits.data[i],(8,8)),cmap='gray')

# plt.show()

# """Multinomial Logistic Regression"""
# """
# Training set is used to train the classifier
# Testing set is used to evaluate the classifer on data it has not been trained on
# """

# data = load_digits()
# X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, train_size=0.5)
# model = LogisticRegression(C=10**-10)
# model.fit(X_train, y_train)
# print "Train accuracy %f" %model.score(X_train,y_train)
# print "Test accuracy %f"%model.score(X_test,y_test)