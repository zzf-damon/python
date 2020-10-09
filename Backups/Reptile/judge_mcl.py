import jieba
import re
import time
import requests, json

punctuation = '!,;:?"\'. '
pattern = r',|\.|/|;|\'|`|\[|\]|<|>|\?|:|"|\{|\}|\~|!|@|#|\$|%|\^|&|\(|\)|-|=|\_|\+|，|。|、|；|‘|’|【|】|·|！| |…|（|）'

src_text = ""
teg_text = ""
data_xh = ""


def get_cookie():
    CardId = "20182204158"
    response = requests.post("http://222.197.219.6:8080/cclzc/login", {"yhbh": CardId, "yhmm": CardId}).cookies
    return {"JSESSIONID": response["JSESSIONID"]}


while True:
    try:
        cookies = get_cookie()
        signC = "search"
        url2 = "http://222.197.219.6:8080/cclzc/" + signC + "?tgt=1&src=0&zh=" + src_text + "&xyz=" + teg_text + "&data_xh=" + data_xh + "&ywzql=&zh_update=" + src_text + "&updatexyz=" + teg_text
        while True:
            try:
                response = requests.get(url2, cookies=cookies).text
                data = json.loads(json.loads(response)["message"])

            except BaseException:
                print("异常")
                break
            src_text = data[0]
            teg_text = data[1]
            data_xh = data[3]
            print("条数:", data[4])
            print(src_text)
            print(teg_text)
            signB = False
            end_count = src_text.count("。")
            question_count = src_text.count("？")
            exclamation_count = src_text.count("！")

            if end_count <= 1 and question_count <= 1 and exclamation_count <= 1:  # 判断中文句子
                en_text = re.sub(r'[{}]+'.format(punctuation), '', teg_text)
                if not en_text.encode('UTF-8').isalpha():  # 判断是否是全英文
                    src_len = list(jieba.cut(re.sub(pattern, "", src_text)))
                    teg_len = re.split(pattern, teg_text)
                    if len(src_text) - len(teg_text) < 1:  # 判断长度
                        print("True")
                        signB = True
            if not signB:
                print("False")
                signC = "inaccuracy"
            time.sleep(1)
    except KeyboardInterrupt:
        break
