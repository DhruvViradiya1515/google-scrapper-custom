import csv
import json
# from .items import NewsItem


class GooglePipeline:
    def __init__(self):
        pass

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        # if isinstance(item, NewsItem):
        #     pass
        search_object = vars(item['search'])
        for result_item in search_object['result_list']:
            result_item = vars(result_item)
            with open('result.txt','a') as file:
                # file.write(str(search_object))
                file.write(str(result_item["url"]))
                file.write("\n")

        return item

