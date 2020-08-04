import logging




logging.basicConfig(level=logging.INFO,
            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
            datefmt='%a, %d %b %Y %H:%M:%S',
            filename="./logging.txt",
            filemode='w'
            )  # 设置日志的输出文件

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info("this is a test")