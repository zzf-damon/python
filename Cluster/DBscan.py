import numpy as np


def get_cores_area(data, dist_matrix, eps, minPts):
    core_points = {}
    if dist_matrix is None:
        dist_matrix = pairwise_distance(data, data)

    for i, core_near_dis in enumerate(dist_matrix):
        inner_points = []	# 包含的点
        for j, dis in enumerate(core_near_dis):
            if i == j:
                continue
            if dis < eps:
                inner_points.append(j)
            if len(inner_points) >= minPts:
                core_points[i] = inner_points	# 标记核心点族群所包含的点
    return core_points

# 计算两点欧式距离
def pairwise_distance(x, y):
    xx = np.sum(x * x, axis=1, keepdims=True)
    yy = np.sum(y * y, axis=1, keepdims=True)
    xy = np.matmul(x, y.T)
    d = xx + yy.T - 2 * xy
    return d


def dbscan(data, eps, minPts):
    dist_matrix = pairwise_distance(data, data)
    cores_area = get_cores_area(data, dist_matrix, eps, minPts)
    clusters = []
    while len(cores_area) > 0:
        cluster = set()
        visit_set = set()
        core, nears = cores_area.popitem()
        visit_set.add(core)
        visit_set.update(nears)
        while len(visit_set) > 0:
            point = visit_set.pop()
            cluster.add(point)
            if point in cores_area:
                visit_set.update(cores_area.pop(point))
        clusters.append(cluster)

    cluster = np.zeros(len(data))
    for i, c in enumerate(clusters):
        for item in c:
            cluster[item] = i
    return cluster


if __name__ == '__main__':
    # print("----DBscan----")
    data, labels = du.read_data()
    eps_set = np.arange(0.15, 0.3, 0.01).round(2)
    minPts_set = np.arange(3, 10, 1)
    for eps in eps_set:
        for minPts in minPts_set:
            print("eps=", eps, ", minPts=", minPts)
            cluster = dbscan(data, eps, minPts)
            purity, fscore, precision, recall = du.standard(cluster)
            print("purity=", purity, ", F-score=", fscore)
    # print("----------------")

