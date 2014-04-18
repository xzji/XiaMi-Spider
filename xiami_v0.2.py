#-*-coding:utf-8-*-
#-----------------------------------
#   程序：虾米歌曲信息获取脚本
#   版本：V0.2
#   作者：Ji
#   日期：14-4-17
#   语言：python-2.7
#   操作：输入歌曲url，自动获取。quit退出
#   功能：歌曲信息获取
#   缺点：获取歌曲信息时不智能，譬如，某些歌曲的词，曲，编不一定都有。
#   改进：获取信息时智能判断是否存在
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
        #模拟浏览器请求头，来访问虾米网站
        headers = {
                'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
                }
        req = urllib2.Request(
                url = self.myUrl,
                headers = headers
                )
        myPage = urllib2.urlopen(req).read()
        #获取该歌曲的信息
        #歌曲信息的标题（0-专辑，1-歌手，2-作词，3-作曲，4-编曲）
        myItems_infotitle = re.findall('<.*?class="item".*?>(.*?)</td>',myPage,re.S)
        #歌曲名
        myItems_title = re.findall('<div id="title">.*?<h1>(.*?)</h1>',myPage,re.S)
        #歌曲的专辑和歌手
        myItems_1 = re.findall(r'<td valign="top".*?><a href=".*?>(.*?)</a>',myPage,re.S)
        #歌曲的作词，作曲，编曲
        myItems_2 = re.findall(r'<td valign="top"><div title=.*?>(.*?)</div>',myPage,re.S)
        #歌曲的歌词
        myItems_lrc = re.findall(r'<div class="lrc_main">(.*?)</div>',myPage,re.S)

        #歌曲名称
        if myItems_title:
            title = myItems_title[0]
            print '歌曲名称：'+ title
        else:
            print '歌曲名称：暂无'
        #歌曲专辑
        if myItems_1[0]:
            album = myItems_1[0]
            albumName = myItems_infotitle[0]
            print albumName + album 
        else:
            print albumName + '暂无'
        #歌曲演唱者
        if myItems_1[1]:
            singer = myItems_1[1]
            singerName = myItems_infotitle[1]
            print singerName +singer
        else:
            print singerName + '暂无'
        #print len(myItems_2)
        #歌曲作词
        if len(myItems_2)>=1:
            composer1 = myItems_2[0]
            composer1Name = myItems_infotitle[2]
            print  composer1Name + composer1
        else:
            print '作词：暂无'
        #歌曲作曲
        if len(myItems_2)>=2:
            composer2 = myItems_2[1]
            composer2Name = myItems_infotitle[3]
            print composer2Name + composer2
        else:
            print '作曲：暂无'
        #歌曲编曲
        if len(myItems_2)>=3:
            composer3 = myItems_2[2]
            composer3Name = myItems_infotitle[4]
            print composer3Name + composer3
        else:
            print '编曲：暂无'
        #歌曲歌词
        lrc = myItems_lrc[0] 
        lrc = lrc.replace('<br />','')
        print '歌词:' + lrc


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


