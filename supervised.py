from sklearn import datasets,svm
import matplotlib.pyplot as plt
iris = datasets.load_iris()
digits = datasets.load_digits()
plt.gray()
plt.matshow(digits.images[0])
plt.show()
clf = svm.SVC(gamma=0.001,C=100.)
clf.fit(digits.data[:-1], digits.target[:-1])  
data=clf.predict(digits.data[20:])
print(data)
print(digits.target[20:])
