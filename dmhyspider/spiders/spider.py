from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
import bs4
from dmhyspider import items
from scrapy_splash import SplashRequest
import re


class animespider(CrawlSpider):
    name="dmhyspider"
    start_urls = ["http://dmhy.org/topics/list/page/"]
    main_url="http://dmhy.org"
    page=1 #最大爬取页数
    def start_requests(self):
        for i in range(1,self.page+1):
            print("start to request:"+self.start_urls[0]+str(i))
            yield Request(url=self.start_urls[0]+str(i),callback=self.parser,dont_filter=True)

    def parser(self,response):
        soup=bs4.BeautifulSoup(response.text,"lxml")
        item_result=soup.select("td.title")
        for item in item_result:
            url=self.main_url+self.getitemurl(item)
            yield Request(url=url,callback=self.item_parser,dont_filter=True)
    #item解析
    def item_parser(self,response):
        soup=bs4.BeautifulSoup(response.text,"lxml")
        item=items.DmhyspiderItem()
        item["name"]=soup.select_one("h3").string
        urls={}
        #会员连接
        urls["member_url"]=soup.select_one("#tabs-1 > p:nth-of-type(1) > a ")["href"]
        #磁链1
        urls["magenet1"] = soup.select_one("#a_magnet")["href"]
        #磁链2
        urls["magenet2"] = soup.select_one("#magnet2")["href"]
        #弹幕url
        urls["danmu_url"] = soup.select_one("#ddplay")["href"]
        item["urls"]=urls
        yield item
        pass
    def getitemurl(self,item):
        a=item.find("a",{"href": re.compile(".*\.html")})
        return a["href"]



