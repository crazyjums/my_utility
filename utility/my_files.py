# _*_ coding=utf-8
import os
import sys

sys.path.append(r"G:\software\pycharm\files\utility\my_files.py")

example = '''
##################### This is a example of my_files.py
1 rename_a_file(old_name="",new_name="A_new.txt")
usage: you can rename a file or a folder.
```
old_name = "1.txt"
new_anme = "2.txt"
rename_a_file(old_name,new_name)
# or 
old_name = "c:/folder1"
new_anme = "c:/folder2"
rename_a_file(old_name,new_name)
```

2 read_from_file_by_list(filename="",mode="r",encoding="utf8")
usage: you can use this function to read the data from file, and return a list of each line's data.
```
file_name = "test.txt" 
# test.txt's content:
## new one
## new two
## ...
## new five

info = read_from_file_by_list(file_name)
# info is a list, info:
# info = ['new one',...,'new five']
```

3 read_from_file_by_str(filename="",mode="r",encoding="utf8")
usage: this function also can read data from file, but return a str not a list.
```
file_name = "test.txt" 
info = read_from_file_by_str(file_name)
## info = "newonenewtwo...newfive"
```

4 write_into_file(filename="",encoding="utf-8",mode="w",content=None)
usage: you can use this function to write a string to file.
```
file_name = "readme.md"
content = "### title one ### title two ..."
write_into_file(filename=file_name,content=content)
```
###################################################
'''




def rename_a_file(old_name="", new_name="A_new.txt"):
    '''

    :param old_name: a file_name or a folder name
    :param new_name:
    :return: 对文件进行改名，如果指定绝对地址，将是对绝对地址进行改名，如果不指定，则是相对地址
    '''
    if old_name != "":
        if not os.path.exists(old_name):
            raise Exception("[{}] is not existed.".format(old_name))
        else:
            os.renames(old=old_name,new=new_name)
            print("rename {} to {} is done.".format(old_name,new_name))
    else:
        raise Exception("[filename] is null")

def read_from_file_by_list(filename="",mode="r",encoding="utf8"):
    '''

    :param filename:
    :param mode:
    :param encoding:
    :return: 返回的是一个list数据结构，将文件中的各行进行当成一个list元素存放在list中
    '''
    if filename != "":
        if not os.path.exists(filename):
            raise Exception("[{}] is not existed.".format(filename))
        else:
            with open(file=filename,mode=mode,encoding=encoding) as file:
                content = file.readlines()
                return content
    else:
        raise Exception("[filename] is null")

def read_from_file_by_str(filename="",mode="r",encoding="utf8"):
    '''

    :param filename:
    :param mode:
    :param encoding:
    :return: 返回文本中的字符，已经使用strip()进行“清洗”,不包括文件中的格式，只返回内容部分
    '''
    if filename != "":
        if not os.path.exists(filename):
            raise Exception("[{}] is not existed.".format(filename))
        else:
            with open(file=filename,mode=mode,encoding=encoding) as file:
                content = file.readlines()
                info = ""
                for each in content:
                    info += each.strip()
                return info
    else:
        raise Exception("[filename] is null")

def write_into_file(filename="",encoding="utf-8",mode="w",content=None):
    '''

    :param filename:
    :param encoding:
    :param mode:
    :param content:
    :return: 将指定的内容写入文件中
    '''
    if content is not None:
        with open(file=filename,mode=mode,encoding=encoding) as file:
            file.write(content)
    elif filename == "":
        filename = "files_1.txt"
        with open(file=filename,mode=mode,encoding=encoding) as file:
            file.write(content)
        print("running done.")
    else:
        raise Exception("[content] is None")

def write_list_into_file(filename="",encoding="utf-8",mode="w",content=None):
    '''

    :param filename:
    :param encoding:
    :param mode:
    :param content:
    :return: 将指定的内容写入文件中
    '''
    if content is not None:
        with open(file=filename,mode=mode,encoding=encoding) as file:
            for each in content:
                file.write(str(each))
                file.write("\n")
    elif filename == "":
        filename = "files_1.txt"
        with open(file=filename,mode=mode,encoding=encoding) as file:
            for each in content:
                file.write(str(each))
                file.write("\n")
        print("running done.")
    else:
        raise Exception("[content] is None")

# def get_dir_lists(dir=r"c:"):
#

if __name__ == '__main__':
    # t = read_text_from_file(r"g:\new1.txt")
    # print(t)
    rename_a_file(r"g:\test",r"g:\test2")
    # if os.path.exists(r"g:\test"):
    #     print("yes")