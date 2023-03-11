#! /usr/bin/env python3
# Purpose : Say hello

import argparse


def get_args():
    parser = argparse.ArgumentParser(description='Say hello')  # description : 도움말로 표시
    # -n, --name : 축약형(short)과 일반형(long)
    # metavar : 인수명
    # default : 기본값
    parser.add_argument('-n', '--name', metavar='name', default='World', help='Name to greet')
    return parser.parse_args()


def main():
    args = get_args()

    # 목적 : 인사하기
    print('Hello, ' + args.name + '!')


if __name__ == '__main__':
    main()
