#!/usr/bin/env python
# -*- coding: utf-8 -*-
from main import data_download, data_save, data_send, data_parse
from main.sortby import SortBy

URL = r'https://itunes.apple.com/rss/customerreviews/page=%d/id=%d/sortby=%s/json?l=en&&cc=cn'
RATING_URL = r'https://www.qimai.cn/app/comment/appid/%d/country/cn'
APP_ID = 1084660392


class RatingMain(object):

    def __init__(self):
        self.download = data_download.DataDownLoad()
        self.parse = data_parse.DataParse()
        self.save = data_save.DataSave()
        self.send = data_send.DataSend()

    def start(self):
        rating_url = RATING_URL % APP_ID
        # rating_data = self.download.download_html_data(rating_url)
        # print(rating_data)
        data = self.__start(1)
        file = self.save.save_data(data)
        # self.send.send_email(file)
        # print(data)

    def __start(self, page):
        url = URL % (page, APP_ID, SortBy.MOST_HELPFUL)
        print('start download page %d' % page)
        json_data = self.download.download_data(url)
        last = self.parse.get_last_page(json_data)
        array_data = self.parse.get_data(json_data)
        page += 1
        if page <= last:
            array_data.extend(self.__start(page))

        return array_data


if __name__ == "__main__":
    rating = RatingMain()
    rating.start()
