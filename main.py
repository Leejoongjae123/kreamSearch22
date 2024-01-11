import json
import random

import openpyxl
import requests
import pprint
import random
import time
from bs4 import BeautifulSoup
import re
import datetime
from email.mime.multipart import MIMEMultipart  # 메일의 Data 영역의 메시지를 만드는 모듈
from email.mime.text import MIMEText  # 메일의 본문 내용을 만드는 모듈
from email.mime.base import MIMEBase
from email import encoders
import smtplib  # SMTP 사용을 위한 모듈

def extract_characters(text):
    return ''.join(re.findall(r'[\w\s]', text))


def GetIDs():

    productIdList=[]
    categoryList=['63','34','64','65','9','66','54','7','67','46','11','43','68']
    for category in categoryList:
        count = 1
        while True:
            cookies = {
                'i18n_redirected': 'kr',
                '_fwb': '53Fihu8lGaq0KdYC9zdmgQ.1704327945391',
                'afUserId': 'a03fa8b1-7200-4048-8b91-5c1f2148d240-p',
                'airbridge_device_alias': '%7B%22amplitude_device_id%22%3A%2241bf9ef6-b793-402d-a489-3299161a9bf0%22%7D',
                'AF_SYNC': '1704327946140',
                '_fbp': 'fb.2.1704327949716.1158384894',
                'ab.storage.deviceId.a45e842b-5d46-46bf-8f41-2f75d6fd4b37': '%7B%22g%22%3A%22a3e13174-64f4-98a9-7887-9f7f7cd4e4c1%22%2C%22c%22%3A1704327954524%2C%22l%22%3A1704328015759%7D',
                'ab.storage.userId.a45e842b-5d46-46bf-8f41-2f75d6fd4b37': '%7B%22g%22%3A%2200bbc1a3-69e7-461b-8d05-34353f86ace0%22%2C%22c%22%3A1704328015758%2C%22l%22%3A1704328015759%7D',
                'did': '62c963a0-bdfd-488d-b8a8-5bcf1c8120dd',
                'AMP_MKTG_487619ef1d': 'JTdCJTdE',
                '_token.local': 'false',
                '_refresh_token.local': 'false',
                '_gid': 'GA1.3.1184485473.1704430254',
                'strategy': 'local',
                'login_type': 'social',
                '_ga': 'GA1.3.482881550.1704327946',
                '_gat_gtag_UA_153398119_1': '1',
                'airbridge_session': '%7B%22id%22%3A%22d8d1b549-b05c-427a-b14d-cae8840d3e19%22%2C%22timeout%22%3A1800000%2C%22start%22%3A1704430254282%2C%22end%22%3A1704430400653%7D',
                'ab.storage.sessionId.a45e842b-5d46-46bf-8f41-2f75d6fd4b37': '%7B%22g%22%3A%22025e3913-2b7b-264a-3d88-4629c462cfa5%22%2C%22e%22%3A1704432220163%2C%22c%22%3A1704430253489%2C%22l%22%3A1704430420163%7D',
                'AMP_487619ef1d': 'JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI0MWJmOWVmNi1iNzkzLTQwMmQtYTQ4OS0zMjk5MTYxYTliZjAlMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjIwMGJiYzFhMy02OWU3LTQ2MWItOGQwNS0zNDM1M2Y4NmFjZTAlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzA0NDMwMjUyOTQ4JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTcwNDQzMDQyMDE2NCUyQyUyMmxhc3RFdmVudElkJTIyJTNBMjElN0Q=',
                'wcs_bt': 's_59a6a417df3:1704430420',
                '_ga_SRFKTMTR0R': 'GS1.1.1704430253.2.1.1704430421.38.0.0',
                '_ga_5LYDPM15LW': 'GS1.1.1704430253.2.1.1704430421.38.0.0',
            }

            headers = {
                'authority': 'www.kream.co.kr',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
                # 'cookie': 'i18n_redirected=kr; _fwb=53Fihu8lGaq0KdYC9zdmgQ.1704327945391; afUserId=a03fa8b1-7200-4048-8b91-5c1f2148d240-p; airbridge_device_alias=%7B%22amplitude_device_id%22%3A%2241bf9ef6-b793-402d-a489-3299161a9bf0%22%7D; AF_SYNC=1704327946140; _fbp=fb.2.1704327949716.1158384894; ab.storage.deviceId.a45e842b-5d46-46bf-8f41-2f75d6fd4b37=%7B%22g%22%3A%22a3e13174-64f4-98a9-7887-9f7f7cd4e4c1%22%2C%22c%22%3A1704327954524%2C%22l%22%3A1704328015759%7D; ab.storage.userId.a45e842b-5d46-46bf-8f41-2f75d6fd4b37=%7B%22g%22%3A%2200bbc1a3-69e7-461b-8d05-34353f86ace0%22%2C%22c%22%3A1704328015758%2C%22l%22%3A1704328015759%7D; did=62c963a0-bdfd-488d-b8a8-5bcf1c8120dd; AMP_MKTG_487619ef1d=JTdCJTdE; _token.local=false; _refresh_token.local=false; _gid=GA1.3.1184485473.1704430254; strategy=local; login_type=social; _ga=GA1.3.482881550.1704327946; _gat_gtag_UA_153398119_1=1; airbridge_session=%7B%22id%22%3A%22d8d1b549-b05c-427a-b14d-cae8840d3e19%22%2C%22timeout%22%3A1800000%2C%22start%22%3A1704430254282%2C%22end%22%3A1704430400653%7D; ab.storage.sessionId.a45e842b-5d46-46bf-8f41-2f75d6fd4b37=%7B%22g%22%3A%22025e3913-2b7b-264a-3d88-4629c462cfa5%22%2C%22e%22%3A1704432220163%2C%22c%22%3A1704430253489%2C%22l%22%3A1704430420163%7D; AMP_487619ef1d=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI0MWJmOWVmNi1iNzkzLTQwMmQtYTQ4OS0zMjk5MTYxYTliZjAlMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjIwMGJiYzFhMy02OWU3LTQ2MWItOGQwNS0zNDM1M2Y4NmFjZTAlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzA0NDMwMjUyOTQ4JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTcwNDQzMDQyMDE2NCUyQyUyMmxhc3RFdmVudElkJTIyJTNBMjElN0Q=; wcs_bt=s_59a6a417df3:1704430420; _ga_SRFKTMTR0R=GS1.1.1704430253.2.1.1704430421.38.0.0; _ga_5LYDPM15LW=GS1.1.1704430253.2.1.1704430421.38.0.0',
                'referer': 'https://www.kream.co.kr/search?tab=43',
                'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'x-kream-api-version': '25',
                'x-kream-client-datetime': '20240105135348+0900',
                'x-kream-device-id': 'web;62c963a0-bdfd-488d-b8a8-5bcf1c8120dd',
                'x-kream-web-build-version': '4.17.7',
            }

            params = {
                'cursor': count,
                'tab': '43',
                'shop_category_id': category,
                'gender':''
                # 'request_key': 'fb3664a0-808c-485f-9786-998d4453bbaa',
            }
            while True:
                try:
                    response = requests.get('https://www.kream.co.kr/api/p/tabs/43/', params=params, cookies=cookies, headers=headers)
                    response.raise_for_status()
                    print('statuscode:',response.status_code)
                    time.sleep(random.randint(5, 10) * 0.1)
                    break
                except:
                    print("실패")
                    time.sleep(10)

            results=json.loads(response.text)
            # pprint.pprint(results)
            results=results['items']
            if len(results)==0:
                break
            for result in results:
                try:
                    productId=result['product']['release']['id']
                except:
                    productId=""
                # print("productId:",productId)
                try:
                    title=result['product']['release']['translated_name']
                except:
                    title=""
                # print("title:",title)
                try:
                    brand = result['product']['brand']['name']
                except:
                    brand=""
                # print("brand:",brand,"/ brand_TYPE:",type(brand))
                try:
                    modelCode=result['product']['release']['style_code']
                except:
                    modelCode=""
                # print("modelCode:",modelCode)
                # print("productId:",productId,"/ productId_TYPE:",type(productId))
                data={'productId':productId,'title':title,'modelCode':modelCode,'brand':brand}
                print("data:",data,"/ data_TYPE:",type(data))
                productIdList.append(data)
            with open('productIdList.json', 'w',encoding='utf-8-sig') as f:
                json.dump(productIdList, f, indent=2,ensure_ascii=False)
            print("================={}/{}/{}==========".format(category,count,len(productIdList)))
            if count>=100:
                break
            count+=1
    return productIdList

    # pprint.pprint(results)

