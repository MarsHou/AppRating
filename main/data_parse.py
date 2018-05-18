#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 14:51
# @Author  : Mars
class DataParse(object):
    def get_last_page(self, json_data):
        feed = json_data.get('feed')
        href = feed.get('link')[3].get('attributes').get('href')

        start = href.find('=') + 1
        end = href[start:].find('/')
        return int(href[start:start + end])

    def get_data(self, json_data):
        entry = json_data.get('feed').get('entry')
        entry.pop(0)
        return entry
