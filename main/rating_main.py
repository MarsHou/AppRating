#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from main import data_download, data_save, data_send, data_parse, show_process
from main.sortby import SortBy

URL = r'https://itunes.apple.com/rss/customerreviews/page=%d/id=%d/sortby=%s/json?l=en&&cc=cn'
RATING_URL = r'https://www.qimai.cn/app/comment/appid/%d/country/cn'
APP_ID = 1084660392


class RatingMain(object):

    def __init__(self):
        self.show_process = show_process.ShowProcess(10)
        self.download = data_download.DataDownLoad()
        self.parse = data_parse.DataParse()
        self.save = data_save.DataSave()
        self.send = data_send.DataSend()
        self.sort_by = SortBy.MOST_HELPFUL

    def start(self):
        # rating_url = RATING_URL % APP_ID
        # rating_data = self.download.download_html_data(rating_url)
        # print(rating_data)
        print('Most helpful:')
        data = self.__start(1)
        self.show_process.close()
        self.save.save_data(data, self.sort_by)
        # get data by most recent
        self.sort_by = SortBy.MOST_RECENT
        print('Most recent:')
        data = self.__start(1)
        self.show_process.close()
        self.save.save_data(data, self.sort_by)

    def __start(self, page):
        url = URL % (page, APP_ID, self.sort_by)
        json_data = self.download.download_data(url)
        self.show_process.show_process(page)
        last = self.parse.get_last_page(json_data)
        array_data = self.parse.get_data(json_data)
        page += 1
        if page <= last:
            array_data.extend(self.__start(page))

        return array_data


if __name__ == "__main__":
    rating = RatingMain()
    rating.start()