def GetBasicData(cookies,productNo):
    print("1234")
    headers = {
        'authority': 'www.kream.co.kr',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        # 'cookie': 'i18n_redirected=kr; did=dd95735e-157c-4bab-a152-cdf6a42dbd0d; AMP_MKTG_487619ef1d=JTdCJTdE; _gid=GA1.3.190152346.1694763247; afUserId=29bf6f50-7c3d-4e36-8a58-1539c060e43e-p; AF_SYNC=1694763248508; _token.social_naver=false; _refresh_token.social_naver=false; refresh_token_cookie=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5NDc2MzI1NSwianRpIjoiYjBiN2ZkMTUtNGM3OC00NzY3LWJkNzgtODI2YjhlYTY1Y2UwIiwidHlwZSI6InJlZnJlc2giLCJpZGVudGl0eSI6NTc4NjMxMiwibmJmIjoxNjk0NzYzMjU1LCJjc3JmIjoiMDc1ZmEzYjItZTVlNi00NDFmLWJmZjMtOTU0ZWE3ZmEyZTZlIiwiZXhwIjoxNjk0ODQ5NjU1LCJ1YyI6eyJzYWZlIjp0cnVlfX0.Fy-n5ifUn9wNb2Ef7G4RSbt3XqcbgJCmXyN4xlp0yM8; csrf_refresh_token=075fa3b2-e5e6-441f-bff3-954ea7fa2e6e; login_type=social; _token.local=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6dHJ1ZSwiaWF0IjoxNjk0NzYzMjU1LCJqdGkiOiIzZTY5MGQwMi1hMDA3LTQ2ZmQtOWQ4NS1kOTQ1NzE0ODJiMTgiLCJ0eXBlIjoiYWNjZXNzIiwiaWRlbnRpdHkiOjU3ODYzMTIsIm5iZiI6MTY5NDc2MzI1NSwiY3NyZiI6IjY4YzI4ZjgxLTFmYmQtNDg2ZS05M2ZiLWQ5NzAxZmUwNjc4NiIsImV4cCI6MTY5NDc3MDQ1NSwidWMiOnsic2FmZSI6dHJ1ZX19.BHTWa9FmkV2VZ2uenBs3-2Gve32v_73qR5G3OJgnWCc; _refresh_token.local=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5NDc2MzI1NSwianRpIjoiYjBiN2ZkMTUtNGM3OC00NzY3LWJkNzgtODI2YjhlYTY1Y2UwIiwidHlwZSI6InJlZnJlc2giLCJpZGVudGl0eSI6NTc4NjMxMiwibmJmIjoxNjk0NzYzMjU1LCJjc3JmIjoiMDc1ZmEzYjItZTVlNi00NDFmLWJmZjMtOTU0ZWE3ZmEyZTZlIiwiZXhwIjoxNjk0ODQ5NjU1LCJ1YyI6eyJzYWZlIjp0cnVlfX0.Fy-n5ifUn9wNb2Ef7G4RSbt3XqcbgJCmXyN4xlp0yM8; strategy=local; ab.storage.userId.8d5d348c-fc26-4528-a5b4-627447ffad5a=%7B%22g%22%3A%2200bbc1a3-69e7-461b-8d05-34353f86ace0%22%2C%22c%22%3A1694763257734%2C%22l%22%3A1694763257735%7D; ab.storage.deviceId.8d5d348c-fc26-4528-a5b4-627447ffad5a=%7B%22g%22%3A%2203cb83bf-8a2e-0465-8ff8-b20c0d6bde11%22%2C%22c%22%3A1694763257736%2C%22l%22%3A1694763257736%7D; ab.storage.sessionId.8d5d348c-fc26-4528-a5b4-627447ffad5a=%7B%22g%22%3A%2221347e74-d2b6-d3c0-6761-0529bb05fe1d%22%2C%22e%22%3A1694765057738%2C%22c%22%3A1694763257735%2C%22l%22%3A1694763257738%7D; _ga=GA1.3.1357366474.1694763247; AMP_487619ef1d=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjIwOTU1MGNiZS01NTdkLTRhZTItYWIwMi03OTY1ZmU3MjQyODYlMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjIwMGJiYzFhMy02OWU3LTQ2MWItOGQwNS0zNDM1M2Y4NmFjZTAlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNjk0NzYzMjQ1ODE4JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTY5NDc2MzI2NTczMSUyQyUyMmxhc3RFdmVudElkJTIyJTNBNiU3RA==; wcs_bt=s_59a6a417df3:1694763385; _fbp=fb.2.1694763385351.1397069681; _ga_SRFKTMTR0R=GS1.1.1694763246.1.1.1694763386.59.0.0; _ga_5LYDPM15LW=GS1.1.1694763246.1.1.1694763386.59.0.0',
        'referer': 'https://www.kream.co.kr/login',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    }

    while True:
        try:
            response = requests.get('https://www.kream.co.kr/products/{}'.format(productNo), cookies=cookies, headers=headers)
            print(response.text)
            response.raise_for_status()
            print("statuscode:",response.status_code)
            break
        except:
            print("실패")
            time.sleep(10)

    soup=BeautifulSoup(response.text,'lxml')
    # print(soup.prettify())

    infoBox=soup.find('div',attrs={'class':'product_info_wrap'})
    try:
        originPrice=infoBox.find_all('div',attrs={'class':'product_info'})[0].get_text()
        # 정규 표현식을 사용하여 숫자만 추출
        extracted = re.findall(r'\d+', originPrice.replace(',', ''))
        # 추출된 숫자 중 두 번째 숫자(한화 금액) 선택
        won_amount = extracted[1] if len(extracted) > 1 else extracted[0]
        originPrice=int(won_amount)
    except:
        originPrice=""
    print('originPrice:',originPrice)

    scripts=soup.find_all("script",type="application/ld+json")
    target=""
    for script in scripts:
        
        if str(script).find("highPrice")>=0:
            result=json.loads(script.get_text())
            # pprint.pprint(result)
            highPrice=result['offers']['highPrice']
            print("highPrice:",highPrice,"/ highPrice_TYPE:",type(highPrice))

    checkResult=False
    try:
        if int(highPrice)>=int(originPrice):
            checkResult=True
    except:
        print("비교불가")
    
    try:
        title=soup.find("meta",attrs={'name':'og:title'})['content'].strip()
    except:
        title=""
    print("title:",title)
    
    return checkResult,originPrice

