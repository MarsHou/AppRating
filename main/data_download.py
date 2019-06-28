#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import urllib2


class DataDownLoad(object):
    def download_data(self, url):
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return ""
        data = response.read().decode('utf-8')
        return json.loads(data)

    def download_html_data(self, rating_url):
        response = urllib2.urlopen(rating_url)
        if response.getcode() != 200:
            return ""
        return response.read().decode('utf-8')
