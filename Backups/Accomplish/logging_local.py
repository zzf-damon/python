import logging



# # # # def main(logfile_path):
# logging.basicConfig(level=logging.INFO,
#             format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#             # datefmt='%a, %d %b %Y %H:%M:%S',
#             # filename=logfile_path,
#             filemode='w'
#             )  # 设置日志的输出文件



logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
logger.setLevel(logging.INFO)

# 在其他文件中只需要 引入这个文件中的looger即可
for i in range(4):
    # fh = logging.FileHandler("./test"+str(i)+".txt")
    # 指定logger输出格式
    # formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')

    # 文件日志
    file_handler = logging.FileHandler("./test"+str(i)+".txt",mode='w', encoding="utf-8")
    file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式
    logger.addHandler(file_handler)
    logger.info("this ia 啊")
    logger.warning("that is 吧")
    logger.removeHandler(file_handler)