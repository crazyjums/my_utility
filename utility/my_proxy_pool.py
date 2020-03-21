# _*_ coding=utf-8
from bs4 import BeautifulSoup as bs
from utility import my_html,my_fake_ua,my_decorator
from utility import my_files,my_bar
import sys,io
import requests,time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="gb18030")
sys.path.append(r"G:\software\pycharm\files\utility\my_proxy_pool.py")

free_proxy_urls = ["http://www.data5u.com/free/index.html",
        "http://www.66ip.cn/",
        "http://www.xicidaili.com/",
        "http://www.goubanjia.com/",
        "http://www.xdaili.cn/",
        "https://www.kuaidaili.com/",
        "http://www.ip3366.net/",
        "http://www.iphai.com/",
        "http://ip.jiangxianli.com/",
        "http://cn-proxy.com/",
        "https://proxy-list.org/chinese/index.php",
        "https://list.proxylistplus.com/Fresh-HTTP-Proxy-List-1"
        ]

def get_proxy_pool():
    url = "http://www.66ip.cn/"
    # soup = my_html.get_soup_from_url(url=url, encoding="gbk")
    # soup = requests.get(url).content.decode("gbk")
    # soup = my_html.get_soup_from_str(soup)
    # max_page = my_html.select_element_by_id(soup=soup, element="div", types_name="PageList", types="id")
    # print(max_page)
    r = requests.get(url=url, headers=my_fake_ua.get_user_agent())
    soup = bs(r.text,"html.parser")
    print(soup)


@my_decorator.ShowRunningTime
def get_ip_list_from_xici():
    ip_list = []
    url = 'http://www.xicidaili.com/nn/'
    proxies = {"http":"http://195.239.178.110:33246"}
    soup = my_html.get_soup_from_url_by_text(url, proxies=proxies)
    time.sleep(5)

    ### get max page number
    max_page = soup.select("div[class='pagination']")[0].find_all("a")
    max_page = max_page[-2]
    max_page = max_page.string
    ######

    ### get the first page's ip list
    _ip_lists = soup.select("table[id='ip_list']")
    trs = _ip_lists[0].find_all("tr")
    for tr,j in zip(trs,range(2,len(trs) + 1)):
        data = tr.find_all("td")
        if len(data) != 0:
            ip_code = data[1].string
            port = data[2].string
            place = data[3].find("a").string
            is_anonymous = data[4].string
            types = data[5].string
            live_time = data[-2].string
            validate_time = data[-1].string
            #
            _ = [ip_code,port,place,is_anonymous,types,live_time,validate_time]
            ip_list.append(_)
        else:
            pass

    ### start with page 2
    for page in range(2, int(max_page) + 1):
        _url = url + str(page)
        _soup = my_html.get_soup_from_url_by_text(_url)
        _ip_lists = soup.select("table[id='ip_list']")
        trs = _ip_lists[0].find_all("tr")
        for tr, j in zip(trs, range(2, len(trs) + 1)):
            data = tr.find_all("td")
            if len(data) != 0:
                ip_code = data[1].string
                port = data[2].string
                place = data[3].find("a").string
                is_anonymous = data[4].string
                types = data[5].string
                live_time = data[-2].string
                validate_time = data[-1].string
                _ = [ip_code, port, place, is_anonymous, types, live_time, validate_time]
                ip_list.append(_)
                my_files.write_list_into_file(filename="./proxy_pool/xici.json", content=ip_list, mode="a")
            else:
                pass
        time.sleep(5)

    return ip_list


@my_decorator.ShowRunningTime
def get_ip_list_from_66ip(page_num):

    ip_list = []
    url = "http://www.66ip.cn/"
    soup = my_html.get_soup_from_url(url, encoding="gb18030")
    max_page = soup.select("div[id='PageList']")[0].find_all("a")
    max_page = max_page[-2]
    max_page = max_page.string

    ### get first page
    trs = soup.find_all("tr")
    # print(trs)
    for tr in trs[2:]:
        data = tr.find_all("td")
        # print(data)
        ip_code = data[0].string
        port = data[1].string
        place = data[2].string
        types = data[3].string
        validate_time = data[-1].string
        ip_list.append([ip_code,port,place,types,validate_time])


    for page in range(int(page_num) + 1):
        _url = "http://www.66ip.cn/{}.html".format(str(page))
        _soup = my_html.get_soup_from_url(url=_url, encoding="gb18030")
        _trs = soup.find_all("tr")
        # print(trs)
        for tr in _trs[2:]:
            _data = tr.find_all("td")
            # print(data)
            _ip_code = _data[0].string
            _port = _data[1].string
            _place = _data[2].string
            _types = _data[3].string
            _validate_time = _data[-1].string
            ip_list.append([_ip_code, _port, _place, _types, _validate_time])
            my_files.write_list_into_file(filename="./proxy_pool/ip66.json", content=ip_list, mode="a")
        # break
        my_bar.print_progress(prefix="ip66", total=page_num, iteration=page)
    # print(ip_list)
    # print(len(ip_list))
    return ip_list

if __name__ == '__main__':
    # get_ip_list_from_xici()
    # ip_list = get_ip_list_from_66ip(100)
    # with open("ip66.json","r",encoding="utf-8") as file:
    #     print(file.readline())
    s = time.time()
    for i in range(1003330):
        e = time.time()
        sys.stdout.write("\r"+str(round(e-s,3)) + "s")
    sys.stdout.flush()





