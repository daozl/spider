# -*- coding: utf-8 -*-
"""
Created on Fri Feb 09 16:41:23 2018

@author: daozl1
"""

import urllib2

class HtmlDownloader(object):
    
    def download(self,url):
        if url is None:
            return None
        
        response = urllib2.urlopen(url)
        
        if response.getcode() != 200:
            print "exitcode = {}".format(response.getcode())
            return None
        return response.read()
    