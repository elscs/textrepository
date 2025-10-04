import urllib.request
from lxml import etree
def create_request(page,author):
    url="https://yande.re/post?page="+str(page)+"&tags="+author
    header={'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'}
    request=urllib.request.Request(url=url,headers=header)
    return request
def get_content(request):
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    return content
def down_load(content,page,directory):
    tree=etree.HTML(content)
    htref_list=tree.xpath('//a[@class="directlink largeimg"]/@href')
    for i in range(len(htref_list)):
        hrtef=htref_list[i]
        urllib.request.urlretrieve(url=hrtef,filename=rf'D:\ACG\画集\{directory}\page='+str(page)+'picture='+str(i)+'.jpg')
if __name__ == '__main__':
    author=input("作者")
    directory=input("文件夹名")
    startpage=int(input("开始页数"))
    endpage=int(input("结束页数"))
    for page in range(startpage,endpage+1):
        request=create_request(page,author)
        content=get_content(request)
        down_load(content,page,directory)