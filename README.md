# SPOko Machine Learning

SPOko machine learning can be used to identify any type of programming language in a text file. This can be integrated into IDEs to automatically recognize files format and enable linting based on the file type.

The full dataset used in this machine learning project has over 90,000 source codes. However, for speed and efficiency it has been reduced to about 9,000.

We were able to achieve an accuracy of 99.39%, 99.21%, 96.01% and 82.41% using LinearSVC, LogisticRegression, KNeighborsClassifier and SVC algorithm respectively.

Due to certain limitations we were only able to train our model on Dart, PHP, Python and C++.

We hope this project will be useful!

# Tutorials


## Fetching your own dataset

In case you do not want to use the [default dataset](dataset/default_dataset.csv) in the dataset folder you can gather your own data, it's simple!

Go to [settings.py](settings.py) and edit the following line

```python

# change to the directory where you have your source code files

crawl_from = 'C:/Users/oracle/desktop/projects' 

```

Then run the command below

```cmd

C:\Users\user\Desktop\lab> python index.py

```

This will automatically generate the dataset for you, by automatically performing the folowing on the files discovered.

- Remove comments in the file
- extract the keywords
- make sure that the new data is not in unique
- you can check [data.py](data.py) for more information


## Using your dataset

You might need to install Jupyter Notebook on your device!

Open [compare.ipynb](compare.ipynb) to compare models

Open [ml.ipynb](ml.ipynb) to train and save model


## Developer

[Oyeniyi Abiola Peace](https://twitter.com/_iamoracle])

## Contributors

0 contributors, be the first!

You can submit your dataset or send enquires to officialbilas(at)gmail(dot)com

Thanks