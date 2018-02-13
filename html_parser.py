# -*- coding: utf-8 -*-
"""
Created on Fri Feb 09 16:41:26 2018

@author: daozl1
"""

from bs4 import BeautifulSoup
import re
import urlparse


class HtmlParser(object):
    
    def _get_urls(self,page_url,soup):
        new_urls = set()
        links = soup.find_all('a',href=re.compile(r'/item/*'))
        for link in links:
            new_url = link['href']
            #print "new_url",new_url
            new_url_full = urlparse.urljoin(page_url,new_url)
            #print "new_url_full",new_url_full
            new_urls.add(new_url_full)
        return new_urls
    
    def _get_data(self,page_url,soup):
        res_data = {}
        
        #url
        res_data['url'] = page_url
        
        #<dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()
        
        
        summary_node = soup.find('div',class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()
        
        return res_data
        
    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls = self._get_urls(page_url,soup)
        new_data = self._get_data(page_url,soup)   
        return new_urls,new_data

