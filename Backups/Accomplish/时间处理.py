from datetime import datetime, timedelta
import re

# 日期格式话模版

# 获取当前时间
today = datetime.today()
today1 = datetime.now()
print(today)
print(today1)
# 格式化输出
format_today = today.strftime("%Y-%m-%d %H:%M:%S")
print(format_today)


def date_compare(start_date: str, end_date: str, pattern: bool) -> timedelta:
    """
    日期比较
    :param start_date: 开始时间
    :param end_date: 结束时间
    :param pattern: 选择比较格式，True 有时间精确到秒  False 没有时间 不需要精确到秒
    :return:相距时间
    """
    format_pattern1 = "%Y-%m-%d %H:%M:%S"
    format_pattern2 = "%Y-%m-%d"
    difference = (datetime.strptime(end_date, format_pattern1) - datetime.strptime(start_date, format_pattern1)) \
        if pattern else (datetime.strptime(end_date, format_pattern2) - datetime.strptime(start_date, format_pattern2))
    return difference


def date_format(date_time: str) -> datetime:
    # 02月17日 18:03
    date_time = "02月17日 18:03"
    date, time = date_time.split(" ")
    date = re.sub("[年月日/]", "-", date)
