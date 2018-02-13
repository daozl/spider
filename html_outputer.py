# -*- coding: utf-8 -*-
"""
Created on Fri Feb 09 16:41:42 2018

@author: daozl1
"""
import xlsxwriter as wx
import time

class HtmlOutputer(object):
    
    def __init__(self):
        self.datas = []
        self.count = 1
        
    
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)
    
    def output_html(self):
        releaseDate = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        workbook = wx.Workbook("output{}.xlsx".format(releaseDate))
        
        sheet = workbook.add_worksheet('baike')
        
        sheet.set_column('A:A', 40)
        sheet.set_column('B:B', 15)
        sheet.set_column('C:C', 120)
       
        #worksheet1.set_row(0, 35)
        titleFormat = workbook.add_format(
        {'font_name': 'Verdana', 'font_color': '#4F5055', 'bg_color': '#E0E0E0',
         'font_size': 9,'bold': 1, 'top': 1,'left': 1, 'right': 1, 'bottom': 1})
    
        textFormat = workbook.add_format(
        {'font_name': 'Verdana', 'font_color': '#800000', 'font_size': 8, 'top': 1, 
         'left': 1, 'right': 1, 'bottom': 1})
    
        sheet.write("A1", "url", titleFormat)
        sheet.write("B1", "title", titleFormat)
        sheet.write("C1", "summary", titleFormat)
        
        
        for data in self.datas:
            self.count += 1
            sheet.write("A{}".format(self.count),data['url'],textFormat)
            sheet.write("B{}".format(self.count),data['title'],textFormat)
            sheet.write("C{}".format(self.count),data['summary'],textFormat)
        
        workbook.close()
       
        
        
        
    
