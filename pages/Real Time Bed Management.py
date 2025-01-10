import streamlit as st
import sklearn 
from sklearn import datasets
from sklearn.datasets import load_iris
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

st.title("Real Time Bed Management(In Progress)")

iris_df = pd.read_csv("csv files/iris.csv")
print(iris_df.head())

print(iris_df.info())
print(iris_df['variety'].unique())

species_mapping= {'Setosa':0,'Versicolor':1, 'Virginica':2 }
iris_df['target'] =  iris_df['variety'].map(species_mapping)

print(iris_df)


X= iris_df.drop(columns=['variety', 'target'])
y= iris_df['target'] 

print("features shapes:", X.shape)
print("target shapes:", y.shape)
print(X.head())


X.train, X.test, y.train, y.test = train_test_split(X,y, test_size=0.2, random_state=42)
print( y.test.shape)

model = RandomForestClassifier(random_state=42)
model.fit(X.train, y.train)

y_pred=model.predict(X.test)

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y.test, y_pred)

print(accuracy)
