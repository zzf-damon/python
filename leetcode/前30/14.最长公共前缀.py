import random
import string

list_f = ["flower", "flow", "flight"]
list_d = ["dog", "racecar", "car"]
list_a = ["aa","a"]

def get_list_a_z():
    s = string.ascii_lowercase  # 小写
    # s = string.ascii_uppercase  # 大写
    s1 = string.ascii_letters  #
    r = random.choice(s)
    print(r)


def longestCommonPrefix(strs) -> str:
    long_str = strs[0] if len(strs) > 0 else ""
    for str in strs:
        pre = 0
        while pre < len(long_str) and pre < len(str):
            if str[pre] == long_str[pre]:
                pre += 1
            else:
                long_str = str[:pre]
                break
        long_str = long_str[:len(str)]
    print(long_str)
    return long_str


# get_list_a_z()
longestCommonPrefix(list_a)
