# _*_ encoding:utf-8 _*_
from time import sleep
from tld import get_fld
import requests
import json
import math
import urllib3


'''
获取域名列表，要求不含协议名和端口号
'''
def getUrlList(filename):
    _list = []
    with open(file=filename, mode='r') as f:
        for line in f:
            _list.append(line.strip())            
    return _list

'''
保存结果到txt文件
'''
def saveResult(data):
    try:
        with open(file='./result.txt', mode='a', encoding='utf-8') as f:
            f.write(f"{data[0]},{data[1]},{data[2]}\n")
        f.close()
    except Exception as e:
        print(f"[-] 结果保存失败 - {e}")

'''
调用爱站接口进行查询
'''
def seo(domains):
    code = "xxxxx"#私钥
    api = "https://apistore.aizhan.com/baidurank/siteinfos/"#api地址
    str = ""
    for domain in domains:
        str += domain + "|"
    data = {
        "domains": str
    }
    try:
        temp = requests.post(
            url=api + code,
            timeout=10,
            data=data,
            proxies={
                "http": "http://127.0.0.1:8080",
                "https": "http://127.0.0.1:8080"
            },
            verify=False,
            allow_redirects=False
        )
        if temp.status_code == 200 and temp.text:
            content = json.loads(temp.text)
            if content["code"] != 200000:
                print(f"[-] 接口调用出错 - {content['msg']}")
                return False
            success = len(content['data']['success'])
            failed = len(content['data']['failed'])
            print(f"[*] 此次共查询{len(domains)}个域名,成功{success}个,失败{failed}个")
            #处理查询成功的域名
            data = content['data']['success']
            for item in data:
                if int(item['pc_br']) >= 1 or int(item['m_br']) >= 1:
                    saveResult(data=[item['domain'], item['pc_br'], item['m_br']])
            #处理查询失败的域名
            if failed != 0:
                print(f"[*] 以下域名无权重或查询失败")
                print("-"*22)
                for _item in content['data']['failed']:
                    print(_item)
                print("-"*22)
            else:
                return True
        else:
            print(f"[-] 接口调用出错 - {temp.status_code}")
            return False
    except Exception as e:
        print(f"[-] 接口调用出错 - {e}")
        return False

if __name__ == '__main__':
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    urls = getUrlList(filename='./urls.txt')
    big_data = [] #存储分组后的列表
    N = 50 #每个分组中的元素个数
    count = math.ceil(len(urls) / N)#向上取整得到分组的组数
    for i in range(count):
        big_data.append(urls[:N])
        del urls[:N]
    
    print(f"[*] 共将进行{len(big_data)}次查询,每次{N}个域名")
    for j in range(len(big_data)):
        print(f"[*] 开始第{j+1}次查询")
        seo(domains=big_data[j])
        sleep(5)











