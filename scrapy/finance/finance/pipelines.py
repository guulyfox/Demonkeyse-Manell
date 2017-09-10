# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FinancePipeline(object):
    def __int__(self):
        dbargs = dict(
            host = '192.168.0.73',
            user = 'root',
            passwd = '',
            charset = 'utf8',
            cursorclass = Mysqldb.cursors.DictCursor,
        )
        self.dbpool = adbapi.ConnectionPool('lolita', **dbargs)
    
    def process_item(self, item, spider):
        return item
    def insert_into_table(self,conn,item):
        conn.execute('insert into finance_sina(plate_name) values(%s)', item[plate_name])
