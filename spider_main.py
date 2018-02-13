# -*- coding: utf-8 -*-
"""
Created on Fri Feb 09 15:48:34 2018

@author: daozl1
"""
import url_manager,html_downloader,html_parser,html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        
    def craw(self,root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print "craw {0} : {1}".format(count,new_url)
                html_cont = self.downloader.download(new_url)
                urls,newdata = self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(urls)
                self.outputer.collect_data(newdata)
                if count == 100:
                    break
                count += 1
            except:
                print "craw failed"
                
        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python/407313"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
