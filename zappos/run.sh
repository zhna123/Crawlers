#!/bin/bash


scrapy crawl tiger_crawl_spider
/usr/local/bin/python3 check_tiger.py tiger.json <email-address>@gmail.com