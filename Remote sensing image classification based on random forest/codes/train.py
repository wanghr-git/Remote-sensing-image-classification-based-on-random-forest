from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn import model_selection
import pickle

#  定义字典，便于来解析样本数据集txt
def Iris_label(s):
    it={b'Yes':0, b'No':1}
    return it[s]

path=r"E:\pyCharm\ID3\data.txt"
SavePath = r"E:\pyCharm\ID3\model.pickle"


#  1.读取数据集
data=np.loadtxt(path, dtype=float, delimiter=',', converters={3:Iris_label} )
#  converters={3:Iris_label}中“3”指的是第8列：将第8列的str转化为label(number)

#  2.划分数据与标签
x,y=np.split(data,indices_or_sections=(3,),axis=1) #x为数据，y为标签
x=x[:,0:3] #选取前3个波段作为特征
train_data,test_data,train_label,test_label = model_selection.train_test_split(x,y, random_state=1, train_size=0.9,test_size=0.1)

#  3.用100个树来创建随机森林模型，训练随机森林
classifier = RandomForestClassifier(n_estimators=100,
                               bootstrap = True,
                               max_features = 'sqrt')
classifier.fit(train_data, train_label.ravel())#ravel函数拉伸到一维


#  4.计算随机森林的准确率
print("训练集：",classifier.score(train_data,train_label))
print("测试集：",classifier.score(test_data,test_label))

#  5.保存模型
#以二进制的方式打开文件：
file = open(SavePath, "wb")
#将模型写入文件：
pickle.dump(classifier, file)
#最后关闭文件：
file.close()