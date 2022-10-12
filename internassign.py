# -*- coding: utf-8 -*-
"""internassign.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rtLSGCWMTkkoPIsHXqmaQDjZ4hQnv__d
"""

Reg no-1081
Name-Rishitha Bandi
Date-12/10/2022

import pandas as pd
import numpy as np

data =pd.read_csv("/content/Enrollments_28092022.csv")
data

data.info()

rows=len(data)
print("no.of rows:",rows)

cols=len(data.axes[1])
print("no.of columns:",str(cols))

import matplotlib.pyplot as plt
import statistics as stat

plt.hist(data["DEGREE"])
plt.show()

plt.hist(data["INTERMEDIATE"])
plt.show()

plt.hist(data["SSC"])
plt.show()

data["INTERNSHIP"].value_counts()

courses=["Data Science","Cloud Computing Services(AWS)","Mean Stack Web Development"]
students=[156,90,51]
plt.pie(students,labels=courses,autopct="%1.2f%%")
plt.show()

#Degree
print("Mean=",np.mean(data["DEGREE"]))
print("Median=",np.median(data["DEGREE"]))
print("Mode=",stat.mode(data["DEGREE"]))

#Intermediate
print("Mean=",np.mean(data["INTERMEDIATE"]))
print("Median=",np.median(data["INTERMEDIATE"]))
print("Mode=",stat.mode(data["INTERMEDIATE"]))

#10th class
print("Mean=",np.mean(data["SSC"]))
print("Median=",np.median(data["SSC"]))
print("Mode=",stat.mode(data["SSC"]))

df = lambda x:np.std(x, ddof=1)/np.mean(x)*100

#Degree
print("Range=",max(data["DEGREE"])-min(data["DEGREE"]))
print("co-effecient of variations =",df(data["DEGREE"]))
data["DEGREE"].describe()

#Intermediate
print("Range=",max(data["INTERMEDIATE"])-min(data["INTERMEDIATE"]))
print("co-effecient of variations=",df(data["INTERMEDIATE"]))
data["INTERMEDIATE"].describe()

#10th class
print("Range=",max(data["SSC"])-min(data["SSC"]))
print("co-effecient of variation=",df(data["SSC"]))
data["SSC"].describe()

def outlier(a):
  q1 = np.quantile(a,0.25)
  q3 = np.quantile(a,0.75)
  med = np.median(a)
  iqr = q3-q1
  upper_bound = q3+(1.5*iqr)
  lower_bound = q1-(1.5*iqr)
  print(iqr,upper_bound,lower_bound)
  print("Inter-Quartile Range:",iqr)
  outliers = a[(a<=lower_bound) | (a>=upper_bound)]
  print("The following are the outliers in the boxplot:\n{}".format(outliers))

#Degree
outlier(data["DEGREE"])

#Intermediate
outlier(data["INTERMEDIATE"])

#10th class
outlier(data["SSC"])

import scipy.stats as stats

print("Standard Scores of Degree:")
print(stats.zscore(data["DEGREE"]))

print("Standard Scores of Intermediate:")
print(stats.zscore(data["INTERMEDIATE"]))

print("Standard Scores of 10th class:")
print(stats.zscore(data["SSC"]))

plt.boxplot(data["DEGREE"])
plt.show()

plt.boxplot(data["INTERMEDIATE"])
plt.show()

plt.boxplot(data["SSC"])
plt.show()

def func(b):
  q9 = np.quantile(b,0.9)
  li=b[b==q9]
  print("No.of students with 90% percentile:",li.count())

#Degree
func(data['DEGREE'])

#Intermediate
func(data['INTERMEDIATE'])

#10th Class
func(data['SSC'])

