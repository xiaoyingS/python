#coding=UTF-8
import urllib2

class Dhttpdownloader(object):
    def download(self,url):
        if url is None:
            return None
        try:
            request=urllib2.Request(url)
            request.add_header('User-Agent','Mozilla/5.0' )
            response=urllib2.urlopen(request)
        except urllib2.URLError,e:
            if hasattr(e,'code'):
                print e.code
            if hasattr(e,'reason'):
                print e.reason
        if response.getcode()!=200:
            return None
        return response.read()
    
        
    
    



