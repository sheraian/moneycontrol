import json
from wsgiref import headers

import scrapy
from pip._internal.utils import urls


class MyspiderSpider(scrapy.Spider):
    name = "myspider"
    allowed_domains = ["moneycontrol.com"]
    def start_requests(self):
        # url="https://www.moneycontrol.com/india/stockpricequote/A"

        cookies={
            'A18ID': '1735825619250.264983',
            'MC_PPID_LOGIC': 'normaluser21193130293479932mcids',
            '_gid': 'GA1.2.1512463253.1735825620',
            '_io_ht_r': '1',
            '__io_r': 'freelancer.com',
            '__io_first_source': 'freelancer.com',
            '__io_lv': '1735825621160',
            '__io': '672340ac8.2e690a47c_1735825621162',
            '__io_pr_utm_campaign': '%7B%22referrerHostname%22%3A%22www.freelancer.com%22%7D',
            '__io_unique_43938': '2',
            '_cb': 'uEdv6_posICHZXJZ',
            '_sharedID': 'df2d8ae1-40ca-4aa9-a03f-7dbd8fd3a35a',
            '_sharedID_cst': 'zix7LPQsHA%3D%3D',
            'WZRK_G': 'b6165915d3ec415f91f896a307bcae61',
            '_cc_id': '68ba02dc438241c4aef7a25b279dc8cf',
            'panoramaId_expiry': '1736430442310',
            'panoramaId': '2f21661ee2e28a9bb29268d3a07f4945a7028febb4248374d9d2a87192b9f24d',
            'panoramaIdType': 'panoIndiv',
            'cto_bundle': 'Mn8lq18xZjJFQ3pXQXJoNUlUY3JDcVNpeThmJTJGcnk5ejhDZk80RUZzaTJzdzJxMmhMa0o4QnNha1BOaUVlNHNqd1lrYzI5bVhTQ0xUUVFtNzFuMmd0R1EwdHhRYlkwU0gydlpqbk5DOVg4bGZTV2QlMkIzJTJGS2tWZnI3JTJGNFdkc3pNNkhUOWtBTEludVVYTWFYSTR0VHNRSFFDRTFjSHJYN21vaDdzTzZyUVhPJTJGdjZvZUJHYXZQdDFXMVNTN1FjOUpyZFQ5NTgwaFFtMmJCbTg5V1J3cFlWOWRWa00xdURzOG1QcllLRlJIQlUyandicHJqTEUwRDJ3U2FiRUhQZU5JeGZOa0lyYWclMkJYbzFtWHJqYW9NSUduSG1CMVFBQSUzRCUzRA',
            '__io_session_id': '5355c759f.d1b1a83f3_1735842400408',
            '__io_visit_43938': '1',
            '__io_d': '2_883510103',
            '__io_nav_state43938': '%7B%22current%22%3A%22%2Findia%2Fstockpricequote%2FA%22%2C%22currentDomain%22%3A%22www.moneycontrol.com%22%2C%22previous%22%3A%22%2Findia%2Fstockpricequote%2FA%22%2C%22previousDomain%22%3A%22www.moneycontrol.com%22%7D',
            'PHPSESSID': 'u78mresd4e1739ehomt51hpic7',
            'MC_INTERSTITIAL_DFP_AD_LOGIC_20250102': '{"0":"https://www.moneycontrol.com/india/stockpricequote/miscellaneous/amfebcon/F03"}',
            '_gcl_au': '1.1.1001301931.1735842582',
            'nousersess': 'dou6dgdbdeystf1n',
            '__gads': 'ID=875140f57be95c97:T=1735825634:RT=1735842764:S=ALNI_MZkP9ZL5-LQc1rKXKFNJaLJQwIKvw',
            '__gpi': 'UID=00000fc3f3247ce6:T=1735825634:RT=1735842764:S=ALNI_MY-2qPSsiJQArerekf4hLtPQNiUPQ',
            '__eoi': 'ID=9233f3eceb4d4cf0:T=1735825634:RT=1735842765:S=AA-AfjZ0mScKAKYyIrVLt0zXIKmf',
            '_ga_HXEC5QES15': 'GS1.1.1735842601.1.1.1735842782.0.0.0',
            '_ga_8J9SC9WB3T': 'GS1.1.1735842594.1.1.1735842784.60.0.0',
            '_ga_4S48PBY299': 'GS1.1.1735842583.1.1.1735842786.60.0.0',
            '_ga': 'GA1.2.230106381.1735825620',
            'dtCookie': 'v_4_srv_7_sn_03B8B9632C75B2E3A9F89EE095E3F07B_perc_100000_ol_0_mul_1_app-3A15ca68b27f59163f_1',
            '_chartbeat2': '.1735825621352.1735842837733.1.CyVYRIDI2hv8CYkCKFDbXmnaDIwY4C.1',
            '_cb_svref': 'external',
            'WZRK_S_86Z-5ZR-RK6Z': '%7B%22p%22%3A7%2C%22s%22%3A1735842467%2C%22t%22%3A1735842838%7D',
            'FCNEC': '%5B%5B%22AKsRol9-FlNedoM1dZK1cuHqjLBjgVZZv0F6e8iw535VubERSX54JuPUXiKAmLcQQJf7Rc8gnFex3emUdebfTiJ8r-pk0ZvxGplbWCRt1cpfK0khI9ihoNsH8vk41NHs6weHn5CSz7kc-FZeOCD1UvE18L0vkZp3DA%3D%3D%22%5D%5D',
        }
        headers={
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            # 'cookie': 'A18ID=1735825619250.264983; MC_PPID_LOGIC=normaluser21193130293479932mcids; _gid=GA1.2.1512463253.1735825620; _io_ht_r=1; __io_r=freelancer.com; __io_first_source=freelancer.com; __io_lv=1735825621160; __io=672340ac8.2e690a47c_1735825621162; __io_pr_utm_campaign=%7B%22referrerHostname%22%3A%22www.freelancer.com%22%7D; __io_unique_43938=2; _cb=uEdv6_posICHZXJZ; _sharedID=df2d8ae1-40ca-4aa9-a03f-7dbd8fd3a35a; _sharedID_cst=zix7LPQsHA%3D%3D; WZRK_G=b6165915d3ec415f91f896a307bcae61; _cc_id=68ba02dc438241c4aef7a25b279dc8cf; panoramaId_expiry=1736430442310; panoramaId=2f21661ee2e28a9bb29268d3a07f4945a7028febb4248374d9d2a87192b9f24d; panoramaIdType=panoIndiv; cto_bundle=Mn8lq18xZjJFQ3pXQXJoNUlUY3JDcVNpeThmJTJGcnk5ejhDZk80RUZzaTJzdzJxMmhMa0o4QnNha1BOaUVlNHNqd1lrYzI5bVhTQ0xUUVFtNzFuMmd0R1EwdHhRYlkwU0gydlpqbk5DOVg4bGZTV2QlMkIzJTJGS2tWZnI3JTJGNFdkc3pNNkhUOWtBTEludVVYTWFYSTR0VHNRSFFDRTFjSHJYN21vaDdzTzZyUVhPJTJGdjZvZUJHYXZQdDFXMVNTN1FjOUpyZFQ5NTgwaFFtMmJCbTg5V1J3cFlWOWRWa00xdURzOG1QcllLRlJIQlUyandicHJqTEUwRDJ3U2FiRUhQZU5JeGZOa0lyYWclMkJYbzFtWHJqYW9NSUduSG1CMVFBQSUzRCUzRA; __io_session_id=5355c759f.d1b1a83f3_1735842400408; __io_visit_43938=1; __io_d=2_883510103; __io_nav_state43938=%7B%22current%22%3A%22%2Findia%2Fstockpricequote%2FA%22%2C%22currentDomain%22%3A%22www.moneycontrol.com%22%2C%22previous%22%3A%22%2Findia%2Fstockpricequote%2FA%22%2C%22previousDomain%22%3A%22www.moneycontrol.com%22%7D; PHPSESSID=u78mresd4e1739ehomt51hpic7; MC_INTERSTITIAL_DFP_AD_LOGIC_20250102={"0":"https://www.moneycontrol.com/india/stockpricequote/miscellaneous/amfebcon/F03"}; _gcl_au=1.1.1001301931.1735842582; nousersess=dou6dgdbdeystf1n; __gads=ID=875140f57be95c97:T=1735825634:RT=1735842764:S=ALNI_MZkP9ZL5-LQc1rKXKFNJaLJQwIKvw; __gpi=UID=00000fc3f3247ce6:T=1735825634:RT=1735842764:S=ALNI_MY-2qPSsiJQArerekf4hLtPQNiUPQ; __eoi=ID=9233f3eceb4d4cf0:T=1735825634:RT=1735842765:S=AA-AfjZ0mScKAKYyIrVLt0zXIKmf; _ga_HXEC5QES15=GS1.1.1735842601.1.1.1735842782.0.0.0; _ga_8J9SC9WB3T=GS1.1.1735842594.1.1.1735842784.60.0.0; _ga_4S48PBY299=GS1.1.1735842583.1.1.1735842786.60.0.0; _ga=GA1.2.230106381.1735825620; dtCookie=v_4_srv_7_sn_03B8B9632C75B2E3A9F89EE095E3F07B_perc_100000_ol_0_mul_1_app-3A15ca68b27f59163f_1; _chartbeat2=.1735825621352.1735842837733.1.CyVYRIDI2hv8CYkCKFDbXmnaDIwY4C.1; _cb_svref=external; WZRK_S_86Z-5ZR-RK6Z=%7B%22p%22%3A7%2C%22s%22%3A1735842467%2C%22t%22%3A1735842838%7D; FCNEC=%5B%5B%22AKsRol9-FlNedoM1dZK1cuHqjLBjgVZZv0F6e8iw535VubERSX54JuPUXiKAmLcQQJf7Rc8gnFex3emUdebfTiJ8r-pk0ZvxGplbWCRt1cpfK0khI9ihoNsH8vk41NHs6weHn5CSz7kc-FZeOCD1UvE18L0vkZp3DA%3D%3D%22%5D%5D',
            'priority': 'u=0, i',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }
        for char in range(65, 91):
            print(chr(char))
            yield scrapy.Request(url=f"https://www.moneycontrol.com/india/stockpricequote/{chr(char)}", headers=headers, cookies=cookies, callback=self.parse)


    def parse(self, response):
        links = response.xpath('//a[@class="bl_12"]/@href').getall()
        # print(links)
        print(response.status)
        print(len(links))
        cookies = {
            'A18ID': '1735825619250.264983',
            'MC_PPID_LOGIC': 'normaluser21193130293479932mcids',
            '_gid': 'GA1.2.1512463253.1735825620',
            '_io_ht_r': '1',
            '__io_r': 'freelancer.com',
            '__io_first_source': 'freelancer.com',
            '__io_lv': '1735825621160',
            '__io': '672340ac8.2e690a47c_1735825621162',
            '__io_pr_utm_campaign': '%7B%22referrerHostname%22%3A%22www.freelancer.com%22%7D',
            '__io_unique_43938': '2',
            '_cb': 'uEdv6_posICHZXJZ',
            '_sharedID': 'df2d8ae1-40ca-4aa9-a03f-7dbd8fd3a35a',
            '_sharedID_cst': 'zix7LPQsHA%3D%3D',
            'WZRK_G': 'b6165915d3ec415f91f896a307bcae61',
            '_cc_id': '68ba02dc438241c4aef7a25b279dc8cf',
            'panoramaId_expiry': '1736430442310',
            'panoramaId': '2f21661ee2e28a9bb29268d3a07f4945a7028febb4248374d9d2a87192b9f24d',
            'panoramaIdType': 'panoIndiv',
            'cto_bundle': 'Mn8lq18xZjJFQ3pXQXJoNUlUY3JDcVNpeThmJTJGcnk5ejhDZk80RUZzaTJzdzJxMmhMa0o4QnNha1BOaUVlNHNqd1lrYzI5bVhTQ0xUUVFtNzFuMmd0R1EwdHhRYlkwU0gydlpqbk5DOVg4bGZTV2QlMkIzJTJGS2tWZnI3JTJGNFdkc3pNNkhUOWtBTEludVVYTWFYSTR0VHNRSFFDRTFjSHJYN21vaDdzTzZyUVhPJTJGdjZvZUJHYXZQdDFXMVNTN1FjOUpyZFQ5NTgwaFFtMmJCbTg5V1J3cFlWOWRWa00xdURzOG1QcllLRlJIQlUyandicHJqTEUwRDJ3U2FiRUhQZU5JeGZOa0lyYWclMkJYbzFtWHJqYW9NSUduSG1CMVFBQSUzRCUzRA',
            '__io_session_id': '5355c759f.d1b1a83f3_1735842400408',
            'PHPSESSID': 'u78mresd4e1739ehomt51hpic7',
            '_gcl_au': '1.1.1001301931.1735842582',
            'nousersess': 'dou6dgdbdeystf1n',
            'MC_INTERSTITIAL_DFP_AD_LOGIC_20250102': '{"0":"https://www.moneycontrol.com/india/stockpricequote/miscellaneous/amfebcon/F03","1":"https://www.moneycontrol.com/india/stockpricequote/finance-leasinghire-purchase/armanfinancialservices/AFS04"}',
            '_ga_4S48PBY299': 'GS1.1.1735842583.1.1.1735843566.60.0.0',
            '__gads': 'ID=875140f57be95c97:T=1735825634:RT=1735843575:S=ALNI_MZkP9ZL5-LQc1rKXKFNJaLJQwIKvw',
            '__gpi': 'UID=00000fc3f3247ce6:T=1735825634:RT=1735843575:S=ALNI_MY-2qPSsiJQArerekf4hLtPQNiUPQ',
            '__eoi': 'ID=9233f3eceb4d4cf0:T=1735825634:RT=1735843575:S=AA-AfjZ0mScKAKYyIrVLt0zXIKmf',
            'WZRK_S_86Z-5ZR-RK6Z': '%7B%22p%22%3A9%2C%22s%22%3A1735842467%2C%22t%22%3A1735843576%7D',
            '_chartbeat2': '.1735825621352.1735843578332.1.BT1I7mD5GFsAx5Hg_DfQFTD1SK3Y.1',
            '_cb_svref': 'external',
            'dtCookie': 'v_4_srv_2_sn_03B8B9632C75B2E3A9F89EE095E3F07B_perc_100000_ol_0_mul_1_app-3A15ca68b27f59163f_1',
            'RE_KJ_CC': 'XvZbbTwv',
            'FCNEC': '%5B%5B%22AKsRol_sceUNlIUM519HBOgSmBNLMNeuNzfVQ6dpru0Qm-OYglfYGm6ZrKgEt2t5mbMAWxwROonWX5OYSh-VAa_TAW3jupwX9z0lXPr8yeoEXL7kxyNzg-rLPXAEGVnu_zffojUiJ-GkcfUOILaZG28N4dt1a_Nn2A%3D%3D%22%5D%5D',
            '_ga': 'GA1.2.230106381.1735825620',
            '_ga_8J9SC9WB3T': 'GS1.1.1735842594.1.1.1735843817.32.0.0',
            '_ga_HXEC5QES15': 'GS1.1.1735842601.1.1.1735843817.0.0.0',
        }

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            # 'cookie': 'A18ID=1735825619250.264983; MC_PPID_LOGIC=normaluser21193130293479932mcids; _gid=GA1.2.1512463253.1735825620; _io_ht_r=1; __io_r=freelancer.com; __io_first_source=freelancer.com; __io_lv=1735825621160; __io=672340ac8.2e690a47c_1735825621162; __io_pr_utm_campaign=%7B%22referrerHostname%22%3A%22www.freelancer.com%22%7D; __io_unique_43938=2; _cb=uEdv6_posICHZXJZ; _sharedID=df2d8ae1-40ca-4aa9-a03f-7dbd8fd3a35a; _sharedID_cst=zix7LPQsHA%3D%3D; WZRK_G=b6165915d3ec415f91f896a307bcae61; _cc_id=68ba02dc438241c4aef7a25b279dc8cf; panoramaId_expiry=1736430442310; panoramaId=2f21661ee2e28a9bb29268d3a07f4945a7028febb4248374d9d2a87192b9f24d; panoramaIdType=panoIndiv; cto_bundle=Mn8lq18xZjJFQ3pXQXJoNUlUY3JDcVNpeThmJTJGcnk5ejhDZk80RUZzaTJzdzJxMmhMa0o4QnNha1BOaUVlNHNqd1lrYzI5bVhTQ0xUUVFtNzFuMmd0R1EwdHhRYlkwU0gydlpqbk5DOVg4bGZTV2QlMkIzJTJGS2tWZnI3JTJGNFdkc3pNNkhUOWtBTEludVVYTWFYSTR0VHNRSFFDRTFjSHJYN21vaDdzTzZyUVhPJTJGdjZvZUJHYXZQdDFXMVNTN1FjOUpyZFQ5NTgwaFFtMmJCbTg5V1J3cFlWOWRWa00xdURzOG1QcllLRlJIQlUyandicHJqTEUwRDJ3U2FiRUhQZU5JeGZOa0lyYWclMkJYbzFtWHJqYW9NSUduSG1CMVFBQSUzRCUzRA; __io_session_id=5355c759f.d1b1a83f3_1735842400408; PHPSESSID=u78mresd4e1739ehomt51hpic7; _gcl_au=1.1.1001301931.1735842582; nousersess=dou6dgdbdeystf1n; MC_INTERSTITIAL_DFP_AD_LOGIC_20250102={"0":"https://www.moneycontrol.com/india/stockpricequote/miscellaneous/amfebcon/F03","1":"https://www.moneycontrol.com/india/stockpricequote/finance-leasinghire-purchase/armanfinancialservices/AFS04"}; _ga_4S48PBY299=GS1.1.1735842583.1.1.1735843566.60.0.0; __gads=ID=875140f57be95c97:T=1735825634:RT=1735843575:S=ALNI_MZkP9ZL5-LQc1rKXKFNJaLJQwIKvw; __gpi=UID=00000fc3f3247ce6:T=1735825634:RT=1735843575:S=ALNI_MY-2qPSsiJQArerekf4hLtPQNiUPQ; __eoi=ID=9233f3eceb4d4cf0:T=1735825634:RT=1735843575:S=AA-AfjZ0mScKAKYyIrVLt0zXIKmf; WZRK_S_86Z-5ZR-RK6Z=%7B%22p%22%3A9%2C%22s%22%3A1735842467%2C%22t%22%3A1735843576%7D; _chartbeat2=.1735825621352.1735843578332.1.BT1I7mD5GFsAx5Hg_DfQFTD1SK3Y.1; _cb_svref=external; dtCookie=v_4_srv_2_sn_03B8B9632C75B2E3A9F89EE095E3F07B_perc_100000_ol_0_mul_1_app-3A15ca68b27f59163f_1; RE_KJ_CC=XvZbbTwv; FCNEC=%5B%5B%22AKsRol_sceUNlIUM519HBOgSmBNLMNeuNzfVQ6dpru0Qm-OYglfYGm6ZrKgEt2t5mbMAWxwROonWX5OYSh-VAa_TAW3jupwX9z0lXPr8yeoEXL7kxyNzg-rLPXAEGVnu_zffojUiJ-GkcfUOILaZG28N4dt1a_Nn2A%3D%3D%22%5D%5D; _ga=GA1.2.230106381.1735825620; _ga_8J9SC9WB3T=GS1.1.1735842594.1.1.1735843817.32.0.0; _ga_HXEC5QES15=GS1.1.1735842601.1.1.1735843817.0.0.0',
            'priority': 'u=0, i',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }
        for url in links:
            yield scrapy.Request(url=url, callback=self.parse_detail, headers=headers, cookies=cookies)


    def parse_detail(self,response):
        URL = response.url
        parts = URL.split("/")
        scId = parts[-1]
        def clean_field(xpath_expr):
            result = response.xpath(xpath_expr).get()
            return result.strip() if result else 'N/A'

        def clean_numeric_field(xpath_expr, default_value='0.00'):
            result = response.xpath(xpath_expr).get()
            return result.strip() if result else default_value

        # Extract and clean the values from the page
        open_value = clean_numeric_field('//td[text()="Open"]/following-sibling::td/text()')
        previous_close = clean_numeric_field('//td[text()="Previous Close"]/following-sibling::td/text()')
        volume = clean_numeric_field('//td[text()="Volume"]/following-sibling::td/text()')
        value_lacs = clean_numeric_field('//td[text()="Value (Lacs)"]/following-sibling::td/text()')
        vwap = clean_field('//td[text()="VWAP"]/following-sibling::td/text()')
        beta = clean_numeric_field('//td[text()="Beta"]/following-sibling::td/div[@class="nsebeta"]/text()')
        market_cap = clean_numeric_field('//td[text()="Mkt Cap (Rs. Cr.)"]/following-sibling::td/text()')
        high = clean_numeric_field('//td[text()="High"]/following-sibling::td/text()')
        low = clean_numeric_field('//td[text()="Low"]/following-sibling::td/text()')
        uc_limit = clean_numeric_field('//td[text()="UC Limit"]/following-sibling::td/text()')
        lc_limit = clean_numeric_field('//td[text()="LC Limit"]/following-sibling::td/text()')
        week_52_high = clean_numeric_field('//td[text()="52 Week High"]/following-sibling::td/text()')
        week_52_low = clean_numeric_field('//td[text()="52 Week Low"]/following-sibling::td/text()')
        face_value = clean_numeric_field('//td[text()="Face Value"]/following-sibling::td/text()')
        all_time_high = clean_numeric_field('//td[text()="All Time High"]/following-sibling::td/text()')
        all_time_low = clean_numeric_field('//td[text()="All Time Low"]/following-sibling::td/text()')
        avg_20d_volume = clean_numeric_field('//td[text()="20D Avg Volume"]/following-sibling::td/text()')
        avg_20d_delivery = clean_field('//td[text()="20D Avg Delivery(%)"]/following-sibling::td/text()')
        book_value_per_share = clean_field('//td[text()="Book Value Per Share"]/following-sibling::td/text()')
        dividend_yield = clean_field('//td[text()="Dividend Yield"]/following-sibling::td/text()')

        # Create a dictionary with the cleaned values
        stock_data = {
            'url':URL,
            'open': open_value,
            'previous_close': previous_close,
            'volume': volume,
            'value_lacs': value_lacs,
            'vwap': vwap,
            'beta': beta,
            'market_cap': market_cap,
            'high': high,
            'low': low,
            'uc_limit': uc_limit,
            'lc_limit': lc_limit,
            '52_week_high': week_52_high,
            '52_week_low': week_52_low,
            'face_value': face_value,
            'all_time_high': all_time_high,
            'all_time_low': all_time_low,
            'avg_20d_volume': avg_20d_volume,
            'avg_20d_delivery': avg_20d_delivery,
            'book_value_per_share': book_value_per_share,
            'dividend_yield': dividend_yield,
        }
        headers = {
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-language": "en-US,en;q=0.9",
            "auth-token": "xGQW9izz4G65y9e1ZoqT5CyjI7h250Zm33zQhJh4WX15GJF78u1otbyVRbjdioHQAErGuBzvRWcHtQwqOWboUQ",
            "if-none-match": 'W/"e8-OBvTANKcvJWZUJFr8r70odvibro"',
            "origin": "https://www.moneycontrol.com",
            "priority": "u=1, i",
            "referer": "https://www.moneycontrol.com/",
            "sec-ch-ua": '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"macOS"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
        }

        yield scrapy.Request(url=f"https://api.moneycontrol.com/mcapi/v1/stock/estimates/analyst-rating?deviceType=W&scId={scId}&ex=N",headers=headers,callback=self.parse_forcast,dont_filter=True,meta={"scId":scId,"stock_data":stock_data})

    def parse_forcast(self, response):
        stock_data = response.meta.get('stock_data')
        scId = response.meta.get('scId')
        if response.status==204:
            headers = {
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'en-US,en;q=0.9',
                'auth-token': 'xGQW9izz4G65y9e1ZoqT5CyjI7h250Zm33zQhJh4WX15GJF78u1otbyVRbjdioHQAErGuBzvRWcHtQwqOWboUQ',
                'if-none-match': 'W/"b6e-1YmJy2wW1XtJ2/KQbxUVKE77oj0"',
                'origin': 'https://www.moneycontrol.com',
                'priority': 'u=1, i',
                'referer': 'https://www.moneycontrol.com/',
                'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
            }
            yield scrapy.Request(
                url=f"https://api.moneycontrol.com/mcapi/technicals/v2/details?scId={scId}&dur=D&deviceType=W",
                callback=self.get_scId_details, headers=headers, meta={"scId": scId, "stock_data": stock_data})

        else:

            forecast = {}
            data = json.loads(response.text)
            filtered_data = {
                item['name']: int(item['value']) for item in data['data']['ratings']
            }
            forecast['Analyst Rating'] = filtered_data
            headers = {
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'en-US,en;q=0.9',
                'auth-token': 'xGQW9izz4G65y9e1ZoqT5CyjI7h250Zm33zQhJh4WX15GJF78u1otbyVRbjdioHQAErGuBzvRWcHtQwqOWboUQ',
                'if-none-match': 'W/"484-FmQ6msXlo93La09wfnYGfxIvFIk"',
                'origin': 'https://www.moneycontrol.com',
                'priority': 'u=1, i',
                'referer': 'https://www.moneycontrol.com/',
                'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
            }
            yield scrapy.Request(
                url=f"https://api.moneycontrol.com/mcapi/v1/stock/estimates/earning-forecast?scId={scId}&ex=N&deviceType=W&frequency=12&financialType=S",
                headers=headers, callback=self.parse_earning, dont_filter=True,
                meta={"scId": scId, "stock_data": stock_data, 'forecast': forecast})

    def parse_earning(self, response):
        stock_data = response.meta.get('stock_data')
        scId = response.meta.get('scId')
        forecast=response.meta.get('forecast')
        if response.status != 200:
            stock_data['forecast'] = forecast
            headers = {
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'en-US,en;q=0.9',
                'auth-token': 'xGQW9izz4G65y9e1ZoqT5CyjI7h250Zm33zQhJh4WX15GJF78u1otbyVRbjdioHQAErGuBzvRWcHtQwqOWboUQ',
                'if-none-match': 'W/"b6e-1YmJy2wW1XtJ2/KQbxUVKE77oj0"',
                'origin': 'https://www.moneycontrol.com',
                'priority': 'u=1, i',
                'referer': 'https://www.moneycontrol.com/',
                'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
            }
            yield scrapy.Request(
                url=f"https://api.moneycontrol.com/mcapi/technicals/v2/details?scId={scId}&dur=D&deviceType=W",
                callback=self.get_scId_details, headers=headers, meta={"scId": scId, "stock_data": stock_data})
        else:
            data = json.loads(response.text)
            forecast['Earnings Forecast'] = data['data']
            headers = {
                "accept": "application/json, text/javascript, */*; q=0.01",
                "accept-language": "en-US,en;q=0.9",
                "auth-token": "xGQW9izz4G65y9e1ZoqT5CyjI7h250Zm33zQhJh4WX15GJF78u1otbyVRbjdioHQAErGuBzvRWcHtQwqOWboUQ",
                "origin": "https://www.moneycontrol.com",
                "priority": "u=1, i",
                "referer": "https://www.moneycontrol.com/",
                "sec-ch-ua": '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"macOS"',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-site",
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
            }
            yield scrapy.Request(
                url=f"https://api.moneycontrol.com/mcapi/v1/stock/estimates/valuation?deviceType=W&scId={scId}&ex=N&financialType=S",
                headers=headers, callback=self.parse_valuation,dont_filter=True,
                meta={"scId": scId, "stock_data": stock_data, 'forecast': forecast})

    def parse_valuation(self, response):
        stock_data = response.meta.get('stock_data')
        scId = response.meta.get('scId')
        forecast = response.meta.get('forecast')
        if response.status != 200:
            stock_data['forecast'] = forecast
            headers = {
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'en-US,en;q=0.9',
                'auth-token': 'xGQW9izz4G65y9e1ZoqT5CyjI7h250Zm33zQhJh4WX15GJF78u1otbyVRbjdioHQAErGuBzvRWcHtQwqOWboUQ',
                'if-none-match': 'W/"b6e-1YmJy2wW1XtJ2/KQbxUVKE77oj0"',
                'origin': 'https://www.moneycontrol.com',
                'priority': 'u=1, i',
                'referer': 'https://www.moneycontrol.com/',
                'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
            }
            yield scrapy.Request(
                url=f"https://api.moneycontrol.com/mcapi/technicals/v2/details?scId={scId}&dur=D&deviceType=W",
                callback=self.get_scId_details, headers=headers, meta={"scId": scId, "stock_data": stock_data})
        else:
            data = json.loads(response.text)
            forecast['Valuations'] = data['data']['list']
            headers = {
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'en-US,en;q=0.9',
                'auth-token': 'xGQW9izz4G65y9e1ZoqT5CyjI7h250Zm33zQhJh4WX15GJF78u1otbyVRbjdioHQAErGuBzvRWcHtQwqOWboUQ',
                'if-none-match': 'W/"111-eXvaprhKoSRT9E0NuMMHjuZOTUI"',
                'origin': 'https://www.moneycontrol.com',
                'priority': 'u=1, i',
                'referer': 'https://www.moneycontrol.com/',
                'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
            }
            yield scrapy.Request(
                url=f"https://api.moneycontrol.com/mcapi/v1/stock/estimates/consensus?scId={scId}&ex=N&deviceType=W",
                headers=headers, callback=self.parse_consensus,
                dont_filter=True,
                meta={"scId": scId, "stock_data": stock_data, 'forecast': forecast})
    def parse_consensus(self,response):
        stock_data = response.meta.get('stock_data')
        scId = response.meta.get('scId')
        forecast = response.meta.get('forecast')
        if response.status != 200:
            stock_data['forecast'] = forecast
            headers = {
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'en-US,en;q=0.9',
                'auth-token': 'xGQW9izz4G65y9e1ZoqT5CyjI7h250Zm33zQhJh4WX15GJF78u1otbyVRbjdioHQAErGuBzvRWcHtQwqOWboUQ',
                'if-none-match': 'W/"b6e-1YmJy2wW1XtJ2/KQbxUVKE77oj0"',
                'origin': 'https://www.moneycontrol.com',
                'priority': 'u=1, i',
                'referer': 'https://www.moneycontrol.com/',
                'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
            }
            yield scrapy.Request(
                url=f"https://api.moneycontrol.com/mcapi/technicals/v2/details?scId={scId}&dur=D&deviceType=W",
                callback=self.get_scId_details, headers=headers, meta={"scId": scId, "stock_data": stock_data})
        else:
            data = json.loads(response.text)
            result = []
            for i, month in enumerate(data['data']["categories"]):
                month_data = {entry["name"]: entry["data"][i] for entry in data['data']["graphData"]}
                result.append({month: month_data})
            forecast['Consensus Recommendations'] = result
            headers = {
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'en-US,en;q=0.9',
                'auth-token': 'xGQW9izz4G65y9e1ZoqT5CyjI7h250Zm33zQhJh4WX15GJF78u1otbyVRbjdioHQAErGuBzvRWcHtQwqOWboUQ',
                'if-none-match': 'W/"49e-yZss5ZpPT+fZYIeMX0/PR8hz0kk"',
                'origin': 'https://www.moneycontrol.com',
                'priority': 'u=1, i',
                'referer': 'https://www.moneycontrol.com/',
                'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
            }
            yield scrapy.Request(
                url=f"https://api.moneycontrol.com/mcapi/v1/stock/estimates/price-forecast?scId={scId}&ex=N&deviceType=W",
                headers=headers, callback=self.price_forecast,
                dont_filter=True,
                meta={"scId": scId, "stock_data": stock_data, 'forecast': forecast})

    def price_forecast(self, response):
        stock_data = response.meta.get('stock_data')
        scId = response.meta.get('scId')
        forecast = response.meta.get('forecast')
        if response.status != 200:
            stock_data['forecast'] = forecast
            headers = {
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'en-US,en;q=0.9',
                'auth-token': 'xGQW9izz4G65y9e1ZoqT5CyjI7h250Zm33zQhJh4WX15GJF78u1otbyVRbjdioHQAErGuBzvRWcHtQwqOWboUQ',
                'if-none-match': 'W/"b6e-1YmJy2wW1XtJ2/KQbxUVKE77oj0"',
                'origin': 'https://www.moneycontrol.com',
                'priority': 'u=1, i',
                'referer': 'https://www.moneycontrol.com/',
                'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
            }
            yield scrapy.Request(
                url=f"https://api.moneycontrol.com/mcapi/technicals/v2/details?scId={scId}&dur=D&deviceType=W",
                callback=self.get_scId_details, headers=headers, meta={"scId": scId, "stock_data": stock_data})
        else:
            data = json.loads(response.text)
            output = {
                "high": data["data"]["high"],
                "mean": data["data"]["mean"],
                "low": data["data"]["low"]
            }
            forecast['Share Price Forecast'] = output
            stock_data['forecast'] = forecast
            # yield data  # or process data as needed
            # After that Weill
            headers = {
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'en-US,en;q=0.9',
                'auth-token': 'xGQW9izz4G65y9e1ZoqT5CyjI7h250Zm33zQhJh4WX15GJF78u1otbyVRbjdioHQAErGuBzvRWcHtQwqOWboUQ',
                'if-none-match': 'W/"b6e-1YmJy2wW1XtJ2/KQbxUVKE77oj0"',
                'origin': 'https://www.moneycontrol.com',
                'priority': 'u=1, i',
                'referer': 'https://www.moneycontrol.com/',
                'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"macOS"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
            }
            yield scrapy.Request(
                url=f"https://api.moneycontrol.com/mcapi/technicals/v2/details?scId={scId}&dur=D&deviceType=W",
                callback=self.get_scId_details, headers=headers, meta={"scId": scId, "stock_data": stock_data})

    def get_scId_details(self,response):
        stock_data = response.meta.get('stock_data')
        scId = response.meta.get('scId')
        mc_technicals={}
        data = json.loads(response.text)  # Parse JSON
        # print(data['data']['summary'])
        filtered_data = {
            item["sentiments"]: item["indication"] for item in data['data']['summary'][:3]
        }
        filtered_data['technical_rating']=data['data']['overall']['indication']



        # daily_data=json.dumps(data, indent=4)['data']
        result = {item['key']: item['pivotLevel'] for item in data['data']['pivotLevels']}
        result['technical_rating']=filtered_data

        mc_technicals['Daily']=result
        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-US,en;q=0.9',
            'auth-token': 'xGQW9izz4G65y9e1ZoqT5CyjI7h250Zm33zQhJh4WX15GJF78u1otbyVRbjdioHQAErGuBzvRWcHtQwqOWboUQ',
            'if-none-match': 'W/"b6e-1YmJy2wW1XtJ2/KQbxUVKE77oj0"',
            'origin': 'https://www.moneycontrol.com',
            'priority': 'u=1, i',
            'referer': 'https://www.moneycontrol.com/',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
        }
        # yield stock_data
        yield scrapy.Request(
            url=f"https://api.moneycontrol.com/mcapi/technicals/v2/details?scId={scId}&dur=W&deviceType=W",
            callback=self.get_scId_details_by_weekly, headers=headers, meta={"scId": scId, "stock_data": stock_data,"mc_technicals":mc_technicals})

    def get_scId_details_by_weekly(self,response):
        stock_data = response.meta.get('stock_data')
        mc_technicals = response.meta.get('mc_technicals')
        scId = response.meta.get('scId')
        data = json.loads(response.text)  # Parse JSON
        # daily_data=json.dumps(data, indent=4)['data']
        filtered_data = {
            item["sentiments"]: item["indication"] for item in data['data']['summary'][:3]
        }
        filtered_data['technical_rating'] = data['data']['overall']['indication']

        result = {item['key']: item['pivotLevel'] for item in data['data']['pivotLevels']}
        result['technical_rating'] = filtered_data
        # mc_technicals.append({"daily_data":result})
        mc_technicals['Weekly']=result
        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-US,en;q=0.9',
            'auth-token': 'xGQW9izz4G65y9e1ZoqT5CyjI7h250Zm33zQhJh4WX15GJF78u1otbyVRbjdioHQAErGuBzvRWcHtQwqOWboUQ',
            'if-none-match': 'W/"b6e-1YmJy2wW1XtJ2/KQbxUVKE77oj0"',
            'origin': 'https://www.moneycontrol.com',
            'priority': 'u=1, i',
            'referer': 'https://www.moneycontrol.com/',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
        }
        # yield stock_data
        yield scrapy.Request(
            url=f"https://api.moneycontrol.com/mcapi/technicals/v2/details?scId={scId}&dur=M&deviceType=W",
            callback=self.get_scId_details_by_monthly, headers=headers, meta={"scId": scId, "stock_data": stock_data,"mc_technicals":mc_technicals})

    def get_scId_details_by_monthly(self,response):
        stock_data = response.meta.get('stock_data')
        mc_technicals = response.meta.get('mc_technicals')
        scId = response.meta.get('scId')
        data = json.loads(response.text)  # Parse JSON
        # daily_data=json.dumps(data, indent=4)['data']
        filtered_data = {
            item["sentiments"]: item["indication"] for item in data['data']['summary'][:3]
        }
        filtered_data['technical_rating'] = data['data']['overall']['indication']

        result = {item['key']: item['pivotLevel'] for item in data['data']['pivotLevels']}
        result['technical_rating'] = filtered_data
        # mc_technicals.append({"daily_data":result})
        mc_technicals['Monthly']=result
        stock_data['mc_technicals']=mc_technicals
        yield stock_data

