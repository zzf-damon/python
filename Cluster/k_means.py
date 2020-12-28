import numpy as np
import matplotlib.pyplot as plt
# from BertVector import bert_vector,bert_vector_cut


# 加载数据
def loadDataSet(fileName):
    data = np.loadtxt(fileName, delimiter='\t')
    return data


# 欧氏距离计算
def distEclud(x, y):
    return np.sqrt(np.sum((x - y) ** 2))  # 计算欧氏距离


# 为给定数据集构建一个包含K个随机质心的集合
def randCent(dataSet, k):
    m = len(dataSet)
    centroids = np.zeros((k, 2))
    for i in range(k):
        index = int(np.random.randint(0, m))  #
        centroids[i, :] = index, 0
    return centroids


# k均值聚类
def KMeans(dataSet, k):
    m = len(dataSet)
    # 第一列存样本属于哪一簇
    # 第二列存样本的到簇的中心点的误差
    clusterAssment = np.mat(np.zeros((m, 2)))
    clusterChange = True

    # 第1步 初始化centroids
    centroids = randCent(dataSet, k)
    while clusterChange:
        clusterChange = False

        # 遍历所有的样本（行数）
        for i in range(m):
            minDist = 100000.0
            minIndex = -1

            # 遍历所有的质心
            # 第2步 找出最近的质心
            for j in range(k):
                # 计算该样本到质心的欧式距离
                distance = bert_vector_cut(dataSet[(int(centroids[j][0]))], dataSet[i])
                if distance < minDist:
                    minDist = distance
                    minIndex = centroids[j][0]
            # 第 3 步：更新每一行样本所属的簇
            if clusterAssment[i, 0] != minIndex:
                clusterChange = True
                clusterAssment[i, :] = minIndex, minDist
        # 第 4 步：更新质心
        # for j in range(k):
        #     index_array = np.nonzero(clusterAssment[:, 0].A == j)[0]
        #     count = 0
        #     for i in index_array:
        #         count += clusterAssment[i][1]
        #     count = count/len(index_array)
        #     centroids[j, :] = np.mean(pointsInCluster, axis=0)  # 对矩阵的行求均值

    print("Congratulations,cluster complete!")
    print(clusterAssment)
    return centroids, clusterAssment


def showCluster(dataSet, k, centroids, clusterAssment):
    m = len(dataSet)
    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
    if k > len(mark):
        print("k值太大了")
        return 1
    # 绘制所有的样本
    for i in range(m):
        index = clusterAssment[i].A.tolist()
        markIndex = int(index[0][0])
        plt.plot(i, markIndex, mark[markIndex])

    # mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']
    # # 绘制质心
    # for i in range(k):
    #     plt.plot(centroids[i, 0], centroids[i, 1], mark[i])

    plt.show()


dataSet = [
    "杭州消防回复保姆纵火案受害者家属信息公开申请:将延期答复",
    "韩伯平:杭州保姆纵火案背后折射出的人性_韩伯平工作室_新浪博客",
    "杭州保姆纵火案未影响房价:该小区法拍房高价拍出",
    "杭州保姆纵火案:大火来临时,豪宅成了被拧紧的瓶口",
    "记者手记|杭州保姆纵火案:未解之问",
    "杭州保姆纵火案二审维持死刑判决",
    "杭州纵火案保姆判死 厘清救火责任才是全部正义",
    "杭州保姆纵火案受害人家属提出信息公开",
    "B站推青少年模式：筛选特定内容到首页 限制使用时间",
    "Win10 5月更新升级热情不高：仅占1.4%份额"
]
k = 3
centroids, clusterAssment = KMeans(dataSet, k)

showCluster(dataSet, k, centroids, clusterAssment)
