import os
import requests
from urllib.error import  HTTPError

import threadpool
from bs4 import BeautifulSoup

# 壁纸网站根地址
base_url = 'http://www.netbian.com'

# 本地保存目录地址
root='./netbian/'

def getHtml(url):
    headers = {
        'Content-Type': 'text/html;charset=utf-8',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }
    resp = requests.get(url=url,headers=headers)
    if resp.status_code == 200 :
        return resp.text
    return ''

# 获取分页信息
def getPage(url):
    soup = BeautifulSoup(getHtml(url), "html.parser")
    a_pics = soup.find('div', id='main').find('div', class_='list').find_all('a')
    img_page_urls = []
    for a in a_pics :
        img_page_url = a['href']
        if not img_page_url.startswith('http'):
            img_page_urls.append(base_url+img_page_url)
        else:
            print("跳过广告链接："+img_page_url)
    # print(img_page_urls)
    return img_page_urls

def getImgUrl(url):
    soup = BeautifulSoup(getHtml(url),"html.parser")
    a = soup.find('div', class_='pic').find('a')
    img_url = base_url+a['href']
    return img_url

def downloadImage(url,title):
    path = root+title
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件[%s]保存成功" % title)
    else:
        print("文件已存在")

def getBigImgUrl(url):
    soup = BeautifulSoup(getHtml(url), "html.parser")
    a = soup.find('table', id='endimg').find('img')
    img_url = a['src']
    title = a['title'].replace(' ','')+'.'+img_url.split('.')[-1]
    downloadImage(img_url,title)


def run(url):
    print("%s-----------开始" % url)
    img_page_urls = getPage(url)
    for img_page_url in img_page_urls :
        img_url = getImgUrl(img_page_url)
        getBigImgUrl(img_url)
    print("%s-----------结束"  % url )
# 开始页码  爬多少页  线程数
def start(start,limit,threads=2):
    url = base_url + '/meinv'
    pageUrls = []

    #生成第start到start+limit页的url
    for index in range(start,start+limit):
        if not index == 1 :
            page_url = url+'/index_%d.htm' % index
        else:
            page_url = url+''
        pageUrls.append(page_url)

    task_pool = threadpool.ThreadPool(threads)
    requestss = threadpool.makeRequests(run,pageUrls)
    for req in requestss :
        task_pool.putRequest(req)
    task_pool.wait()

if __name__ == '__main__':
    ## 80
    start(1,1,1)

