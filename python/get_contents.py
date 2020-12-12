import os

from collections import Counter

CNT = Counter()
CSV_PATH = "./"


def write(flag: str, path: str, sub_path: str, separator: str = "<=>"):
    CNT[flag] += 1
    item = f"{CNT[flag]}{separator}{flag}{separator}{sub_path}{separator}{os.path.abspath(path)}{separator}{os.path.splitext(sub_path)[-1][1:]}"
    f.write(item + "\r\n")


def get_contents(parent_path: str = None):
    if os.path.exists(parent_path):
        sub_path_list = os.listdir(parent_path)

        for sub_path in sub_path_list:
            path = parent_path + sub_path

            if os.path.isdir(path):
                write('dir', path, sub_path)
                get_contents(parent_path=path + "/")

            # elif os.path.isfile(path):
            else:
                write('file', path, sub_path)

    else:
        print("该路径不存在：{}".format(parent_path))


if __name__ == "__main__":
    with open(CSV_PATH + "contents.csv", "a+", encoding='utf-8', newline='') as f:
        get_contents(parent_path="./")
