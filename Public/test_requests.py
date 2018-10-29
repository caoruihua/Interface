# -*- coding: utf-8 -*-
# @Author  : laocao
import requests,json
from Public.log import LOG,logger
@logger('requests封装')
class requ():
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0",
                        "Authorization": "Bearer cf8d86e3-4ae9-4800-a937-714781106643"}
    def get(self, url,params):#get消息
        try:
            r = requests.get(url, params=params,headers=self.headers)
            r.encoding = 'UTF-8'
            json_response = json.loads(r.text)
            return {'code':0,'result':json_response}
        except Exception as e:
            LOG.info('get请求出错，出错原因:%s'%e)
            return {'code': 1, 'result': 'get请求出错，出错原因:%s'%e}
    def post(self, url, params):#post消息
        data = json.dumps(params)
        try:
            r =requests.post(url,params=data,headers=self.headers)
            json_response = json.loads(r.text)
            return {'code': 0, 'result': json_response}
        except Exception as e:
            LOG.info('post请求出错，出错原因:%s' % e)
            return {'code': 1, 'result': 'post请求出错，出错原因:%s' % e}
    def delfile(self,url,params):#删除的请求
        try:
            del_word=requests.delete(url,params=params,headers=self.headers)
            json_response=json.loads(del_word.text)
            return {'code': 0, 'result': json_response}
        except Exception as e:
            LOG.info('del请求出错，出错原因:%s' % e)
            return {'code': 1, 'result': 'del请求出错，出错原因:%s' % e}
    def putfile(self,url,params):#put请求
        try:
            data=json.dumps(params)
            me=requests.put(url,data)
            json_response=json.loads(me.text)
            return {'code': 0, 'result': json_response}
        except Exception as e:
            LOG.info('put请求出错，出错原因:%s' % e)
            return {'code': 1, 'result': 'put请求出错，出错原因:%s' % e}