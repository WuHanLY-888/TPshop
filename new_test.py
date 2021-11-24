import requests

from lxml import etree
from requests.api import head
headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44"
}
def get_pic(url):
    return requests.get(url,headers=headers).content

url='http://www.tp-linkshop.com.cn/ProductImg540/1729.png'
pic=get_pic(url)

with open("images\\pic.png","wb") as f:
    f.write(pic)
# url1=['http://www.tp-linkshop.com.cn/ProductImg540/1729.png','http://www.tp-linkshop.com.cn/ProductImg540/1729_1.jpg','http://www.tp-linkshop.com.cn/ProductImg540/1729_2.jpg','http://www.tp-linkshop.com.cn/ProductImg540/1729_3.jpg','http://www.tp-linkshop.com.cn/ProductImg540/1729_4.jpg']
# print(len(url1))
