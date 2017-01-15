import requests
from numpy import genfromtxt, zeros, mean
from pylab import plot, figure, subplot, hist, xlim, show
from sklearn.naive_bayes import GaussianNB
from sklearn import model_selection


# 数据导入与可视化
url = 'http://aima.cs.berkeley.edu/data/iris.csv'
res = requests.get(url).content
with open('iris.csv', 'wb') as f:
    f.write(res)

data = genfromtxt('iris.csv', delimiter=',', usecols=([0,1,2,3]))
target = genfromtxt('iris.csv', delimiter=',', usecols=([4]), dtype=str)
plot(data[target=='setosa', 0], data[target=='setosa', 2], 'bo')
plot(data[target=='versicolor',0],data[target=='versicolor',2],'ro')
plot(data[target=='virginica',0],data[target=='virginica',2],'go')
show()

xmin = min(data[:,0])
xmax = max(data[:,0])
figure()
subplot(411) # distribution of the setosa class (1st, on the top)
hist(data[target=='setosa',0],color='b',alpha=.7)
xlim(xmin,xmax)
subplot(412) # distribution of the versicolor class (2nd)
hist(data[target=='versicolor',0],color='r',alpha=.7)
xlim(xmin,xmax)
subplot(413) # distribution of the virginica class (3rd)
hist(data[target=='virginica',0],color='g',alpha=.7)
xlim(xmin,xmax)
subplot(414) # global histogram (4th, on the bottom)
hist(data[:,0],color='y',alpha=.7)
xlim(xmin,xmax)
show()


# 分类
t = zeros(len(target))
t[target == 'setosa'] = 1
t[target == 'versicolor'] = 2
t[target == 'virginica'] = 3

classifier = GaussianNB()
train, test, t_train, t_test = model_selection.train_test_split(data, t, test_size=0.4, random_state=0)
classifier.fit(train, t_train)
# print(classifier.score(test, t_test))
scores = model_selection.cross_val_score(classifier, data, t, cv=6)  # 交叉验证
print(scores)
print(mean(scores))
