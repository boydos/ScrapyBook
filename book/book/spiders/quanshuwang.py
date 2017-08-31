# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from book.items import BookItem,BookType

class QuanshuwangSpider(scrapy.Spider):
    name = 'quanshuwang'
    allowed_domains = ['www.quanshuwang.com']
    start_urls = ['http://www.quanshuwang.com/']

    def parse(self, response):

        print "书籍爬虫..."
        for li in response.xpath('//ul[@class="channel-nav-list"]/li'):
            title = li.xpath("a/text()").extract_first()
            link = li.xpath("a/@href").extract_first()
            print "title",title,"link",link
            yield Request(url=link,meta={'type':title.encode("utf-8")},callback=self.parse_by_type)

    def parse_by_type(self,response) :
        """"根据分类进行解析书籍列表 """
        booktype = response.meta["type"]
        print "正在爬取分类...[",booktype,"]\n"
        #links = response.xpath("//section/ul[@class='seeWell cf']/li/a/@href").extract()
        #imgs = response.xpath("//section/ul[@class='seeWell cf']/li/a/img/@src").extract()
        #titles = response.xpath("//section/ul[@class='seeWell cf']/li/span/a[1]/text()").extract()
        #authors = response.xpath("//section/ul[@class='seeWell cf']/li/span/a[2]/text()").extract()
        #readlinks = response.xpath("//section/ul[@class='seeWell cf']/li/span/a[3]/@href").extract()
        bookMeta ={}
        for li in response.xpath("//section/ul[@class='seeWell cf']/li") :
            bookMeta["title"] = li.xpath("span/a[1]/text()").extract_first().encode("utf-8")
            bookMeta["type"] = booktype
            bookMeta["author"] = li.xpath("span/a[2]/text()").extract_first().encode("utf-8")
            bookMeta["img"] = li.xpath("a/img/@src").extract_first()
            bookMeta["link"] = li.xpath("a/@href").extract_first()
            yield Request(url=bookMeta["link"],meta=bookMeta,callback=self.parse_book_read)
    def parse_book_read(self,response) :
        "书籍中转...可以获得详细简介"
        bookMeta = response.meta
        bookMeta["des"] = response.xpath("//div[@class='detail']//div[@id='waa']/text()").extract_first().encode("utf-8")
        bookMeta["status"] = response.xpath("//div[@class='detail']//div[@class='bookDetail']/dl[1]/dd/text()").extract_first().encode("utf-8")
        bookMeta["link"] =response.xpath("//div[@class='detail']//div[@class='b-oper']/a[@class='reader']/@href").extract_first()
        print bookMeta["title"],"\n"
        print "小说状态",bookMeta["status"],"\n"
        print "简介:",bookMeta["des"],"\n"
        yield Request(url=bookMeta["link"],meta=bookMeta,callback=self.parse_book)
    def parse_book(self,response) :
        "书籍详情列表,章节获取"
        print "章节获取...."
        bookMeta = response.meta
        for li in response.xpath("//div[@class='chapterNum']/ul/div[@class='clearfix dirconone']/li"):
            chapterName = li.xpath("a/text()").extract_first().encode("utf-8")
            chapterUrl = li.xpath("a/@href").extract_first()
            print chapterName,"连接:",chapterUrl

    def parse_book_chapter(self,response) :
        "书籍具体章节详情"
        bookMeta = response.meta
        print response.xpath("//div[@id='content']").extract_first().encode("utf-8")
