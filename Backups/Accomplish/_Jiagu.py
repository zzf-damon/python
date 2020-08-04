import jiagu

text = """三官寨彝名“协奎迪”，原系明朝天启年间扯勒部永宁宣抚使奢崇明后裔领地。长期以来，这里的彝族人民一直保持和传承着许多优秀的彝族文化传统，二十世纪八十年代，被誉为彝族歌舞之乡，2002年列入全省20个保护与建设的民族村寨之一，2009年列为贵州省首批16个历史文化名村之一。现人2986人，其中彝族人口占73％，大多均可用母语顺畅交流。三官寨古彝礼俗传承良好，“呣哼”（唢呐）曲调亘远悠扬，撒麻舞、衣角舞原始生态，酒歌、情歌韵律传统，服饰等手工艺品技法古朴。三官彝寨酒歌系列按照迎宾落座、欢聚欢歌、离别送客和彝家待客礼俗整理打造，主要由三官彝歌队演绎而成。"""
print(text)
words = jiagu.seg(text) # 分词
print(words)

pos = jiagu.pos(words) # 词性标注
print(pos)

ner = jiagu.ner(text) # 命名实体识别
print(ner)

text = '汉服和服装'

words = jiagu.seg(text) # 默认分词
print(words)

words = jiagu.seg([text, text, text], input='batch') # 批量分词，加快速度。
print(words)

words = jiagu.seg(text, model='mmseg') # 使用mmseg算法进行分词
print(words)

text =  """三官寨彝名“协奎迪”，原系明朝天启年间扯勒部永宁宣抚使奢崇明后裔领地。长期以来，这里的彝族人民一直保持和传承着许多优秀的彝族文化传统，二十世纪八十年代，被誉为彝族歌舞之乡，2002年列入全省20个保护与建设的民族村寨之一，2009年列为贵州省首批16个历史文化名村之一。现人2986人，其中彝族人口占73％，大多均可用母语顺畅交流。三官寨古彝礼俗传承良好，“呣哼”（唢呐）曲调亘远悠扬，撒麻舞、衣角舞原始生态，酒歌、情歌韵律传统，服饰等手工艺品技法古朴。三官彝寨酒歌系列按照迎宾落座、欢聚欢歌、离别送客和彝家待客礼俗整理打造，主要由三官彝歌队演绎而成。"""

keywords = jiagu.keywords(text, 5) # 关键词
print(keywords)


summarize = jiagu.summarize(text, 1) # 摘要
print(summarize)

# jiagu.findword('input.txt', 'output.txt') # 根据文本，利用信息熵做新词发现。