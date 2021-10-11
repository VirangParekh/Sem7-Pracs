# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import urllib.request
from google.colab import drive
from pyspark import SparkContext
from pyspark.sql import SparkSession
import findspark
import os
from IPython import get_ipython

# %%
get_ipython().system('apt-get install openjdk-8-jdk-headless -qq > /dev/null ')


# %%
get_ipython().system(
    'wget -q https://archive.apache.org/dist/spark/spark-3.0.0/spark-3.0.0-bin-hadoop3.2.tgz')


# %%
get_ipython().system('tar xf spark-3.0.0-bin-hadoop3.2.tgz')


# %%
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = "/content/spark-3.0.0-bin-hadoop3.2"


# %%
get_ipython().system('pip install -q findspark')


# %%
findspark.init()
spark = SparkSession.builder.master("local[*]").getOrCreate()
sc = SparkContext.getOrCreate()


# %%
drive.mount('/content/drive')


# %%
shkspr = urllib.request.urlretrieve(
    'https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt', '/content/drive/My Drive/shakespeare.txt')


# %%
Words = sc.textFile("/content/drive/My Drive/shakespeare.txt")
WordsCount = Words.flatMap(lambda line: line.split(" ")
                           ).map(lambda word: (word, 1))
WordsCount.count()


# %%
DistinctWordsCount = WordsCount.reduceByKey(lambda a, b: a+b)
DistinctWordsCount.count()


# %%
SortedWordsCount = DistinctWordsCount.map(lambda a: (a[1], a[0])).sortByKey()


# %%
SortedWordsCount.top(20)


# %%
Sorted_final = SortedWordsCount.map(lambda a: (a[1], a[0]))
Sorted_final.top(20)


# %%
