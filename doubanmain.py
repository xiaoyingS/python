#coding=UTF-8

from douban import d_urlmanagement, d_httpdownloader, d_httpparser,\
    d_httpoutputer

import time

class DoubanMain(object):
    def __init__(self):
        self.durls=d_urlmanagement.Durlmanagement()
        self.ddownload=d_httpdownloader.Dhttpdownloader()
        self.dparser=d_httpparser.Dhttpparser()
        self.doutputer=d_httpoutputer.Dhttpoutputer()
          
    def crow(self):        
        pag_num=0
        while(1):
            #https://book.douban.com/tag/小说?start=40&type=T
            try:
                url='https://book.douban.com/tag/小说'+'?start='+str(pag_num*20)+'&type=T'
                print '%d page'%pag_num
                time.sleep(0.1)
                html_cont=self.ddownload.download(url)
                
                new_urls=self.dparser.parser(html_cont,url)
                
                self.durls.add_new_urls(new_urls)
                
                while self.durls.has_new_url():
                    book_url= self.durls.get_new_url()
                    
                    time.sleep(0.1)
                    book_cont=self.ddownload.download(book_url)
                    
                    new_datas=self.dparser.book_parser(book_url,book_cont)
                    
                    self.doutputer.collectdata(new_datas)   
            except:
                print 'error'   
            pag_num = pag_num +1
            if pag_num >=100:
                break   
        self.doutputer.ouput()

if __name__=='__main__':
    
    douban=DoubanMain()
    douban.crow()
    
    
    