# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
from pandas import read_csv
from matplotlib import pyplot
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from sklearn.svm import SVC


# %%
#open the dataset
data_file = open("dataset/default_dataset.csv")

#the two columns are content and category
names = ['content','category']

#read the data set as csv
dataset = read_csv(data_file, names=names)


# %%
#split the dataset into content and category columns
content = dataset['content']

categories = dataset['category']


# %%
#turn strings into integers for easy calculation using bag of words algorithm
vectorizer = CountVectorizer()

content = vectorizer.fit_transform(content)


# %%
#split data into train and test
content_train, content_test, categories_train, categories_test = train_test_split(content, categories, test_size=0.2, random_state=1, shuffle=True)


# %%
#train our model
model = LogisticRegression(solver='liblinear', multi_class='ovr', max_iter=10)
model.fit(content_train, categories_train)


# %%
#make prediction
predictions = model.predict(content_test)


# %%
print(predictions)


# %%


