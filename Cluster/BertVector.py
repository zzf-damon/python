# -*- coding: utf-8 -*-
import numpy, jieba, re
from gensim.models import word2vec
import numpy as np
import jieba.posseg as pseg

bc = BertClient(ip='', check_version=False, check_length=False)
with open("./Datas/stopwords.txt", "r", encoding='utf-8') as f:
    STOPWORDS = f.readlines()
N_LIST = ["n", "nr", "nr1", "nr2", "nrj", "nrf", "ns", 'nsf', "nt", "nz", "nl", "ng", "v", "vd", "vn", "vshi", "vyou",
          "vf", "vx", "vi", "vl", "vg"]


def robust(actual_do):
    def add_robust(*args, **keyargs):
        try:
            return actual_do(*args, **keyargs)
        except:
            print('程序出错，出错的方法名是: %s' % actual_do.__name__)

    return add_robust



def bert_vector_1(title):
    vec1 = bc.encode([title], is_tokenized=True)
    return vec1

@robust
def bert_vector(cluster_center: str, contrast_sentence: str) -> int:
    '''
    :param cluster_center:  簇心
    :param contrast_sentence:  需要判断的句子
    :return: 两句话的欧式距离
    '''
    vec1 = bc.encode(list(filter(None,[participle(cluster_center)])), is_tokenized=True)
    vec2 = bc.encode(list(filter(None,[participle(contrast_sentence)])), is_tokenized=True)
    return numpy.sqrt(numpy.sum(numpy.square(vec1 - vec2)))


# op7=np.dot(vector1,vector2)/(np.linalg.norm(vector1)*(np.linalg.norm(vector2)))
# print(op7)
def bert_vector_cut(cluster_center: str, contrast_sentence: str) -> int:
    vector1 = bc.encode([cluster_center])
    vector2 = bc.encode([contrast_sentence])
    return numpy.sqrt(numpy.sum(numpy.square(vector1 - vector2)))
    # return np.dot(vector1,vector2)/(np.linalg.norm(vector1)*(np.linalg.norm(vector2)))





def stopwords_list(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


if __name__ == '__main__':
    str1 = "无证,驾驶,肇事,逃逸,指使,铁证"
    str2 = "淮滨,发生,肇事,逃逸,致,人,死亡,警方,小时,破案"
    str3 = "犯罪,嫌疑人,肇事,逃逸"
    str4 = "天津,犯罪,嫌疑人,李某辉,犯,交通肇事,逃逸,罪,警"
    print(bert_vector(cluster_center=str1, contrast_sentence=str2))
    print(bert_vector(cluster_center=str2, contrast_sentence=str3))
    print(bert_vector(cluster_center=str3, contrast_sentence=str4))
    print(bert_vector(cluster_center=str1, contrast_sentence=str4))
