#!/bin/bash


scrapy crawl tiger_crawl_spider
python check_tiger.py tiger.json <email>