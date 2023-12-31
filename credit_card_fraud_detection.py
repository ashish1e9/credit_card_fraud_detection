# -*- coding: utf-8 -*-
"""Copy of Credit_card_fraud_detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NEBZ5575GceEK9Yn8EDf1mcVIVhseW9A
"""

import pandas as pd

from google.colab import drive
drive.mount('/content/drive')

data=pd.read_csv('/content/drive/MyDrive/Data analysys/creditcard.csv')

data.head()

data.tail()



seti=data.shape

print("Number of rows: ", seti[0])
print("Number of columns: ", seti[1])

data.info()

data.isnull().sum()

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
data['Amount']=sc.fit_transform(pd.DataFrame(data['Amount']))

print(data['Amount'].max())

data=data.drop(['Time'], axis=1)

data.shape

data.duplicated().any()

data= data.drop_duplicates()

data.shape

data['Class'].value_counts()

import seaborn as sns
import matplotlib.pyplot as plt

data['Class'] = data['Class'].astype('category')
sns.countplot(x='Class', data=data)
plt.show()

#undersampling

normal = data[data['Class']==0]
fraud = data[data['Class']==1]

normal.shape

fraud.shape

normal_sample=normal.sample(n=1000)
normal_sample.shape



new_data=pd.concat([normal_sample,fraud], ignore_index=True)

new_data['Class'].value_counts()

new_data.head()

X=new_data.drop('Class',axis=1)
Y=new_data['Class']

from sklearn.model_selection import train_test_split

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3, random_state=42)

from sklearn.linear_model import LogisticRegression
log = LogisticRegression()
log.fit(X_train,Y_train)

y_pred=log.predict(X_test)

from sklearn.metrics import accuracy_score

accuracy_score(Y_test,y_pred)

from sklearn.metrics import f1_score
f1_score(Y_test,y_pred)

from sklearn.metrics import recall_score
recall_score(Y_test,y_pred)

from sklearn.metrics import precision_score
precision_score(Y_test,y_pred)

from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier()
dt.fit(X_train,Y_train)

y_pred2 = dt.predict(X_test)

accuracy_score(Y_test,y_pred2)

precision_score(Y_test,y_pred2)

recall_score(Y_test,y_pred2)

f1_score(Y_test,y_pred2)

#Random forest Classifier

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
rf.fit(X_train,Y_train)

y_pred3=rf.predict(X_test)

accuracy_score(Y_test,y_pred3)

precision_score(Y_test,y_pred3)

f1_score(Y_test,y_pred3)

recall_score(Y_test,y_pred3)

final_result = pd.DataFrame({'Models':['LR','DT','RF'],
                             'Accuracy':[
                                 accuracy_score(Y_test,y_pred),
                                 accuracy_score(Y_test,y_pred2),
                                 accuracy_score(Y_test,y_pred3),
                             ],
                             'Precision':[
                                 precision_score(Y_test,y_pred),
                                 precision_score(Y_test,y_pred2),
                                 precision_score(Y_test,y_pred3),
                             ],
                             'f1_score':[
                                 f1_score(Y_test,y_pred),
                                 f1_score(Y_test,y_pred2),
                                 f1_score(Y_test,y_pred3),
                             ],
                             'Recall_score':[
                                 recall_score(Y_test,y_pred),
                                 recall_score(Y_test,y_pred2),
                                 recall_score(Y_test,y_pred3),
                             ]
                             })

print(final_result)



import seaborn as sns
import matplotlib.pyplot as plt

# Assuming final_data is your DataFrame with columns 'model' and 'acc'
sns.barplot(x='Models', y='Accuracy', data=final_result)

# Add labels and title
plt.xlabel('Models')
plt.ylabel('Accuracy')
plt.title('Models vs Accuracy')

# Show the plot
plt.show()

#oversampling

x = data.drop('Class', axis=1)
y = data['Class']

print(x.shape,y.shape)

from imblearn.over_sampling import SMOTE
x_res,y_res = SMOTE().fit_resample(x,y)

print(x_res.shape,y_res.shape)

y_res.value_counts()

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x_res,y_res,test_size=0.3, random_state=42)

#LogisticRegression

from sklearn.linear_model import LogisticRegression
log = LogisticRegression()
log.fit(x_train,y_train)

pred_value1=log.predict(x_test)

accuracy_score(y_test,pred_value1)

precision_score(y_test,pred_value1)

f1_score(y_test,pred_value1)

recall_score(y_test,pred_value1)

#Decision Tree model

from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier()
dt.fit(x_train,y_train)

pred_value2=log.predict(x_test)

accuracy_score(y_test,pred_value2)

precision_score(y_test,pred_value2)

f1_score(y_test,pred_value2)

recall_score(y_test,pred_value2)

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
rf.fit(x_train,y_train)

pred_value3=rf.predict(x_test)

accuracy_score(y_test,pred_value3)

f1_score(y_test,pred_value3)

recall_score(y_test,pred_value3)

precision_score(y_test,pred_value3)

final_result2 = pd.DataFrame({'Models':['LR','DT','RF'],
                             'Accuracy':[
                                 accuracy_score(y_test,pred_value3),
                                 accuracy_score(y_test,pred_value3),
                                 accuracy_score(y_test,pred_value3),
                             ],
                             'Precision':[
                                 precision_score(y_test,pred_value3),
                                 precision_score(y_test,pred_value3),
                                 precision_score(y_test,pred_value3),
                             ],
                             'f1_score':[
                                 f1_score(y_test,pred_value3),
                                 f1_score(y_test,pred_value3),
                                 f1_score(y_test,pred_value3),
                             ],
                             'Recall_score':[
                                 recall_score(y_test,pred_value3),
                                 recall_score(y_test,pred_value3),
                                 recall_score(y_test,pred_value3),
                             ]
                             })

print(final_result2)

import seaborn as sns
import matplotlib.pyplot as plt
sns.barplot(x='Models', y='Accuracy', data=final_result2)
plt.xlabel('Models')
plt.ylabel('Accuracy')
plt.title('Models vs Accuracy')
plt.show()

#randomforest is giving best results by our analysis
import joblib
joblib.dump(rf,"credit_card_model")
model = joblib.load("credit_card_model")

pred = model.predict([[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,]])

if pred == 0:
  print("Normal Transaction")
else:
  print("Fraudulent Transaction")