def GetToken():
    cookies = {
        'i18n_redirected': 'kr',
        'afUserId': '92d9569b-f0e5-4a77-aed1-f0b3ac529581-p',
        'AF_SYNC': '1701661188073',
        'airbridge_device_alias': '%7B%22amplitude_device_id%22%3A%22ffdb56da-7661-42f0-8d87-4d1d1b59d46c%22%7D',
        '_fwb': '11Uusi3FTaGqJopqZc3EJx.1701833305082',
        '_fbp': 'fb.2.1701936854500.2073430007',
        '_gid': 'GA1.3.1820798567.1701936855',
        'ab.storage.deviceId.a45e842b-5d46-46bf-8f41-2f75d6fd4b37': '%7B%22g%22%3A%22e10b0036-816e-3e47-fb0a-e136dbfadb43%22%2C%22c%22%3A1701936863775%2C%22l%22%3A1701936863775%7D',
        'did': '44c3f570-2970-47b3-9fc2-a23f225698eb',
        '_token.local': 'false',
        'NA_SA': 'Y2k9MHpDMDAwMS1LQjV6dkNvcmcxaTR8dD0xNzAxOTU0MTI1fHU9aHR0cHMlM0ElMkYlMkZrcmVhbS5jby5rciUyRiUzRnV0bV9zb3VyY2UlM0RuYXZlciUyNnV0bV9tZWRpdW0lM0RjcG0lMjZ1dG1fY2FtcGFpZ24lM0RCUyUyNnV0bV9ncm91cCUzRFBDXzIzMTIwNCUyNnV0bV9jb250ZW50JTNEaG9tZWxpbmslMjZ1dG1fdGVybSUzREtSRUFNJTI2bl9tZWRpYSUzRDI3NzU4JTI2bl9xdWVyeSUzREtSRUFNJTI2bl9yYW5rJTNEMSUyNm5fYWRfZ3JvdXAlM0RncnAtYTAwMS0wNC0wMDAwMDAwMzY5Nzk0ODElMjZuX2FkJTNEbmFkLWEwMDEtMDQtMDAwMDAwMjc1OTQ3NDg3JTI2bl9rZXl3b3JkX2lkJTNEbmt3LWEwMDEtMDQtMDAwMDA1NjE5NTA1NzkzJTI2bl9rZXl3b3JkJTNES1JFQU0lMjZuX2NhbXBhaWduX3R5cGUlM0Q0JTI2bl9jb250cmFjdCUzRHRjdC1hMDAxLTA0LTAwMDAwMDAwMDgwNjMxOCUyNm5fYWRfZ3JvdXBfdHlwZSUzRDUlMjZOYVBtJTNEY3QlMjUzRGxwdjdqaDh3JTI1N0NjaSUyNTNEMHpDMDAwMS1LQjV6dkNvcmcxaTQlMjU3Q3RyJTI1M0Ricm5kJTI1N0NoayUyNTNEODUyMGMxMjc1MTlkZDQyZTA3OWMyNzMxOGZlOGFlM2RkMzNiMzE3ZnxyPWh0dHBzJTNBJTJGJTJGc2VhcmNoLm5hdmVyLmNvbSUyRnNlYXJjaC5uYXZlciUzRndoZXJlJTNEbmV4ZWFyY2glMjZzbSUzRHRvcF9odHklMjZmYm0lM0QwJTI2aWUlM0R1dGY4JTI2cXVlcnklM0RrcmVhbQ==',
        'NA_SAS': '1',
        'NVADID': '0zC0001-KB5zvCorg1i4',
        '_refresh_token.local': 'false',
        'AMP_MKTG_487619ef1d': 'JTdCJTIydXRtX2NhbXBhaWduJTIyJTNBJTIyTkVXXyVFQyU5RSU5MCVFQyU4MiVBQyVFQiVBQSU4NV8lRUMlODglOTglRUIlOEYlOTlfUEMlMjIlMkMlMjJ1dG1fY29udGVudCUyMiUzQSUyMkEuJTIwJUVDJTlFJTkwJUVDJTgyJUFDJUVCJUFBJTg1XyVFQyU4OCU5OCVFQiU4RiU5OSUyMiUyQyUyMnV0bV9tZWRpdW0lMjIlM0ElMjJjcGMlMjIlMkMlMjJ1dG1fc291cmNlJTIyJTNBJTIyZ29vZ2xlJTIyJTJDJTIydXRtX3Rlcm0lMjIlM0ElMjIlRUQlODElQUMlRUIlQTYlQkMlMjIlMkMlMjJyZWZlcnJlciUyMiUzQSUyMmh0dHBzJTNBJTJGJTJGd3d3Lmdvb2dsZS5jb20lMkYlMjIlMkMlMjJyZWZlcnJpbmdfZG9tYWluJTIyJTNBJTIyd3d3Lmdvb2dsZS5jb20lMjIlMkMlMjJnY2xpZCUyMiUzQSUyMkNqd0tDQWlBOThXckJoQVlFaXdBMld2aE9pRTF6cnlVdjZaUkl2Y2QwQmhlalowRTRyeUtKM3dxTzVqcUt0R2ZER1VHbVQ2VzFDQURJaG9DUGhrUUF2RF9Cd0UlMjIlN0Q=',
        '_gac_UA-153398119-1': '1.1701959965.CjwKCAiA98WrBhAYEiwA2WvhOiE1zryUv6ZRIvcd0BhejZ0E4ryKJ3wqO5jqKtGfDGUGmT6W1CADIhoCPhkQAvD_BwE',
        '_gat_gtag_UA_153398119_1': '1',
        'airbridge_utm': '%7B%22channel%22%3A%22google%22%2C%22parameter%22%3A%7B%22medium%22%3A%22cpc%22%2C%22campaign%22%3A%22NEW_%uC790%uC0AC%uBA85_%uC218%uB3D9_PC%22%2C%22term%22%3A%22%uD06C%uB9BC%22%2C%22content%22%3A%22A.%20%uC790%uC0AC%uBA85_%uC218%uB3D9%22%7D%7D',
        'airbridge_utm_url': 'https%3A//kream.co.kr/%3Futm_source%3Dgoogle%26utm_medium%3Dcpc%26utm_campaign%3DNEW_%25EC%259E%2590%25EC%2582%25AC%25EB%25AA%2585_%25EC%2588%2598%25EB%258F%2599_PC%26utm_term%3D%25ED%2581%25AC%25EB%25A6%25BC%26utm_content%3DA.%2520%25EC%259E%2590%25EC%2582%25AC%25EB%25AA%2585_%25EC%2588%2598%25EB%258F%2599%26gclid%3DCjwKCAiA98WrBhAYEiwA2WvhOiE1zryUv6ZRIvcd0BhejZ0E4ryKJ3wqO5jqKtGfDGUGmT6W1CADIhoCPhkQAvD_BwE',
        'airbridge_utm_timestamp': '1701959965224',
        'ab.storage.sessionId.a45e842b-5d46-46bf-8f41-2f75d6fd4b37': '%7B%22g%22%3A%22eb15a355-54eb-f80a-9e2b-b64386e56a98%22%2C%22e%22%3A1701961777465%2C%22c%22%3A1701959977466%2C%22l%22%3A1701959977466%7D',
        'wcs_bt': 's_59a6a417df3:1701959977',
        'AMP_487619ef1d': 'JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjJmZmRiNTZkYS03NjYxLTQyZjAtOGQ4Ny00ZDFkMWI1OWQ0NmMlMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjJjZWRmNjk1ZC1jMzJhLTQxNjctOWJmNi0wNjFlOGI0NTdmNTclMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzAxOTU5OTYzMDgxJTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTcwMTk1OTk3NzQ3NSUyQyUyMmxhc3RFdmVudElkJTIyJTNBODUlN0Q=',
        'airbridge_session': '%7B%22id%22%3A%226ec19915-5bc6-464b-afe0-7307b9958696%22%2C%22timeout%22%3A1800000%2C%22start%22%3A1701959965244%2C%22end%22%3A1701959977548%7D',
        '_ga_SRFKTMTR0R': 'GS1.1.1701959964.8.1.1701959977.47.0.0',
        '_ga_5LYDPM15LW': 'GS1.1.1701959964.8.1.1701959977.47.0.0',
        '_ga': 'GA1.3.248227678.1701661186',
    }

    headers = {
        'authority': 'kream.co.kr',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        # 'cookie': 'i18n_redirected=kr; afUserId=92d9569b-f0e5-4a77-aed1-f0b3ac529581-p; AF_SYNC=1701661188073; airbridge_device_alias=%7B%22amplitude_device_id%22%3A%22ffdb56da-7661-42f0-8d87-4d1d1b59d46c%22%7D; _fwb=11Uusi3FTaGqJopqZc3EJx.1701833305082; _fbp=fb.2.1701936854500.2073430007; _gid=GA1.3.1820798567.1701936855; ab.storage.deviceId.a45e842b-5d46-46bf-8f41-2f75d6fd4b37=%7B%22g%22%3A%22e10b0036-816e-3e47-fb0a-e136dbfadb43%22%2C%22c%22%3A1701936863775%2C%22l%22%3A1701936863775%7D; did=44c3f570-2970-47b3-9fc2-a23f225698eb; _token.local=false; NA_SA=Y2k9MHpDMDAwMS1LQjV6dkNvcmcxaTR8dD0xNzAxOTU0MTI1fHU9aHR0cHMlM0ElMkYlMkZrcmVhbS5jby5rciUyRiUzRnV0bV9zb3VyY2UlM0RuYXZlciUyNnV0bV9tZWRpdW0lM0RjcG0lMjZ1dG1fY2FtcGFpZ24lM0RCUyUyNnV0bV9ncm91cCUzRFBDXzIzMTIwNCUyNnV0bV9jb250ZW50JTNEaG9tZWxpbmslMjZ1dG1fdGVybSUzREtSRUFNJTI2bl9tZWRpYSUzRDI3NzU4JTI2bl9xdWVyeSUzREtSRUFNJTI2bl9yYW5rJTNEMSUyNm5fYWRfZ3JvdXAlM0RncnAtYTAwMS0wNC0wMDAwMDAwMzY5Nzk0ODElMjZuX2FkJTNEbmFkLWEwMDEtMDQtMDAwMDAwMjc1OTQ3NDg3JTI2bl9rZXl3b3JkX2lkJTNEbmt3LWEwMDEtMDQtMDAwMDA1NjE5NTA1NzkzJTI2bl9rZXl3b3JkJTNES1JFQU0lMjZuX2NhbXBhaWduX3R5cGUlM0Q0JTI2bl9jb250cmFjdCUzRHRjdC1hMDAxLTA0LTAwMDAwMDAwMDgwNjMxOCUyNm5fYWRfZ3JvdXBfdHlwZSUzRDUlMjZOYVBtJTNEY3QlMjUzRGxwdjdqaDh3JTI1N0NjaSUyNTNEMHpDMDAwMS1LQjV6dkNvcmcxaTQlMjU3Q3RyJTI1M0Ricm5kJTI1N0NoayUyNTNEODUyMGMxMjc1MTlkZDQyZTA3OWMyNzMxOGZlOGFlM2RkMzNiMzE3ZnxyPWh0dHBzJTNBJTJGJTJGc2VhcmNoLm5hdmVyLmNvbSUyRnNlYXJjaC5uYXZlciUzRndoZXJlJTNEbmV4ZWFyY2glMjZzbSUzRHRvcF9odHklMjZmYm0lM0QwJTI2aWUlM0R1dGY4JTI2cXVlcnklM0RrcmVhbQ==; NA_SAS=1; NVADID=0zC0001-KB5zvCorg1i4; _refresh_token.local=false; AMP_MKTG_487619ef1d=JTdCJTIydXRtX2NhbXBhaWduJTIyJTNBJTIyTkVXXyVFQyU5RSU5MCVFQyU4MiVBQyVFQiVBQSU4NV8lRUMlODglOTglRUIlOEYlOTlfUEMlMjIlMkMlMjJ1dG1fY29udGVudCUyMiUzQSUyMkEuJTIwJUVDJTlFJTkwJUVDJTgyJUFDJUVCJUFBJTg1XyVFQyU4OCU5OCVFQiU4RiU5OSUyMiUyQyUyMnV0bV9tZWRpdW0lMjIlM0ElMjJjcGMlMjIlMkMlMjJ1dG1fc291cmNlJTIyJTNBJTIyZ29vZ2xlJTIyJTJDJTIydXRtX3Rlcm0lMjIlM0ElMjIlRUQlODElQUMlRUIlQTYlQkMlMjIlMkMlMjJyZWZlcnJlciUyMiUzQSUyMmh0dHBzJTNBJTJGJTJGd3d3Lmdvb2dsZS5jb20lMkYlMjIlMkMlMjJyZWZlcnJpbmdfZG9tYWluJTIyJTNBJTIyd3d3Lmdvb2dsZS5jb20lMjIlMkMlMjJnY2xpZCUyMiUzQSUyMkNqd0tDQWlBOThXckJoQVlFaXdBMld2aE9pRTF6cnlVdjZaUkl2Y2QwQmhlalowRTRyeUtKM3dxTzVqcUt0R2ZER1VHbVQ2VzFDQURJaG9DUGhrUUF2RF9Cd0UlMjIlN0Q=; _gac_UA-153398119-1=1.1701959965.CjwKCAiA98WrBhAYEiwA2WvhOiE1zryUv6ZRIvcd0BhejZ0E4ryKJ3wqO5jqKtGfDGUGmT6W1CADIhoCPhkQAvD_BwE; _gat_gtag_UA_153398119_1=1; airbridge_utm=%7B%22channel%22%3A%22google%22%2C%22parameter%22%3A%7B%22medium%22%3A%22cpc%22%2C%22campaign%22%3A%22NEW_%uC790%uC0AC%uBA85_%uC218%uB3D9_PC%22%2C%22term%22%3A%22%uD06C%uB9BC%22%2C%22content%22%3A%22A.%20%uC790%uC0AC%uBA85_%uC218%uB3D9%22%7D%7D; airbridge_utm_url=https%3A//kream.co.kr/%3Futm_source%3Dgoogle%26utm_medium%3Dcpc%26utm_campaign%3DNEW_%25EC%259E%2590%25EC%2582%25AC%25EB%25AA%2585_%25EC%2588%2598%25EB%258F%2599_PC%26utm_term%3D%25ED%2581%25AC%25EB%25A6%25BC%26utm_content%3DA.%2520%25EC%259E%2590%25EC%2582%25AC%25EB%25AA%2585_%25EC%2588%2598%25EB%258F%2599%26gclid%3DCjwKCAiA98WrBhAYEiwA2WvhOiE1zryUv6ZRIvcd0BhejZ0E4ryKJ3wqO5jqKtGfDGUGmT6W1CADIhoCPhkQAvD_BwE; airbridge_utm_timestamp=1701959965224; ab.storage.sessionId.a45e842b-5d46-46bf-8f41-2f75d6fd4b37=%7B%22g%22%3A%22eb15a355-54eb-f80a-9e2b-b64386e56a98%22%2C%22e%22%3A1701961777465%2C%22c%22%3A1701959977466%2C%22l%22%3A1701959977466%7D; wcs_bt=s_59a6a417df3:1701959977; AMP_487619ef1d=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjJmZmRiNTZkYS03NjYxLTQyZjAtOGQ4Ny00ZDFkMWI1OWQ0NmMlMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjJjZWRmNjk1ZC1jMzJhLTQxNjctOWJmNi0wNjFlOGI0NTdmNTclMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzAxOTU5OTYzMDgxJTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTcwMTk1OTk3NzQ3NSUyQyUyMmxhc3RFdmVudElkJTIyJTNBODUlN0Q=; airbridge_session=%7B%22id%22%3A%226ec19915-5bc6-464b-afe0-7307b9958696%22%2C%22timeout%22%3A1800000%2C%22start%22%3A1701959965244%2C%22end%22%3A1701959977548%7D; _ga_SRFKTMTR0R=GS1.1.1701959964.8.1.1701959977.47.0.0; _ga_5LYDPM15LW=GS1.1.1701959964.8.1.1701959977.47.0.0; _ga=GA1.3.248227678.1701661186',
        'origin': 'https://kream.co.kr',
        'referer': 'https://kream.co.kr/login',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-kream-api-version': '26',
        'x-kream-client-datetime': '20231207233954+0900',
        'x-kream-device-id': 'web;44c3f570-2970-47b3-9fc2-a23f225698eb',
        'x-kream-web-build-version': '4.17.0',
    }

    # params = {
    #     'request_key': '039854fd-67ea-443d-a2b9-065d71bb2ba0',
    # }
    #대표님 테스트계정
    # json_data = {
    #     'email': 'zmflal001@gmail.com',
    #     'password': 'zmflal001*',
    # }
    #대표님 서버 계정
    json_data = {
        'email': 'civilkwak@naver.com',
        'password': 'dlwndwo2!',
    }

    response = requests.post('https://kream.co.kr/api/auth/login', cookies=cookies, headers=headers,
                             json=json_data)
    print(response.text)
    results=json.loads(response.text)
    with open('tokenData.json', 'w',encoding='utf-8-sig') as f:
        json.dump(results, f, indent=2,ensure_ascii=False)
    return results

