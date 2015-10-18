from sklearn.datasets import fetch_mldata
from sklearn import svm
from sklearn.cross_validation import train_test_split as tts

mnist = fetch_mldata('MNIST original')
print("Data fetched.")

Xtr, Xts, Ytr, Yts = tts(mnist.data,
                         mnist.target,
                         test_size=10000)
print("tts done.")
clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(Xtr, Ytr)
print("fitted.")
predicted_label = clf.predict(Xts[-1])
