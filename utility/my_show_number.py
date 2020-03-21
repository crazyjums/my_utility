# _*_ coding=utf8



def get_standard_cn_str(num):
    '''

    :param num:
    :return: show like this, show_standard_cn(1000123) --> output:100W
    input data is a int type data, and return a str type data for show.
    '''
    if isinstance(num, int):
        if num < 10000:
            return str(num)
        elif num >= 10000 and num < 100000:
            _num = str(num)
            index = len(_num) - 4
            before_point = _num[:-4]
            after_point = _num[index]
            if int(_num[index + 1]) >= 5:
                pass
            info = before_point + "." + after_point + "W"
            return info
        elif num >= 100000 and num < 1000000:
            _num = str(num)
            before_point = _num[:-4]
            after_point = _num[2]
            info = before_point + "." + after_point + "W"
            return info
        elif num >= 1000000 and num < 10000000:
            _num = str(num)
            before_point = _num[:-4]
            after_point = _num[3]
            info = before_point + "." + after_point + "W"
            return info
        elif num >= 10000000 and num < 100000000:
            _num = str(num)
            before_point = _num[:-4]
            after_point = _num[4]
            info = before_point + "." + after_point + "W"
            return info
        elif num >= 100000000 and num < 1000000000:
            _num = str(num)
            before_point = _num[:-8]
            after_point = _num[1]
            info = before_point + "." + after_point + "YI"
            return info
        elif num >= 1000000000 and num < 10000000000:
            _num = str(num)
            before_point = _num[:-8]
            after_point = _num[2]
            info = before_point + "." + after_point + "YI"
            return info
        elif num >= 10000000000 and num < 100000000000:
            _num = str(num)
            before_point = _num[:-8]
            after_point = _num[3]
            info = before_point + "." + after_point + "YI"
            return info
        elif num >= 100000000000:
            _num = str(num)
            if len(_num) == 13:
                before_point = _num[0]
                after_point = _num[1]
            elif len(_num) == 14:
                return num
            info = before_point + "." + after_point + "WanYI"
            return info






if __name__ == '__main__':
    print(get_standard_cn_str(34500900010000))