def GetGMTransaction(GMScroll,token,refreshToken,headers,productNo):
    cookies = {
        'i18n_redirected': 'kr',
        'afUserId': '92d9569b-f0e5-4a77-aed1-f0b3ac529581-p',
        'AF_SYNC': '1701661188073',
        'airbridge_device_alias': '%7B%22amplitude_device_id%22%3A%22ffdb56da-7661-42f0-8d87-4d1d1b59d46c%22%7D',
        '_fwb': '11Uusi3FTaGqJopqZc3EJx.1701833305082',
        '_fbp': 'fb.2.1701936854500.2073430007',
        '_gid': 'GA1.3.1820798567.1701936855',
        'did': '44c3f570-2970-47b3-9fc2-a23f225698eb',
        'NA_SA': 'Y2k9MHpDMDAwMS1LQjV6dkNvcmcxaTR8dD0xNzAxOTU0MTI1fHU9aHR0cHMlM0ElMkYlMkZrcmVhbS5jby5rciUyRiUzRnV0bV9zb3VyY2UlM0RuYXZlciUyNnV0bV9tZWRpdW0lM0RjcG0lMjZ1dG1fY2FtcGFpZ24lM0RCUyUyNnV0bV9ncm91cCUzRFBDXzIzMTIwNCUyNnV0bV9jb250ZW50JTNEaG9tZWxpbmslMjZ1dG1fdGVybSUzREtSRUFNJTI2bl9tZWRpYSUzRDI3NzU4JTI2bl9xdWVyeSUzREtSRUFNJTI2bl9yYW5rJTNEMSUyNm5fYWRfZ3JvdXAlM0RncnAtYTAwMS0wNC0wMDAwMDAwMzY5Nzk0ODElMjZuX2FkJTNEbmFkLWEwMDEtMDQtMDAwMDAwMjc1OTQ3NDg3JTI2bl9rZXl3b3JkX2lkJTNEbmt3LWEwMDEtMDQtMDAwMDA1NjE5NTA1NzkzJTI2bl9rZXl3b3JkJTNES1JFQU0lMjZuX2NhbXBhaWduX3R5cGUlM0Q0JTI2bl9jb250cmFjdCUzRHRjdC1hMDAxLTA0LTAwMDAwMDAwMDgwNjMxOCUyNm5fYWRfZ3JvdXBfdHlwZSUzRDUlMjZOYVBtJTNEY3QlMjUzRGxwdjdqaDh3JTI1N0NjaSUyNTNEMHpDMDAwMS1LQjV6dkNvcmcxaTQlMjU3Q3RyJTI1M0Ricm5kJTI1N0NoayUyNTNEODUyMGMxMjc1MTlkZDQyZTA3OWMyNzMxOGZlOGFlM2RkMzNiMzE3ZnxyPWh0dHBzJTNBJTJGJTJGc2VhcmNoLm5hdmVyLmNvbSUyRnNlYXJjaC5uYXZlciUzRndoZXJlJTNEbmV4ZWFyY2glMjZzbSUzRHRvcF9odHklMjZmYm0lM0QwJTI2aWUlM0R1dGY4JTI2cXVlcnklM0RrcmVhbQ==',
        'NA_SAS': '1',
        'NVADID': '0zC0001-KB5zvCorg1i4',
        'AMP_MKTG_487619ef1d': 'JTdCJTIydXRtX2NhbXBhaWduJTIyJTNBJTIyTkVXXyVFQyU5RSU5MCVFQyU4MiVBQyVFQiVBQSU4NV8lRUMlODglOTglRUIlOEYlOTlfUEMlMjIlMkMlMjJ1dG1fY29udGVudCUyMiUzQSUyMkEuJTIwJUVDJTlFJTkwJUVDJTgyJUFDJUVCJUFBJTg1XyVFQyU4OCU5OCVFQiU4RiU5OSUyMiUyQyUyMnV0bV9tZWRpdW0lMjIlM0ElMjJjcGMlMjIlMkMlMjJ1dG1fc291cmNlJTIyJTNBJTIyZ29vZ2xlJTIyJTJDJTIydXRtX3Rlcm0lMjIlM0ElMjIlRUQlODElQUMlRUIlQTYlQkMlMjIlMkMlMjJyZWZlcnJlciUyMiUzQSUyMmh0dHBzJTNBJTJGJTJGd3d3Lmdvb2dsZS5jb20lMkYlMjIlMkMlMjJyZWZlcnJpbmdfZG9tYWluJTIyJTNBJTIyd3d3Lmdvb2dsZS5jb20lMjIlMkMlMjJnY2xpZCUyMiUzQSUyMkNqd0tDQWlBOThXckJoQVlFaXdBMld2aE9pRTF6cnlVdjZaUkl2Y2QwQmhlalowRTRyeUtKM3dxTzVqcUt0R2ZER1VHbVQ2VzFDQURJaG9DUGhrUUF2RF9Cd0UlMjIlN0Q=',
        'refresh_token_cookie': refreshToken,
        'csrf_refresh_token': '9b39c907-2d44-4947-952b-83e8b2b2cf55',
        'login_type': 'email',
        '_token.local': token,
        '_refresh_token.local': refreshToken,
        'ab.storage.deviceId.a45e842b-5d46-46bf-8f41-2f75d6fd4b37': '%7B%22g%22%3A%22e10b0036-816e-3e47-fb0a-e136dbfadb43%22%2C%22c%22%3A1701936863775%2C%22l%22%3A1701959994791%7D',
        'ab.storage.userId.a45e842b-5d46-46bf-8f41-2f75d6fd4b37': '%7B%22g%22%3A%226366f46a-b525-46b6-9e07-af6dcba56c49%22%2C%22c%22%3A1701959994789%2C%22l%22%3A1701959994791%7D',
        'strategy': 'local',
        'airbridge_utm': '%7B%22channel%22%3A%22google%22%2C%22parameter%22%3A%7B%22medium%22%3A%22cpc%22%2C%22campaign%22%3A%22NEW_%uC790%uC0AC%uBA85_%uC218%uB3D9_PC%22%2C%22term%22%3A%22%uD06C%uB9BC%22%2C%22content%22%3A%22A.%20%uC790%uC0AC%uBA85_%uC218%uB3D9%22%7D%7D',
        'airbridge_utm_url': 'https%3A//kream.co.kr/%3Futm_source%3Dgoogle%26utm_medium%3Dcpc%26utm_campaign%3DNEW_%25EC%259E%2590%25EC%2582%25AC%25EB%25AA%2585_%25EC%2588%2598%25EB%258F%2599_PC%26utm_term%3D%25ED%2581%25AC%25EB%25A6%25BC%26utm_content%3DA.%2520%25EC%259E%2590%25EC%2582%25AC%25EB%25AA%2585_%25EC%2588%2598%25EB%258F%2599%26gclid%3DCjwKCAiA98WrBhAYEiwA2WvhOiE1zryUv6ZRIvcd0BhejZ0E4ryKJ3wqO5jqKtGfDGUGmT6W1CADIhoCPhkQAvD_BwE',
        'airbridge_utm_timestamp': '1701959996934',
        '_ga': 'GA1.3.248227678.1701661186',
        '_gac_UA-153398119-1': '1.1701959997.CjwKCAiA98WrBhAYEiwA2WvhOiE1zryUv6ZRIvcd0BhejZ0E4ryKJ3wqO5jqKtGfDGUGmT6W1CADIhoCPhkQAvD_BwE',
        'ab.storage.sessionId.a45e842b-5d46-46bf-8f41-2f75d6fd4b37': '%7B%22g%22%3A%225589cdf9-8744-d52e-0947-d98aae11f215%22%2C%22e%22%3A1701962031505%2C%22c%22%3A1701959994791%2C%22l%22%3A1701960231505%7D',
        'AMP_487619ef1d': 'JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjJmZmRiNTZkYS03NjYxLTQyZjAtOGQ4Ny00ZDFkMWI1OWQ0NmMlMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjI2MzY2ZjQ2YS1iNTI1LTQ2YjYtOWUwNy1hZjZkY2JhNTZjNDklMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzAxOTU5OTYzMDgxJTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTcwMTk2MDIzMTUwOSUyQyUyMmxhc3RFdmVudElkJTIyJTNBODglN0Q=',
        'wcs_bt': 's_59a6a417df3:1701960232',
        '_gat_gtag_UA_153398119_1': '1',
        'airbridge_session': '%7B%22id%22%3A%226ec19915-5bc6-464b-afe0-7307b9958696%22%2C%22timeout%22%3A1800000%2C%22start%22%3A1701959965244%2C%22end%22%3A1701960232744%7D',
        '_ga_SRFKTMTR0R': 'GS1.1.1701959964.8.1.1701960233.59.0.0',
        '_ga_5LYDPM15LW': 'GS1.1.1701959964.8.1.1701960233.59.0.0',
    }
    count=1
    dataList=[]
    while True:
        params = {
            'cursor': count,
            'per_page': '50',
            'sort': '',
            'request_key': '3e327bfd-49c7-4cfb-9f68-b6c795847f23',
        }
        try:
            response = requests.get('https://kream.co.kr/api/p/products/{}/bids'.format(productNo), params=params,cookies=cookies, headers=headers)
            print(response.text)
            results = json.loads(response.text)['items']
        except:
            print("더없다")
            break

        for result in results:
            try:
                price=result['price']
            except:
                price=""
            # print(price)
            try:
                size=extract_characters(result['option'])
            except:
                size=""
            # print(size)
            try:
                quantity=result['quantity']
            except:
                quantity=""
            # print(quantity)
            # try:
            #     immediate=result['is_immediate_delivery_item']
            # except:
            #     immediate=""
            # print(immediate)
            data={'category':"GM",'price':price,'size':size,'quantity':quantity}
            # print(data)
            dataList.append(data)
        if count >= GMScroll:
            print("스크롤채움")
            break
        count+=1
        time.sleep(random.randint(10, 15) * 0.1)
    return dataList
