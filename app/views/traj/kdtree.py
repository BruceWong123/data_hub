from sklearn.neighbors import KDTree
import numpy as np


class KDTreeAdaptor(object):
    def __init__(self, leaf_size=30, metric='euclidean') -> None:
        self.leaf_size = leaf_size
        self.metric = metric
        self.data = None
        self.data_info = None
        self.tree = None

    def construct_kdtree(self, data, data_info):
        self.data = data
        self.data_info = data_info
        self.tree = KDTree(np.array(self.data), leaf_size=self.leaf_size, metric=self.metric)

    def query_with_k(self, points, k):
        if not isinstance(points, np.ndarray):
            points = np.array(points)
        if len(points.shape) != 2:
            raise ValueError("only support shape of 2")
        out_index = self.tree.query(points, k=min(k, len(self.data_info)), return_distance=False)
        output = []
        for i in range(points.shape[0]):
            hdmap_info = []
            for idx in out_index[i]:
                hdmap_info.append([self.data_info[idx]])
            output.append(hdmap_info)
        return output

    def query_with_radius(self, points, r):
        if not isinstance(points, np.ndarray):
            points = np.array(points)
        if len(points.shape) != 2:
            raise ValueError("only support shape of 2")
        out_index = self.tree.query_radius(points, r)
        output = []
        for i in range(points.shape[0]):
            hdmap_info = []
            for idx in out_index[i]:
                hdmap_info.append([self.data_info[idx]])
            output.append(hdmap_info)
        return output





