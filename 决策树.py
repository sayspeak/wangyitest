import numpy as np
from sklearn import tree
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import classification_report
from sklearn.cross_validation import train_test_split
data = np.array([[1.5 ,50,'thin'], [1.5 ,60, 'fat'] ,[1.6 ,40 ,'thin'], [1.6 ,60, 'fat'] ,[1.7 ,60 ,'thin'], [1.7 ,80 ,'fat'] ,[1.8 ,60 ,'thin'],[1.8 ,90 ,'fat'], [1.9 ,70 ,'thin'],[1.9 ,80, 'fat']])
labels = data[:,-1]
y = np.zeros(labels.shape)
y[labels == 'fat'] = 1
y[labels == 'thin'] = 0
x = data[:,:2]
x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.2,random_state=0)
clf=tree.DecisionTreeClassifier(criterion='entropy')
clf.fit(x_train, y_train)

with open("tree.dot", 'w') as f:
    f = tree.export_graphviz(clf, out_file=f)

print (clf.feature_importances_)
precision, recall, thresholds = precision_recall_curve(y_train,clf.predict(x_train))
answer = clf.predict_proba(x)[:,1]
print(classification_report(y,answer,target_names = ['thin', 'fat']))