[![](https://img.realpython.net/8899c4a6d15334a6b9f769e9f8bc0cf7)](https://srv.realpython.net/click/41686012779/?c=7309556696&p=29182759436&r=38754)

Machine Learning[¶](#machine-learning "Permalink to this headline")
===================================================================

![https://d33wubrfki0l68.cloudfront.net/e2de4e3466f5d5bd753ac42697153d6d01cddfeb/b41c7/_images/34018729885_002ced9b54_k_d.jpg](https://d33wubrfki0l68.cloudfront.net/e2de4e3466f5d5bd753ac42697153d6d01cddfeb/b41c7/_images/34018729885_002ced9b54_k_d.jpg)

Python has a vast number of libraries for data analysis, statistics, and Machine Learning itself, making it a language of choice for many data scientists.

Some widely used packages for Machine Learning and other data science applications are listed below.

SciPy Stack[¶](#scipy-stack "Permalink to this headline")
---------------------------------------------------------

The SciPy stack consists of a bunch of core helper packages used in data science for statistical analysis and visualising data. Because of its huge number of functionalities and ease of use, the Stack is considered a must-have for most data science applications.

The Stack consists of the following packages (link to documentation given):

1.  [NumPy](http://www.numpy.org/)
2.  [SciPy library](https://www.scipy.org/)
3.  [Matplotlib](http://matplotlib.org/)
4.  [IPython](https://ipython.org/)
5.  [pandas](http://pandas.pydata.org/)
6.  [Sympy](http://www.sympy.org/en/index.html)
7.  [nose](http://nose.readthedocs.io/en/latest/)

The stack also comes with Python bundled in, but has been excluded from the above list.

### Installation[¶](#installation "Permalink to this headline")

For installing the full stack, or individual packages, you can refer to the instructions given [here](https://www.scipy.org/install.html).

**NB:** [Anaconda](https://www.continuum.io/anaconda-overview) is highly preferred and recommended for installing and maintaining data science packages seamlessly.

scikit-learn[¶](#scikit-learn "Permalink to this headline")
-----------------------------------------------------------

Scikit is a free and open source machine learning library for Python. It offers off-the-shelf functions to implement many algorithms like linear regression, classifiers, SVMs, k-means, Neural Networks, etc. It also has a few sample datasets which can be directly used for training and testing.

Because of its speed, robustness, and ease of, it’s one of the most widely-used libraries for many Machine Learning applications.

### Installation[¶](#id1 "Permalink to this headline")

Through PyPI:

pip install \-U scikit\-learn

Through conda:

conda install scikit\-learn

scikit-learn also comes shipped with Anaconda (mentioned above). For more installation instructions, refer to [this link](http://scikit-learn.org/stable/install.html).

### Example[¶](#example "Permalink to this headline")

For this example, we train a simple classifier on the [Iris dataset](http://en.wikipedia.org/wiki/Iris_flower_data_set), which comes bundled in with scikit-learn.

The dataset takes four features of flowers: sepal length, sepal width, petal length, and petal width, and classifies them into three flower species (labels): setosa, versicolor, or virginica. The labels have been represented as numbers in the dataset: 0 (setosa), 1 (versicolor), and 2 (virginica).

We shuffle the Iris dataset and divide it into separate training and testing sets, keeping the last 10 data points for testing and rest for training. We then train the classifier on the training set and predict on the testing set.

from sklearn.datasets import load\_iris
from sklearn import tree
from sklearn.metrics import accuracy\_score
import numpy as np

#loading the iris dataset
iris \= load\_iris()

x \= iris.data #array of the data
y \= iris.target #array of labels (i.e answers) of each data entry

#getting label names i.e the three flower species
y\_names \= iris.target\_names

#taking random indices to split the dataset into train and test
test\_ids \= np.random.permutation(len(x))

#splitting data and labels into train and test
#keeping last 10 entries for testing, rest for training

x\_train \= x\[test\_ids\[:\-10\]\]
x\_test \= x\[test\_ids\[\-10:\]\]

y\_train \= y\[test\_ids\[:\-10\]\]
y\_test \= y\[test\_ids\[\-10:\]\]

#classifying using decision tree
clf \= tree.DecisionTreeClassifier()

#training (fitting) the classifier with the training set
clf.fit(x\_train, y\_train)

#predictions on the test dataset
pred \= clf.predict(x\_test)

print pred #predicted labels i.e flower species
print y\_test #actual labels
print (accuracy\_score(pred, y\_test))\*100 #prediction accuracy

Since we’re splitting randomly and the classifier trains on every iteration, the accuracy may vary. Running the above code gives:

\[0 1 1 1 0 2 0 2 2 2\]
\[0 1 1 1 0 2 0 2 2 2\]
100.0

The first line contains the labels (i.e. flower species) of the testing data as predicted by our classifier, and the second line contains the actual flower species as given in the dataset. We thus get an accuracy of 100% this time.

More on scikit-learn can be read in the [documentation](http://scikit-learn.org/stable/user_guide.html).