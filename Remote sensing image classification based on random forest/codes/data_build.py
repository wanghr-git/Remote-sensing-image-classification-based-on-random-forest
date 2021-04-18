import gdal
import os
import random


# 读取tif数据集
def readTif(fileName):
    dataset = gdal.Open(fileName)
    if dataset == None:
        print(fileName + "文件无法打开")
    return dataset


Landset_Path = r"E:\pyCharm\ID3\Data5.tif"
LabelPath = r"E:\pyCharm\ID3\daataset.tif"
txt_Path = r"E:\pyCharm\ID3\data.txt"

##########################################################  读取图像数据
dataset = readTif(Landset_Path)
Tif_width = dataset.RasterXSize  # 栅格矩阵的列数
Tif_height = dataset.RasterYSize  # 栅格矩阵的行数
Tif_bands = dataset.RasterCount  # 波段数
Tif_geotrans = dataset.GetGeoTransform()  # 获取仿射矩阵信息
Landset_data = dataset.ReadAsArray(0, 0, Tif_width, Tif_height)
dataset = readTif(LabelPath)
Label_data = dataset.ReadAsArray(0, 0, Tif_width, Tif_height)

# 写之前，先检验文件是否存在，存在就删掉
if os.path.exists(txt_Path):
    os.remove(txt_Path)
# 以写的方式打开文件，如果文件不存在，就会自动创建
file_write_obj = open(txt_Path, 'w')

####################################################首先收集植被类别样本，
####################################################遍历所有像素值，
####################################################为植被的像元全部收集。
count = 0
for i in range(Label_data.shape[0]):
    for j in range(Label_data.shape[1]):
        #  我设置的植被类别在标签图中像元值为1
        if (Label_data[i][j] == 2):
            var = ""
            for k in range(Landset_data.shape[0]):
                var = var + str(Landset_data[k][i][j]) + ","
            var = var + "Yes"
            file_write_obj.writelines(var)
            file_write_obj.write('\n')
            count = count + 1

####################################################其次收集非植被类别样本，
####################################################因为非植被样本比植被样本多很多，
####################################################所以采用在所有非植被类别中随机选择非植被样本，
####################################################数量与植被样本数量保持一致。
Threshold = count
count = 0
for i in range(10000000000):
    X_random = random.randint(0, Label_data.shape[0] - 1)
    Y_random = random.randint(0, Label_data.shape[1] - 1)
    #  我设置的非植被类别在标签图中像元值为0
    if (Label_data[X_random][Y_random] == 1):
        var = ""
        for k in range(Landset_data.shape[0]):
            var = var + str(Landset_data[k][X_random][Y_random]) + ","
        var = var + "No"
        file_write_obj.writelines(var)
        file_write_obj.write('\n')
        count = count + 1
    if (count == Threshold):
        break

file_write_obj.close()