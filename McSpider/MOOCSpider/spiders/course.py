import scrapy
from MOOCSpider.items import CourseItem
import json
from copy import deepcopy

class CourseSpider(scrapy.Spider):
    name = 'course'
    allowed_domains = ['www.icourse163.org']
    start_urls = ['http://www.icourse163.org/']

    def start_requests(self):#数据->https://www.icourse163.org/web/j/mocSearchBean.searchCourse.rpc?csrfKey=2e72caa03e43481d9aae81bc1ef6906c
        url='https://www.icourse163.org/web/j/mocSearchBean.searchCourse.rpc?csrfKey=2e72caa03e43481d9aae81bc1ef6906c'
        for i in range(7):
            data_dict = {
                'keyword':'python',
                'pageIndex': str(i+1),
                'highlight':'true',
                'orderBy':0,
                'stats': 30,
                'pageSize':20
                }#
            data_str=json.dumps(data_dict)
            data={
                'mocCourseQueryVo':data_str
            }
            yield scrapy.FormRequest(
                method='POST',
                url=url,
                formdata=data,
                callback=self.parse,
                dont_filter=True
            )
    def parse(self,response):
        data=response.body.decode('utf-8')
        course_list=json.loads(data)['result']['list']
        item=CourseItem()#初始化
        for course in course_list:
            CourseCard=course['mocCourseCard']['mocCourseCardDto']
            item['courseName']=CourseCard['name']
            item['university']=CourseCard['schoolPanel']['name']
            if CourseCard['mocTagDtos']:
                item['category']=CourseCard['mocTagDtos'][0]['name']
            else:
                item['category']='NULL'
            #人数提取
            item['enrollCount']=CourseCard['termPanel']['enrollCount']
            #学校名称缩写
            shortName=CourseCard['schoolPanel']['shortName']
            course_id=course['courseId']
            url='https://www.icourse163.org/course/'+\
                shortName+'-'+str(course_id)
            yield scrapy.Request(url,meta={'item':deepcopy(item)},
                                 callback=self.parse_section)
    def parse_section(self,response):
        item=response.meta['item']
        item['overview']='NULL'
        item['objective']='NULL'
        item['preliminaries'] = 'NULL'
        course_section=response.xpath(
            '//div[@id="content-section"]')[0]
        for i in range(3,10,2):
            path_str='div['+str(i)+']/span[2]/text()'
            text=course_section.xpath(path_str).extract()
            path='div['+str(i+1)+']/div//p//text()'
            if '课程概述' in text:
                overview=course_section.xpath(path).extract()
                overview=''.join(overview)
                item['overview']=overview
            elif '授课目标' in text:
                objective=course_section.xpath(path).extract()
                objective=''.join(objective)
                item['objective']=objective
            elif '预备知识' in text:
                preliminaries=course_section.xpath(path).extract()
                preliminaries=''.join(preliminaries)
                item['preliminaries']=preliminaries
            yield item