def SendMail(filepath):

    smtp_server = 'smtp.naver.com'
    smtp_port = 587

    # 네이버 이메일 계정 정보
    username = 'civilkwak@naver.com'  # 클라이언트 정보 입력
    password = '!dkagh5010'  # 클라이언트 정보 입력

    # receiver='wsgt17@naver.com'
    receiver='civilkwak@naver.com'
    # receiver=email

    # username = 'hellfir2@naver.com'  # 클라이언트 정보 입력
    # password = 'dlwndwo1!'  # 클라이언트 정보 입력
    # =================커스터마이징
    try:
        to_mail = receiver
    except:
        print("메일주소없음")
        return

    # =================

    # 메일 수신자 정보
    to_email = receiver

    # 참조자 정보
    cc_email = 'ljj3347@naver.com'

    # 메일 본문 및 제목 설정
    contentList=[]

    content="\n".join(contentList)


    # MIMEMultipart 객체 생성
    timeNow=datetime.datetime.now().strftime("%Y년%m월%d일 %H시%M분%S초")
    msg = MIMEMultipart('alternative')
    msg["Subject"] = "[결과]크림 상품 크롤링 (현재시각:{})".format(timeNow)  # 메일 제목
    msg['From'] = username
    msg['To'] = to_email
    msg['Cc'] = cc_email  # 참조 이메일 주소 추가
    msg.attach(MIMEText(content, 'plain'))

    # 파일 첨부
    part = MIMEBase('application', 'octet-stream')
    with open(filepath, 'rb') as file:
        part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename={filepath}')
    msg.attach(part)

    # SMTP 서버 연결 및 로그인
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(username, password)
    # 이메일 전송 (수신자와 참조자 모두에게 전송)
    to_and_cc_emails = [to_email] + [cc_email]
    server.sendmail(username, to_and_cc_emails, msg.as_string())
    # SMTP 서버 연결 종료
    server.quit()
    print("전송완료")



