from sklearn.datasets import load_wine
import pandas as pd
import numpy as np
np.set_printoptions(precision=4)
from matplotlib import pyplot as plt
import seaborn as sns
sns.set()
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
wine = load_wine()
X = pd.DataFrame(wine.data, columns=wine.feature_names)
numOfFeatures=X.shape[1]

y = pd.Categorical.from_codes(wine.target, wine.target_names)
df = X.join(pd.Series(y, name='class'))

# Calculate within-class scatter
class_feature_means = pd.DataFrame(columns=wine.target_names)
withinClass=np.zeros((numOfFeatures,numOfFeatures))
for c, rows in df.groupby('class'):
	class_feature_means[c]= rows.mean()
	s=np.zeros((numOfFeatures,numOfFeatures))
	rows=rows.drop(['class'],axis=1)
	sub=rows.values-class_feature_means[c].values.reshape(1,numOfFeatures)
	withinClass+= (sub.T).dot((sub))
#Calculate between class scatter
allMean= X.mean().values.reshape(numOfFeatures,1)
betweenClass=np.zeros((numOfFeatures,numOfFeatures))
for c, rows in df.groupby('class'):
	n=rows.shape[0]
	classMean=class_feature_means[c].values.reshape(numOfFeatures,1)
	sub=classMean - allMean
	betweenClass+= n*(sub).dot((sub).T)
#Find Eigen Values and Eigen Vectors
eigValues,eigVectors =np.linalg.eig(np.linalg.inv(withinClass).dot(betweenClass))
# Put the in pair list
pairs = [(np.abs(eigValues[i]), eigVectors[:,i]) for i in range(len(eigValues))]
# Sort Eigen Values
pairs =sorted(pairs, key=lambda x:x[0],reverse=True)
# Keep only the first two eigenvectors
w_matrix = np.hstack((pairs[0][1].reshape(13,1), pairs[1][1].reshape(13,1))).real
#Project data into the new spece, spanned by the highest two eigenvectors
X_lda = np.array(X.dot(w_matrix))
#Encode labels
le = LabelEncoder()
y = le.fit_transform(df['class'])
plt.xlabel('LD1')
plt.ylabel('LD2')
plt.title('Data After LDA Projection')
plt.scatter(
    X_lda[:,0],
    X_lda[:,1],
    c=y,
    cmap='rainbow',
    alpha=0.7,
    edgecolors='b'
)
plt.show()

#Train a Decision Tree
#Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_lda, y, random_state=1)
dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)
y_pred = dt.predict(X_test)
#Confusion Matrix
print(confusion_matrix(y_test, y_pred))
#100 % accuracy no error !!!