import numpy as np
from sklearn import neighbors
knn = neighbors.KNeighborsClassifier()
knn.fit(x,y)
knn.predict()