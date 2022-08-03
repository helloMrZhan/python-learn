# 实现一个用以 scrapy 爬虫处理中保存 stackoverflow 标签数据的管道处理类，爬虫管道类必须实现3个方法
#
# open_spider(self, spider)
# process_item(self, item, spider)
# close_spider(self, spider)
# 本例最终输出的 json 文件格式请参考stackoverflow.tag.json

# -*- coding: UTF-8 -*-
import json

class StackOverflowTagPipeline(object):
    def open_spider(self, spider):
        ''' 打开文件并写入'[\n' 到 json 文件'''
        self.file = open('/tmp/stackoverflow.tag.json', 'w')
        self.file.write('[\n')
        self.count = 0
        self.tags = {}

    def process_item(self, item, spider):
        ''' 写入一个 {"name":xxx} 格式的元素，注意逗号拼接 '''

        # 去重
        if self.tags.get(item['name']) is not None:
            return
        self.tags[item['name']] = True

        # 请正确实现拼接json写入的代码
        words = []
        if self.count > 0:
            words.append(',\n')
        words.append('  ')
        words.append(json.dumps(item, ensure_ascii=False).strip())
        result = ''.join(words)

        # 写入拼接文本
        self.file.write(result)
        self.count += 1

    def close_spider(self, spider):
        ''' 写入'\n]' 并关闭文件 '''
        self.file.write('\n]')
        self.file.close()

if __name__ == "__main__":
    t = StackOverflowTagPipeline()
    t.open_spider(None)
    t.process_item({'name': 'c++'}, None)
    t.close_spider(None)