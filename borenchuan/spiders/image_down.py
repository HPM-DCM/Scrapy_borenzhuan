import ahttp
from borenchuan import settings
class ImageDown:
    def get_image(chpath,imageurls):
        print(chpath)
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}
        reqs=[ahttp.get(url,headers=head) for url in imageurls]
        reps=ahttp.run(reqs)
        for i,rep in enumerate(reps):
            filepath=r'%s\%s\%s.jpg' %(settings.IMAGES_STORE,chpath,i)
            print(rep)
            with open(filepath,'wb') as writer:
                writer.write(rep.content)