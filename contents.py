import os
import sys


content_index = 0
file_index = 0
csv_path = None


def get_contents(path_name: str = None):

    if os.path.exists(path_name):
        sub_path_list = os.listdir(path_name)

        for sub_path in sub_path_list:
            path = path_name+sub_path
            if os.path.isdir(path):
                global content_index
                content_index = content_index+1
                item = str(content_index)+"," + "目录" + \
                    "," + sub_path+","+path_name
                with open(csv_path+"contents.csv", "a+", encoding='utf-8', newline='') as f:
                    f.write(item+"\r\n")
                get_contents(path_name=path+"/")

            if os.path.isfile(path):
                global file_index
                file_index = file_index+1
                item = str(file_index)+"," + "文件"+"," + sub_path+","+path_name
                with open(csv_path+"contents.csv", "a+", encoding='utf-8', newline='') as f:
                    f.write(item+"\r\n")

            if os.path.islink(path):
                pass

    else:
        print("该路径不存在：{}".format(path_name))


def main():
    global csv_path
    csv_path = "./"
    get_contents(
        path_name=csv_path
    )


if __name__ == "__main__":
    main()
