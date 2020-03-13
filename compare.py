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
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC, LinearSVC

# import nltk

# nltk.download('stopwords')


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
models = []
results = []
names = []
models.append(('KNN', KNeighborsClassifier()))
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('SVM', SVC(gamma='auto')))
models.append(('LVM', LinearSVC()))


for name, model in models:
    
    kfold = StratifiedKFold(n_splits=20, random_state=2, shuffle=True)
    
    cv_results = cross_val_score(model, content_train, categories_train, cv=kfold, scoring="accuracy")
    
    names.append(name)
    
    results.append(cv_results)
    
    print('%s: %f %f' %(name, cv_results.mean(), cv_results.std()))

pyplot.boxplot(results, labels=names)

pyplot.title("compare")

pyplot.show()


# %%


