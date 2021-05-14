import ahttp
image_url=['https://img001.bolong-aterials.com/images/comic/393/784347/118a3133d9.jpg/0','https://img001.bolong-aterials.com/images/comic/393/784347/1111455a1d.jpg/0','https://img001.bolong-aterials.com/images/comic/393/784347/110fc320d0.jpg/0']
head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}
reqs=[ahttp.get(url,headers=head) for url in image_url]
responses=ahttp.run(reqs)
for i,resp in enumerate(responses):
    file='%s.jpg' %i
    print(resp)
    with open(file,'wb') as writer:
        writer.write(resp.content)