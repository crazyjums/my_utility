import time
from functools import wraps
import logging

# def log(func):
#     @wraps(func)
#     def wrap(*args,**kwargs):
#         res_list = []
#         t = time.ctime()
#         t_str = t.split(" ")
#         show_t = "{}-{}-{} {}".format(t_str[-1], t_str[1], t_str[3], t_str[4])
#         file_name = "{}_{}_{}_logging.log".format(t_str[-1], t_str[1], t_str[3])
#         s_time = time.time()
#         res = func(*args,**kwargs)
#         e_time = time.time() - s_time
#         args = [arg for arg in args]
#         print(args)
#         l = "[{}]{}({})->{}".format(show_t,func.__name__,args[0] if args is not None else "null",res)
#         if l not in res_list:
#             res_list[l] = 1
#         else:
#             res_list[l] = res_list[l] + 1
#         args_str = ",".join(repr(arg) for arg in args)
#         info = "[DEBUG][{}](%0.9fs)|{}({})->{}".format(show_t,func.__name__,args_str,res) % round(float(e_time),9)
#         print(info)
#         with open("{}.txt".format(file_name),"a") as file:
#             file.write(info + "\n")
#         return res
#     return wrap


def my_log(level="info"):
    def log(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            args_list = []
            for arg in list(args):
                args_list.append(arg)
            print("args:",args_list)
            kwargs_list = []
            for k,v in kwargs.items():
                print(k,v)
            #     # kwargs_list.append(v)
            # # print(kwargs_list)
            print("Level-Function-datatime")
            if level == "info":
                return_info = func(*args, **kwargs)
                print("[{}]-{}-{}".format(level,func.__name__,time.ctime()))
            elif level == "debug":
                return_info = func(*args, **kwargs)
                print("[{}]-{}-{}".format(level, func.__name__, time.ctime()))
            # print("{}".format(func.__name__))
            # print(return_info)
            return return_info
        return wrapper
    return log


def show_time(func):
    '''

    :param func:
    :return: calcuate the func running time
    '''
    @wraps(func)
    def wrapper(*args, **kw):
        # print("************function_name:[{}] is rnnning now...".format(func.__name__))
        before = time.time()
        return_info = func(*args, **kw)
        after = time.time()
        print("func :[{}] running time: {}s".format(func.__name__,str(round(after - before, 3))))
        # print("************function_name:[{}] is done.".format(func.__name__))
        return return_info
    return wrapper

class ShowRunningTime():
    def __init__(self,func):
        self.func = func

    def __call__(self, *args, **kwargs):
        before = time.time()
        return_info = self.func(*args, **kwargs)
        after = time.time()
        print("function:[{}] running time: {}s".format(self.func.__name__, str(round(after - before, 3))))
        # print("return info: {}".format(return_info))
        return return_info


def show_time_bar_in_commang_line(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        before = time.time()
        return_info = func(*args, **kwargs)
        after = time.time()
        sys.stdout.write("{}".format(after-before))
        sys.stdout.flush()
        return return_info
    return wrapper

@show_time_bar_in_commang_line
def test(nihao, sum=0, a=1, b=2, c=3):
    # sum = 0
    for i in range(100000000):
        sum += i
    return sum



if __name__ == '__main__':
    sum = test("woshoshihsi",a=2,c=3)
    print(sum)