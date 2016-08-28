#coding=UTF-8
import xlwt
class Dhttpoutputer(object):
    def __init__(self):
        self.datas=[]
    
    def ouput(self):
        work=xlwt.Workbook(encoding='utf-8')
        sheet=work.add_sheet(u'sheet')
        sheet.write(0,0,'书名')
        sheet.write(0,1,'作者')
        sheet.write(0,2,'评分')
        sheet.write(0,3,'简介')
        sheet.write(0,4,'url')
        n=1
        for data in self.datas:
            sheet.write(n,0,data['book_name'].encode('utf8'))
            sheet.write(n,1,data['book_author'].encode('utf8'))
            sheet.write(n,2,data['book_score'])
            sheet.write(n,3,data['book_introduction'].encode('utf8'))
            sheet.write(n,4,data['book_url'].encode('utf8'))
            n=n+1
        work.save(u'douban.xls'.encode('utf8'))
        '''
		#html形式输出
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

    '''
    def collectdata(self,data):
        if data is None:
            return
        self.datas.append(data)
        
    
    
    