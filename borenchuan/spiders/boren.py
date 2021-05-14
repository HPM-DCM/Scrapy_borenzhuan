import scrapy,re,sys
sys.path.append('..')
from borenchuan.items import BorenchuanItem
from bs4 import BeautifulSoup
from image_down import ImageDown
class BorenSpider(scrapy.Spider):
    name = 'boren'
    allowed_domains = ['www.36mh.net']
    host='https://www.36mh.net/'
    img_host='https://img001.microland-design.com/'
    start_urls = ['https://www.36mh.net/manhua/borenchuanhuoyingcishidai/'] #启动程序最开始爬的url

    '''博人传首页获取所有章节url'''
    def parse(self, response):
        chatlist=response.xpath('//*[@id="chapter-list-4"]/li') #存放在ul的所有章节
        for chat in chatlist:
            url=chat.xpath('./a/@href').extract()
            chatname=chat.xpath('./a/span/text()').extract()
            chaturl=self.host+url[0]
            #print(chatname,chaturl)
            yield scrapy.Request(chaturl,callback=self.parse2,meta={"chatname":chatname[0],"chaturl":chaturl})

    '''进入章节，从script拿到images的名称、和图片域名路径'''
    def parse2(self,response):
        resp=BeautifulSoup(response.text,'lxml').select('body script')[0].string
        img_list = re.findall(r'"(\w+.jpg)\\/0"', resp)  #漫画图片列表
        tmp_host=re.findall(r'var chapterPath = "(.*?)"',resp)[0]  #图片域名路径
        img_host=self.img_host+tmp_host  #https://img001.microland-design.com/images/comic/377/752993/
        items = BorenchuanItem()
        chatname = response.meta.get('chatname')
        cname=chatname.split(' ')[0]  #第1话

        imglist=[]  #图片顺序编号
        for img in img_list:
            img_url=r'%s%s\0' %(img_host,img)  #https://img001.microland-design.com/images/comic/377/752993/080c932ddd.jpg
            img_list.append(img_url)
        #items['imgpath']=cname
        #items['imgurl'] = imglist
        imgdown=ImageDown()
        imgdown.get_image(cname,imglist)