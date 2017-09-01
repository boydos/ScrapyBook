#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

class BookUtils:
    """for book db."""
    path = "/home/tongdongsheng/Desktop/小说"
    def __init__(self):
        pass
    def createBook(self,bookName):
        """创建文件夹"""
        if not bookName.strip():
            return ;
        if not os.path.exists(self.path):
            print "createBook ",self.path
            os.makedirs(self.path)
        try:
            os.mkdir(self.path +"/"+bookName)
        except IOError:
            print "文件创建失败"

    def createBookDetail(self,bookName,chapterName,content):
        """创建书籍章节详情"""
        if not bookName.strip() or not chapterName.strip():
            return ;
        bookName = bookName.encode('gb2312')
        chapterName =chapterName.encode('gb2312')
        self.createBook(bookName)
        filename = self.path+"/"+bookName+"/"+chapterName+".txt"
        with open(filename,'w') as file:
            file.write(chapterName+"\n")
            file.write(content.encode('gb2312').replace("<br/>","\n"))
