# _*_ coding=utf8
import requests
from bs4 import BeautifulSoup as bs
from utility import my_fake_ua




headers = my_fake_ua.get_user_agent()

example = '''
############## This is a example of my_html.py
1 load_text_from_html(url="",method="get",data={},encoding="utf8")
usage: you can use this function to download a url's text, and the function will return a type of str, named text for you.
```
url = "http(s)://example.com"
# if you want to change the parma, you can DIY it.
text = load_text_from_html(url=url, method="get", encoding="gb2312")
print(text)
```

2 get_soup_from_url(url="", method="get", encoding="utf8")
usage: you can use this function to get a soup that type of BeautifulSoup from the web, and you need the internet connected.
```
url = "http(s)://example.com"
soup = get_soup_from_url(url)
soup.select(...)

```

3 get_soup_from_str(text="")
usage: you can also get a soup, but from text(type of str), the same result of get_soup_from_url
```
url = "http(s)://example.com"
text = load_text_from_html(url) # or text = "<html>...</html>"
soup = get_soup_from_str(text)
soup.select(...)
```

4 get_status_code(url)
usage: you can get a status_code of the url.
```
url = "http(s)://example.com"
status_code = get_status_code(url)
```

5 select_element_by_id(soup=None, element="div", types="class", types_name="")
usage: this function is the BeautifulSoup.select()
```
soup = bs(content, "lxml")
hrefs = select_element_by_id(soup, "a", "class", "my-href") 
# hrefs  is list
```

##############################################
'''

code = '''
code type: 
     chinese:gb2312<gbk<gb18030
     global:utf-8
'''

def load_text_from_html(url="",method="get",data={},encoding="utf8", cookies=None, proxies={}):
    if url != "":
        if method == "get":
            resp = requests.get(url=url, headers=my_fake_ua.get_user_agent(), cookies=cookies, proxies=proxies)
            text = resp.content.decode(encoding=encoding)
            return text
        elif method == "post":
            resp = requests.post(url=url, data=data, headers=headers, cookies=cookies, proxies=proxies)
            text = resp.content.decode(encoding=encoding)
            return text
    else:
        raise Exception("[url] is null.")

def get_soup_from_url(url="", method="get", encoding="utf8", cookies=None, data={}, proxies={}):
    if url != "":
        if method == "get":
            resp = requests.get(url=url, headers=headers, cookies=cookies, proxies=proxies)
            text = resp.content.decode(encoding)
            try:
                # print("runnnn")
                soup = bs(text, "lxml")
                return soup
            except UnicodeEncodeError as e:
                print("error-->", e)
            return soup
        elif method == "post":
            resp = requests.post(url=url, data=data, headers=headers, cookies=cookies, proxies=proxies)
            text = resp.content.decode(encoding)
            try:
                # print("runnnn")
                soup = bs(text, "lxml")
                return soup
            except UnicodeEncodeError as e:
                print("error-->", e)
            return soup
    else:
        raise Exception("[url] is null.")

def get_soup_from_url_by_text(url="", method="get", encoding="utf8", proxies={}, cookies=None, data={}):
    if url != "":
        if method == "get":
            resp = requests.get(url=url, headers=headers, cookies=cookies, proxies=proxies)
            text = resp.text
            try:
                # print("runnnn")
                soup = bs(text, "lxml")
                return soup
            except UnicodeEncodeError as e:
                print("error-->", e)
            return soup
        elif method == "post":
            resp = requests.post(url=url, data=data, headers=headers, cookies=cookies, proxies=proxies)
            text = resp.text
            try:
                # print("runnnn")
                soup = bs(text, "lxml")
                return soup
            except UnicodeEncodeError as e:
                print("error-->", e)
            return soup
    else:
        raise Exception("[url] is null.")

def get_soup_from_str(text=""):
    if text != "":
        soup = bs(str(text),"html.parser")
        return soup
    else:
        raise Exception("[text] is null.")

def get_status_code(url):
    if url != "":
        resp = requests.get(url=url, headers=my_fake_ua.get_user_agent())
        status_code = resp.status_code
        return status_code
    else:
        raise Exception("[url] is null.")

def select_element_by_id(soup=None, element="div", types="class", types_name=""):
    '''

    :param soup:
    :param element:
    :param types:
    :param types_name:
    :return: return a list data struct, select all matched information from the soup.
    '''
    if soup is not None:
        if types_name != "":
            result = soup.select("{}[{}={}]".format(element,types,types_name))
            return result
        else:
            raise Exception("[types_name] is None.")
    else:
        raise Exception("[soup] is None.")


if __name__ == '__main__':
    url = "https://jums.club"

