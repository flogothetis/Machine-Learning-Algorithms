from sklearn.datasets import load_wine
import pandas as pd
import numpy as np
np.set_printoptions(precision=4)
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import multiprocessing as mp


class kNN:
	#Calculate Euclidean Distance of a test sample with the whole training set
	def getNeighboors(self, data, labels, test_point, k):
		euclidean_distance = np.sqrt(np.sum((data.values- test_point)**2,axis=1))
		pairs = [(euclidean_distance[i], labels[i]) for i in range(len(euclidean_distance))]
		#Sort all euclidean distances
		pairs = sorted(pairs, key=lambda x: x[0], reverse=False)[:k];
		return pairs

	#Classify test point
	def classify(self,data, labels, test_data, test_labels, k):
		if(k > data.shape[0]):
			return -1
		count=0
		for ((index, rows), y) in zip(test_data.iterrows(),test_labels):
			neighbors = self.getNeighboors(data, labels, rows.values,k)
			output_values = [category[1] for category in neighbors]
			#Categirize according to max voting rule
			prediction = max(set(output_values), key=output_values.count)
			if(prediction==y):
				count +=1
		return count/test_data.shape[0]* 100

	def classifyInParallel(self,data, labels, test_data, test_labels, k):
		if(k > data.shape[0]):
			return -1
		count=0
		pool = mp.Pool(processes= 8)

		arr = [pool.apply(self.getNeighboors, args=(data, labels, rows.values, k)) for (index, rows) in test_data.iterrows()]
		pool.close()
		for (neighbors, y) in zip(arr,test_labels):
			output_values = [category[1] for category in neighbors]
			prediction = max(set(output_values), key=output_values.count)
			if(prediction==y):
				count +=1
		return count/test_data.shape[0]* 100



if __name__ == '__main__':
	#Load Wine Dataset
	wine = load_wine()
	X = pd.DataFrame(wine.data, columns=wine.feature_names)
	y = pd.Categorical.from_codes(wine.target, wine.target_names)
	df = X.join(pd.Series(y, name='class'))
	le = LabelEncoder()
	y = le.fit_transform(df['class'])
	#Split data
	X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
	#Run KNN
	mykNN= kNN()
	# Get accuracy (k=16)
	result=mykNN.classifyInParallel(X_train,y_train,X_test,y_test,16);
	if(result>=0):
		print('Accuracy:', result)
	else:
		print('An error occured')