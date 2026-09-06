#------------------------------------------------------
# Deep leraning pipeline
#------------------------------------------------------
# 1. Read data from CSv
# 2. Data Analysis (EDA)
# 3. Preprocessing
# 4. Train Test Split
# 5. Feature Scaling
# 6. FNN Model training
# 7. Model Evaluation
# 8. Graphical Representation
# 9. Model Preserve
# 10. Model loading
# 11. Test Unseen Data
#------------------------------------------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix 
#------------------------------------------------------
# 1. Read data from CSV
#------------------------------------------------------

print("1. Read data from CSV")

data = pd.read_csv("placement_data.csv")

print("Complete Dataset")
print(data)

#------------------------------------------------------
#2. Data Analysis (EDA)
#------------------------------------------------------

print("2. Data Analysis (EDA)")

print("First 5 rows : ")
print(data.head())

print("Columns of dataset")
print(data.columns)

print("Shape of Data set")
print(data.shape)

print("Statistical summary :")
print(data.describe)

#------------------------------------------------------
# 3. Preprocessing
#------------------------------------------------------

print("Preprocessing")

X = data[['Aptitude', 'Coding', 'Communication', 'Academics', 'Internship']]
Y = data['Placed']

print("Input features")
print(X.head())

print("Output features")
print(Y.head())

#------------------------------------------------------
#4. Train Test Split
#------------------------------------------------------

print("4. Train Test Split")

X_train, X_test, Y_train , Y_test = train_test_split(X,Y,test_size=0.30,random_state=42)

print("Training input Shape : ",X_train.shape)
print("Testing input Shape : ",X_test.shape)
print("Training Output Shape : ",Y_train.shape)
print("Testing Output Shape : ",Y_test.shape)

#------------------------------------------------------
# 5. Feature Scalling
#------------------------------------------------------

print("Feature Scalling")

scalar = StandardScaler()

X_train_scaled = scalar.fit_transform(X_train) 
X_test_scaled = scalar.fit_transform(X_test)

print("Scaled Training data : ")
print(X_train_scaled[:5])

#------------------------------------------------------
# 6. FNN Model Training
#------------------------------------------------------

print("6. FNN Model training")
model=MLPClassifier(
    hidden_layer_sizes=(8,4),
    activation='relu',
    solver="adam",
    max_iter=1000,
    random_state= 42
)

print(model)

print("Train the model : ")

model.fit(X_train_scaled,Y_train)
print("Model training completed")

#------------------------------------------------------
# 7. Model Evaluation
#------------------------------------------------------

print("Model Evaluation")

Y_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(Y_test,Y_pred)

print("Accuracy is : ",accuracy)

cm = confusion_matrix(Y_test,Y_pred)

print("Confusion matrix : ",cm)

print("Predicct the probability : ")

Y_prob = model.predict_proba(X_test_scaled)

print(Y_prob[:5])

#------------------------------------------------------
# 9. Model Preserve
#------------------------------------------------------

print("9. Model Preserve")

joblib.dump(model,"placement_fnn_model.pkl")
joblib.dump(scalar,"placement_scalar.pkl")

print("Model and Scalar gets dumped successfully")

#------------------------------------------------------
# 10. Model Loading and preserve
#------------------------------------------------------
print("10. Model Loading and preserve")

loaded_model = joblib.load("placement_fnn_model.pkl")
loaded_scalar = joblib.load("placement_scalar.pkl")

print("Model gets loaded successfully")

#------------------------------------------------------
# 11. Test Unseen Data
# 
# Aptitude :        70
# Coding :          75
# Communication :   80
# Academics :       85
# Internship :      1
#------------------------------------------------------

new_student = pd.DataFrame([[70,75,80,85]],columns = ['Aptitude', 'Coding', 'Communication', 'Academics', 'Internship'])

new_student_scaled = loaded_scalar.transform(new_student)

new_prediction = loaded