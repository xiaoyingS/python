#coding=UTF-8
from bs4 import BeautifulSoup
import re

class Dhttpparser(object):
   
    def _get_new_urls(self, soup):
        new_urls=set()
        links=soup.find_all('a',href=re.compile(r'https://book.douban.com/subject/\d+\/'),title=re.compile(r"."))
        if links is None:
            return
        for link in links:
            new_url=link['href']
            new_urls.add(new_url)
        return new_urls
                
    def _get_new_datas(self, soup, book_url):
        new_datas={}
        #<span property="v:itemreviewed">人生的枷锁</span>
        #书名
        new_datas['book_name']=soup.find('span',property='v:itemreviewed').string
        #<strong class="ll rating_num " property="v:average"> 9.0 </strong>
        #评分
        new_datas['book_score']=soup.find('strong',class_='ll rating_num ').string
        #<span>
        #<span class="pl"> 作者</span>:
        # <a href="/search/%E6%AF%9B%E5%A7%86">[英] 毛姆</a>
        #</span>
        #作者
        info = soup.find('div', id='info')
        new_datas['book_author'] = info.find(text=' 作者').next_element.next_element.string
        #书籍简介
        intro_datas=soup.find('div',class_='intro').strings
        new_datas['book_introduction']=''
        for string in intro_datas:
            new_datas['book_introduction']=new_datas['book_introduction']+str(string)
        #书籍url
        new_datas['book_url']=book_url
        
        return new_datas
      
    def parser(self,html_cont,url):        
        if html_cont is None:
            return
        soup=BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')        
        new_urls=self._get_new_urls(soup)
        return new_urls
           
    def book_parser(self,book_url,book_cont):
        if book_url is None or book_cont is None:
            return
        soup=BeautifulSoup(book_cont,'html.parser',from_encoding='utf-8')
        new_datas=self._get_new_datas(soup,book_url)
        return new_datas



