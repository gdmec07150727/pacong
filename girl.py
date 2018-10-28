import urllib.request
import os
import re

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()
    return html

def get_images(html):
    html = html.decode('utf-8')
    p = r'<img class="BDE_Image" src="([^"]+\.jpg)"'
    imglist = re.findall(p,html)
    return imglist

def save_imgs(folder,imglist):
    for each in imglist:
        filename = each.split('/')[-1]
        with open(filename,'wb') as f:
            img = url_open(each)
            f.write(img)
        # urllib.request.urlretrieve(each,filename)


if __name__ == '__main__':
    folder = "girl"
    os.mkdir(folder)
    os.chdir(folder)
    url = "https://tieba.baidu.com/p/5929210378"
    save_imgs(folder,get_images(url_open(url)))