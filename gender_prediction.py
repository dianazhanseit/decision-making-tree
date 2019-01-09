from sklearn import tree
# [height, weight, shoe size]
X = [[181,80,44], [168,72,38], [177,70,43], [160,60,38], [155, 54,37]]
Y = ['male', 'female', 'male', 'female', 'female']
 # to store our decision tree model: clf - classifier
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)
prediction = clf.predict([[190,70,43]])
print(prediction)