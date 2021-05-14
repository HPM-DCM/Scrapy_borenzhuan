# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy,os,re,sys
sys.path.append('..')
import borenchuan.settings as settings
from scrapy.pipelines.images import ImagesPipeline
#<img src="https://img001.microland-design.com/images/comic/377/752997/096118b420.jpg/0" data-index="1" style="">
#自增图片id
def append_chatp():
    inner_chatp = []
    inner_image = []
    def inner(chatp,i):
        if chatp  in inner_chatp:
            inner_image.append(i)
            images=len(i)
        else:
            inner_chatp.append(chatp)
            inner_image.clear()
            inner_image.append(i)
            images=len(i)
        return images
    return inner

class BorenchuanPipeline(object):
    def process_item(self, item, spider):
        return item

class BorenchuanImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # request_object=super().get_media_requests(item,info)
        # for request_obj in request_object:
        #     request_obj=item
        # return request_object
        for imageurl in item['imgurl']:
            yield scrapy.Request(imageurl,meta={"imagepath":item['imgpath']})


    def file_path(self, request, response=None, info=None):
        #path=super().file_path(request,response,info)
        #imgpath=request.item.get('imgpath')
        imgpath=request.meta['imgpath']
        filename=request.url.split('/')[-1]
        # filepath=os.path.join(settings.IMAGES_STORE,imgpath,filename)
        # if not os.path.exists(filepath):
        #     os.makedirs(filepath)
        newpath=u'%s/%s' %(imgpath,filename)
        print(newpath)
        return newpath