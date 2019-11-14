import requests

# second_first_url = 'https://huobi.vn'    #需要科学上网
huobi_url = 'https://api.huobi.br.com'   #不用翻墙
parse ='/v1/common/symbols'

urls = huobi_url+parse
print(urls)
response = requests.get(urls)
print(response.status_code)
print(response.text)



class GetRequests(object):
    def __init__(self, name):
        self.name = name



    def get_text(self, url):
        #请求方法
        #text返回
        print(url)
        response = requests.get(url)

        return response.text

    def get_json(self, url):
        #请求方法
        # json格式返回
        print(url)
        response = requests.get(url)
        return response.json()


huobi = GetRequests()
text = huobi.get_text(urls)
print(test)