count=0
firstFlag=True
while True:
    print("대기중...")
    count+=1
    time.sleep(1)
    if count>=90000 or firstFlag==True:
        cookies={
        'i18n_redirected': 'kr',
        '_fwb': '53Fihu8lGaq0KdYC9zdmgQ.1704327945391',
        'afUserId': 'a03fa8b1-7200-4048-8b91-5c1f2148d240-p',
        'airbridge_device_alias': '%7B%22amplitude_device_id%22%3A%2241bf9ef6-b793-402d-a489-3299161a9bf0%22%7D',
        'AF_SYNC': '1704327946140',
        '_fbp': 'fb.2.1704327949716.1158384894',
        'ab.storage.deviceId.a45e842b-5d46-46bf-8f41-2f75d6fd4b37': '%7B%22g%22%3A%22a3e13174-64f4-98a9-7887-9f7f7cd4e4c1%22%2C%22c%22%3A1704327954524%2C%22l%22%3A1704328015759%7D',
        'ab.storage.userId.a45e842b-5d46-46bf-8f41-2f75d6fd4b37': '%7B%22g%22%3A%2200bbc1a3-69e7-461b-8d05-34353f86ace0%22%2C%22c%22%3A1704328015758%2C%22l%22%3A1704328015759%7D',
        'did': '62c963a0-bdfd-488d-b8a8-5bcf1c8120dd',
        'AMP_MKTG_487619ef1d': 'JTdCJTdE',
        '_token.local': 'false',
        '_refresh_token.local': 'false',
        '_gid': 'GA1.3.1184485473.1704430254',
        'strategy': 'local',
        'login_type': 'social',
        '_ga': 'GA1.3.482881550.1704327946',
        '_gat_gtag_UA_153398119_1': '1',
        'airbridge_session': '%7B%22id%22%3A%22d8d1b549-b05c-427a-b14d-cae8840d3e19%22%2C%22timeout%22%3A1800000%2C%22start%22%3A1704430254282%2C%22end%22%3A1704430400653%7D',
        'ab.storage.sessionId.a45e842b-5d46-46bf-8f41-2f75d6fd4b37': '%7B%22g%22%3A%22025e3913-2b7b-264a-3d88-4629c462cfa5%22%2C%22e%22%3A1704432220163%2C%22c%22%3A1704430253489%2C%22l%22%3A1704430420163%7D',
        'AMP_487619ef1d': 'JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI0MWJmOWVmNi1iNzkzLTQwMmQtYTQ4OS0zMjk5MTYxYTliZjAlMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjIwMGJiYzFhMy02OWU3LTQ2MWItOGQwNS0zNDM1M2Y4NmFjZTAlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzA0NDMwMjUyOTQ4JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTcwNDQzMDQyMDE2NCUyQyUyMmxhc3RFdmVudElkJTIyJTNBMjElN0Q=',
        'wcs_bt': 's_59a6a417df3:1704430420',
        '_ga_SRFKTMTR0R': 'GS1.1.1704430253.2.1.1704430421.38.0.0',
        '_ga_5LYDPM15LW': 'GS1.1.1704430253.2.1.1704430421.38.0.0',
        }

        # ============전체상품리스트 가져오기
        # productIdList=GetIDs()


        # # ================상세정보에서 1차 필터링
        # with open ('productIdList.json', "r",encoding='utf-8-sig') as f:
        #     productDataList = json.load(f)
        # filteredList=[]
        # for index,productData in enumerate(productDataList):
        #     url='https://www.kream.co.kr/products/{}'.format(productData['productId'])
        #     print("url:",url,"/ url_TYPE:",type(url))
        #     productId=productData['productId']
        #     checkResult,originPrice=GetBasicData(cookies,productId)
        #     if checkResult==True:
        #         data={'productId':productId,'title':productData['title'],'modelCode':productData['modelCode'],'brand':productData['brand'],'originPrice':originPrice}
        #         filteredList.append(data)
        #         with open('filteredList.json', 'w',encoding='utf-8-sig') as f:
        #             json.dump(filteredList, f, indent=2,ensure_ascii=False)
        #
        #     print("==========={}/{}=================".format(index+1,len(productDataList)))
        #     time.sleep(random.randint(5,10)*0.1)

        #========================로그인하기
        with open ('filteredList.json', "r",encoding='utf-8-sig') as f:
            filteredList = json.load(f)
        GetToken()
        with open('tokenData.json', "r", encoding='utf-8-sig') as f:
            tokenData = json.load(f)
        token = tokenData['access_token']
        refreshToken = tokenData['refresh_token']
        print("토큰가져오기완료1")


        wb=openpyxl.Workbook()
        ws=wb.active
        columName=['확인날짜','상품명','발매가','판매가','사이즈','브랜드','모델코드','URL']
        ws.append(columName)
        for filteredElem in filteredList:
            headers = {
            'authority': 'www.kream.co.kr',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'authorization': 'Bearer {}'.format(token),
            # 'cookie': 'afUserId=cd0a42c4-1500-45e1-a551-746510b06fbf-p; _fbp=fb.2.1691128991158.731815584; i18n_redirected=kr; _gid=GA1.3.1693048652.1694520729; AF_SYNC=1694520730521; did=75448f17-2f9f-4c5d-bb93-45a642909201; AMP_MKTG_487619ef1d=JTdCJTdE; _gat_gtag_UA_153398119_1=1; _token.social_naver=false; _refresh_token.social_naver=false; refresh_token_cookie=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5NDcwNDE1OCwianRpIjoiMWFkNGQ5NzUtZTJlYi00NjExLWFjZDYtYTU2OTYwOTVmZmEwIiwidHlwZSI6InJlZnJlc2giLCJpZGVudGl0eSI6NTc4NjMxMiwibmJmIjoxNjk0NzA0MTU4LCJjc3JmIjoiNWM2YTYzODMtOTM3My00NjlkLWIwN2YtNzZmOWIxMjQwMWJiIiwiZXhwIjoxNjk0NzkwNTU4LCJ1YyI6eyJzYWZlIjp0cnVlfX0.vOXtvTNZX4-H_qcHPgxMOXA3lEma3XPtK5Q36PiB1jg; csrf_refresh_token=5c6a6383-9373-469d-b07f-76f9b12401bb; login_type=social; _token.local=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6dHJ1ZSwiaWF0IjoxNjk0NzA0MTU4LCJqdGkiOiJiZDI5YzYzOS02NTFlLTQ3ODktYjQ4YS1lMzUwNmI1YjhiNmQiLCJ0eXBlIjoiYWNjZXNzIiwiaWRlbnRpdHkiOjU3ODYzMTIsIm5iZiI6MTY5NDcwNDE1OCwiY3NyZiI6IjBmNjg4NzZjLWI3OGUtNGMwZi1hNTQ3LTUzNmQ2OGNlODk5MCIsImV4cCI6MTY5NDcxMTM1OCwidWMiOnsic2FmZSI6dHJ1ZX19.YHdNCKgtZgsaOFj89S4ZZBhquXVGyzJx1pOhNCeBNTc; _refresh_token.local=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5NDcwNDE1OCwianRpIjoiMWFkNGQ5NzUtZTJlYi00NjExLWFjZDYtYTU2OTYwOTVmZmEwIiwidHlwZSI6InJlZnJlc2giLCJpZGVudGl0eSI6NTc4NjMxMiwibmJmIjoxNjk0NzA0MTU4LCJjc3JmIjoiNWM2YTYzODMtOTM3My00NjlkLWIwN2YtNzZmOWIxMjQwMWJiIiwiZXhwIjoxNjk0NzkwNTU4LCJ1YyI6eyJzYWZlIjp0cnVlfX0.vOXtvTNZX4-H_qcHPgxMOXA3lEma3XPtK5Q36PiB1jg; strategy=local; ab.storage.sessionId.8d5d348c-fc26-4528-a5b4-627447ffad5a=%7B%22g%22%3A%2231ec7f48-fd10-7a63-e63e-4a55e6ad6dfb%22%2C%22e%22%3A1694705960071%2C%22c%22%3A1694704160071%2C%22l%22%3A1694704160071%7D; ab.storage.deviceId.8d5d348c-fc26-4528-a5b4-627447ffad5a=%7B%22g%22%3A%227cca38ec-4ce8-06d5-d010-af23569e6653%22%2C%22c%22%3A1691128725307%2C%22l%22%3A1694704160072%7D; ab.storage.userId.8d5d348c-fc26-4528-a5b4-627447ffad5a=%7B%22g%22%3A%2200bbc1a3-69e7-461b-8d05-34353f86ace0%22%2C%22c%22%3A1694528997964%2C%22l%22%3A1694704160072%7D; _ga=GA1.3.975923776.1691128716; AMP_487619ef1d=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI5YTA2NDVkOS0yZmU5LTQzMzYtYWYyMi00M2VlMzQ3NTBlYjMlMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjIwMGJiYzFhMy02OWU3LTQ2MWItOGQwNS0zNDM1M2Y4NmFjZTAlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNjk0NzA0MTI1MTA3JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTY5NDcwNDE2NTQ0MSUyQyUyMmxhc3RFdmVudElkJTIyJTNBMTYxJTdE; wcs_bt=s_59a6a417df3:1694704168; _ga_SRFKTMTR0R=GS1.1.1694704125.38.1.1694704169.16.0.0; _ga_5LYDPM15LW=GS1.1.1694704125.38.1.1694704169.16.0.0',
            'referer': 'https://www.kream.co.kr/products/21935',
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            'x-kream-api-version': '26',
            'x-kream-client-datetime': '20230915000940+0900',
            'x-kream-device-id': 'web;75448f17-2f9f-4c5d-bb93-45a642909201',
            }
            GMScroll=1
            productNo=filteredElem['productId']
            try:
                dataList = GetGMTransaction(GMScroll, token, refreshToken, headers, productNo)
                print("가져오기성공")
                time.sleep(random.randint(1,2))
                # pprint.pprint(dataList)
                with open('dataList.json', 'w', encoding='utf-8-sig') as f:
                    json.dump(dataList, f, indent=2, ensure_ascii=False)
            except:
                print("구매정보가져오기실패")
                continue
            timeNow=datetime.datetime.now().strftime("%Y%m%d %H:%M")
            for data in dataList:
                # columName = ['확인날짜', '상품명', '발매가', '옵션', '판매가', '브랜드', '모델코드', 'URL']
                dataRow=[timeNow,filteredElem['title'],filteredElem['originPrice'],data['price'],data['size'],filteredElem['brand'],filteredElem['modelCode'],"https://www.kream.co.kr/products/{}".format(productNo)]
                ws.append(dataRow)
                print("dataRow:",dataRow,"/ dataRow_TYPE:",type(dataRow))
            filepath='result.xlsx'
            wb.save(filepath)
        SendMail(filepath)
    count=0
    firstFlag=False
