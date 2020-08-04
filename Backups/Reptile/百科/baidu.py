import time,re
from Request_Header import request_py
url = "https://baike.baidu.com/item/"

nation =["傣族","彝族"]

dict = {}
doc = request_py(url+nation[0])
basic_dts = doc(".basic-info dl dt").items()
basic_dds = doc(".basic-info dl dd").items()
basic_dt_list = basic_dd_list =[]
# for basic_dt in basic_dts:
#     basic_dt_list.append(basic_dt.text())
#
# for basic_dd in basic_dds:
#     basic_dd_list.append(basic_dd.text())


def rm_space(str):
    str = re.sub(" ","",str)
    str= re.sub("\xa0","",str)
    return str

for basic_dt,basic_dd in zip(basic_dts,basic_dds):
    relationship= rm_space(basic_dt.text())
    entity = rm_space(basic_dd.text())
    dict[relationship]=entity