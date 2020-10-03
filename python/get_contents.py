import os

from collections import Counter

cnt = Counter()

csv_path = "./"
f = open(csv_path + "contents.csv", "a+", encoding='utf-8', newline='')


def get_contents(parent_path: str = None):
    def write(flag: str, path: str, sub_path: str):
        cnt[flag] += 1
        item = f"{cnt[flag]}<=>{flag}<=>{sub_path}<=>{os.path.abspath(path)}<=>{os.path.splitext(sub_path)[-1][1:]}"
        f.write(item + "\r\n")

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
    get_contents(parent_path="./")
    f.close()
