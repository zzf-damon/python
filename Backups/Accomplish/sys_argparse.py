# -*-coding:utf-8-*-


# import sys
#
# gpus = sys.argv[1]
# # gpus = [int(gpus.split(','))]
# batch_size = sys.argv[2]
# print(gpus)
# print(batch_size)

import argparse
# theme 首先呢，argparse是一个\color{red}{命令行参数解析}模块！
parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--gpus', type=str, default=None, help="gpu")
parser.add_argument('--batch-size', type=int, default=32)
args = parser.parse_args()
print(args.gpus)
print(args.batch_size)
