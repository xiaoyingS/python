#coding=UTF-8

class Dhttpoutputer(object):
    def __init__(self):
        self.datas=[]
    
    def ouput(self):
        fount=open('douban.html','w')
        fount.write('<html>')
        fount.write('<meta http_equiv="Content-Type" content="text/html" charset="utf-8">')
        fount.write('<body>')
        fount.write('<table>')
        for data in self.datas:
            fount.write('<tr>')
            fount.write('<td>%s</td>'%data['book_name'].encode('utf8'))
            fount.write('<td>%s</td>'%data['book_score'])
            fount.write('<td>%s</td>'%data['book_author'].encode('utf8'))
            fount.write('<td>%s</td>'%data['book_introduction'].encode('utf8'))
            fount.write('<td>%s</td>'%data['book_url'].encode('utf8'))
            fount.write('</tr>')
        fount.write('</table>')
        fount.write('</body>')
        fount.write('</html>')
        fount.close()

    
    def collectdata(self,data):
        if data is None:
            return
        self.datas.append(data)
        
    
    
    