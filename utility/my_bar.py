#coding=utf-8
import sys
import time

def print_progress(iteration, total, prefix='Start', suffix='Complete', decimals=1, barLength=30, s=time.time()):
    """
    Call in a loop to create a terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        barLength   - Optional  : character length of bar (Int)
    """
    formatStr = "{0:." + str(decimals) + "f}"
    percent = formatStr.format(100 * (iteration / float(total)))
    filledLength = int(round(barLength * iteration / float(total)))
    bar = '>' * filledLength + '-' * (barLength - filledLength)
    e = time.time()
    sys.stdout.write('\r%s |%s| %s%s %s/%s %s | %ss' % (prefix, bar, percent, '%', iteration, total, suffix, round(e-s,3))),
    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()





if __name__ == '__main__':
    pass
    long = 1000000
    for i in range(long):
        print_progress(i,long)

