import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# load the CSV file
data = pd.read_csv('features_ADNI2.csv')

# separate features and labels
X = data.iloc[:, 2:].values
y = data.iloc[:, 1].values

# get the unique class names
class_names = data.iloc[:, 1].unique()

# split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# train the SVM model using cross-validation
clf = svm.SVC(kernel='linear')
scores = cross_val_score(clf, X_train, y_train, cv=5)
print('Cross Validation Scores:', scores)
print('Mean Accuracy:', scores.mean())

# fit the model on the full training data
clf.fit(X_train, y_train)

# make predictions on the testing set
y_pred = clf.predict(X_test)

# evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)

# print the confusion matrix
cm = confusion_matrix(y_test, y_pred)
print('Confusion Matrix:\n', cm)

# plot the confusion matrix
sns.heatmap(cm, annot=True, cmap='Blues', fmt='g', xticklabels=class_names, yticklabels=class_names)
plt.title("Confusion matrix for PPMI")
plt.xlabel('Predicted Class')
plt.ylabel('True Class')
plt.show()
