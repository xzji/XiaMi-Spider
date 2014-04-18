#-*-coding:utf-8-*-
#-----------------------------------
#   程序：虾米歌曲信息获取脚本
#   版本：V0.1
#   作者：Ji
#   日期：14-4-15
#   语言：python-2.7
#   操作：输入歌曲url，自动获取。quit退出
#   功能：歌曲信息获取
#   缺点：获取歌曲信息时不智能，譬如，某些歌曲的词，曲，编不一定都有。
#----------------------------------

import urllib
import urllib2
import re

#-----------加载处理歌曲信息----------------
class XiaMi_Spider:
    #申明相关属性
    def __init__(self,url):
        self.myUrl = url
        print u'已启动虾米爬虫，喀嚓喀嚓'

    #初始化提取信息    
    def xiami_info(self):
        #myPage = urllib2.urlopen(self.myUrl).read()
        headers = {
                'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
                }
        req = urllib2.Request(
                url = self.myUrl,
                headers = headers
                )
        myPage = urllib2.urlopen(req).read()
               #获取该歌曲的信息
        myItems_title = re.findall('<div id="title">.*?<h1>(.*?)</h1>',myPage,re.S)
        myItems_1 = re.findall(r'<td valign="top".*?><a href=".*?>(.*?)</a>',myPage,re.S)
        myItems_2 = re.findall(r'<td valign="top"><div title=.*?>(.*?)</div>',myPage,re.S)
        myItems_lrc = re.findall(r'<div class="lrc_main">(.*?)</div>',myPage,re.S)

        #print len(myItems_title)
        title = myItems_title[0]
        print '歌曲名称：'+ title 

        album = myItems_1[0]
        print '专辑:' + album 
        singer = myItems_1[1]
        print '演唱家：' + singer

        #print len(myItems_2)
        composer_1 = myItems_2[0]
        print '作词：' + composer_1
        composer_2 = myItems_2[1]
        print '作曲：' + composer_2
        
        #composer_3 = myItems_2[3]
        #print '编曲：' +composer_3

        #print len(myItems_lrc)
        lrc = myItems_lrc[0] 
        lrc = lrc.replace('<br />','')
        print '歌词' + lrc


        print u'请按任意键退出'
        raw_input()


    #def find_info(self,myPage):
     #   myMatch = re.search(r'<table id="albums_info.*?"><tr:><>')


#-----------加载处理歌曲信息----------------


#-----------程序入口处--------------------------
print """
#-----------------------------------
#   程序：虾米歌曲信息获取脚本
#   版本：V0.1
#   作者：Ji
#   日期：14-4-15
#   语言：python-2.7
#   操作：输入歌曲url，自动获取。quit退出
#   功能：歌曲信息获取
#----------------------------------
"""

print u'请输入要查找歌曲的url:'
xmurl = str(raw_input())

#调用
mySpider = XiaMi_Spider(xmurl)
mySpider.xiami_info()


