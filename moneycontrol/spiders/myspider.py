import json
import time
from wsgiref import headers

import scrapy
from pip._internal.utils import urls


class MyspiderSpider(scrapy.Spider):
    name = "myspider"
    # allowed_domains = ["moneycontrol.com"]
    def start_requests(self):
        # url="https://www.moneycontrol.com/india/stockpricequote/A"

        cookies = {
            'A18ID': '1735825619250.264983',
            'MC_PPID_LOGIC': 'normaluser21193130293479932mcids',
            '__io_r': 'freelancer.com',
            '__io_first_source': 'freelancer.com',
            '__io': '672340ac8.2e690a47c_1735825621162',
            '__io_pr_utm_campaign': '%7B%22referrerHostname%22%3A%22www.freelancer.com%22%7D',
            '_cb': 'uEdv6_posICHZXJZ',
            'WZRK_G': 'b6165915d3ec415f91f896a307bcae61',
            '_cc_id': '68ba02dc438241c4aef7a25b279dc8cf',
            '_gcl_au': '1.1.1001301931.1735842582',
            '__utmz': '1.1737917515.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
            '_ga_HXEC5QES15': 'GS1.1.1737924438.5.0.1737924438.0.0.0',
            '_ga_8J9SC9WB3T': 'GS1.1.1737924403.5.1.1737924457.6.0.0',
            '__utma': '1.230106381.1735825620.1737921553.1738156826.3',
            '__gads': 'ID=875140f57be95c97:T=1735825634:RT=1738156829:S=ALNI_MZkP9ZL5-LQc1rKXKFNJaLJQwIKvw',
            '__gpi': 'UID=00000fc3f3247ce6:T=1735825634:RT=1738156829:S=ALNI_MY-2qPSsiJQArerekf4hLtPQNiUPQ',
            '__eoi': 'ID=9233f3eceb4d4cf0:T=1735825634:RT=1738156829:S=AA-AfjZ0mScKAKYyIrVLt0zXIKmf',
            '_is_in': '0',
            'verify': '1%24%24%23%23%24%241',
            'nnmc': 'DURGESH+Nemade',
            'UIDHASH': '74d2875064aeb528adcba5db48ca5e415f29765f538b2b8e324b39da8751877d',
            'token-normal': 'xGQW9izz4G65y9e1ZoqT5CyjI7h250Zm33zQhJh4WX15GJF78u1otbyVRbjdioHQAErGuBzvRWcHtQwqOWboUQ',
            'tvuid': 'Ym1WdFlXUmxaSFZ5WjJWemFBPT0%3D',
            '__token__': 'st=1738156933~exp=1738160533~acl=/*~data=__1__1766860199~hmac=3c374466cb84e5409a8f91acdea9b82feeb57a4b39fbce15a0f3dd169498170e',
            'mcpro': '1',
            '_abck': '5DFAB8E02FBA9E0A2A8C8E706F58E13F~0~YAAQEKInF+TeErCUAQAAPQM6sg2EW37o/FNHYFMDlS44SKaHmrESvfbciReVv0vzBf9V30/Z9/2JjML3doOPDSQoUtaIhv4vckSrlccbdEuXLvXXymVvlsyK3Za03TpU9xMAnv9+4t8DGvxKa+rA7ZFGa4d02Kjd8chKJOvqeewvmsRCsM6s90tC32XQeMIZgyqD2gBsc5Z5pHntwgsCGLHJpkVMyAwjry+LXFoR1PCw19P507VqmoEWIH2nzcyWfNqWpxJ1e4k+1fgcAKwOWnYyIwqQAxd9cGNAvmOEibcx8zuP3PgeV/fOrQipmK5jBUkN/GnaAKdFLd4qG9NWivb4Q2hnAdGg3g282kGjzt21gZi9qPaSlzODK9GKSS4Whrbu41MYudY9NZpoTn1KwOubZlCwF2bRMtMrysB6XkavwWxF9ea1DYE9rXBu9qkzNv5SP+FDILE9xEDPvlFRFhwFxSneK+DWQxVzwGKw6mrZbQASZ93n+YVpoj6s1ipHc+WWDSlVURY2tDzvyE8u7b2AphfQeEWkxAo8cIYw9MYuZ3BjjVEieW3GlDyk9KY6BsfDc7y2YXrVr5+jp5eIiLhvEjMI3WVTJxduerJ7Naq2f5GashIvNIXxQg7kZJX7O7JCi8gFXiNzMkGw/qyDY2XkxPVMQOE5+YtJw+eyZdHjolLh7BvD1fChAOuZDt6IkgfNfXs6n8VP1hV4fklZifI=~-1~-1~-1',
            '_ga_4S48PBY299': 'deleted',
            'nousersess': '81b9lm01yvbb0fjq',
            'stocks': '|Cyient.DLM_CD06~24%7CJ.G.Chemicals_CL10%7E6%7CABB.India_ABB%7E29%7CA.K.Spintex_AKS01%7E1%7CA.K.Capital.Ser_AKC01%7E2%7CUflex_FI08%7E1%7CA.G.Universal_U01%7E5%7CN_JB02%7E8%7C_F04%7E18%7C_U01%7E6',
            'dtCookie': 'v_4_srv_3_sn_01E29794A8D36D94350FDA86DA52B61E_perc_100000_ol_0_mul_1_app-3A15ca68b27f59163f_1',
            '_gid': 'GA1.2.1444747103.1738914975',
            'PHPSESSID': 'mug5cci05ou0c2iktq1t08o4m0',
            'cto_bundle': 'toqJ0V8xZjJFQ3pXQXJoNUlUY3JDcVNpeThZJTJGRXVQRTZKZDF5OTUlMkZjMVJVeWJpQSUyRmJjYTBpWiUyRnJyQWdpeWZJJTJGNm9OU2xDNDNONkVZOVlCeWtYWlpvQkd0S3RwZW84ZUV1ZUNmR0JrWXdjTmpsMlVBUllGbzJ5SDR4amxQN05qalExUjlBUlZ0TXd6cXVQRENKalIycklGUEdRSUFYYmhIdCUyQlF0eFh6JTJGa21oUFR2VlVzdXRiYU5rRUpyQVlaaTZHRUw4RzQyck0lMkJJd24lMkJLNTN5bXlzaGxGWlltaEo5NUElMkJoQ1R0UklnJTJGR3loVTZ6ZURrOXg2NGdhY29ibFVTMWxwVWtVYnpFTXhsYTJSSHJMRFdtekxMSUhEWUElM0QlM0Q',
            'FCNEC': '%5B%5B%22AKsRol-1auT8_Xkxjk_mMZZZBU3lwkouNi6_Cdx9V3igeq6fKYiX8-R6jPijbvGRshkqNhxTqfUZKp6eq5KjDwKaOx0VMfiQp02Jm-HEJCkt-kpGaiPQIuzPoOn8RrpynESeawyxCY1Kw0OMTNn79bwOhqQDJZceow%3D%3D%22%5D%5D',
            '_ga_4S48PBY299': 'GS1.1.1738914975.22.1.1738915022.13.0.0',
            '_ga': 'GA1.2.230106381.1735825620',
            '_io_ht_r': '1',
            '__io_session_id': '3f8a3ea39.2c2d248fc_1738915027054',
            '__io_unique_43938': '7',
            '__io_visit_43938': '1',
            '_gat': '1',
            '__io_d': '3_3330783724',
            '__io_nav_state43938': '%7B%22current%22%3A%22%2Findia%2Fstockpricequote%2F%22%2C%22currentDomain%22%3A%22www.moneycontrol.com%22%2C%22previous%22%3A%22%2Findia%2Fstockpricequote%2FA%22%2C%22previousDomain%22%3A%22www.moneycontrol.com%22%7D',
            '_chartbeat2': '.1735825621352.1738915052413.1001101110000111.CE0MfmBHX9KNDXWTW7B99WB0mxjNy.1',
            '_cb_svref': 'external',
            'WZRK_S_86Z-5ZR-RK6Z': '%7B%22p%22%3A4%2C%22s%22%3A1738914981%2C%22t%22%3A1738915054%7D',
            '_chartbeat5': '99|1015|%2Findia%2Fstockpricequote%2F|https%3A%2F%2Fwww.moneycontrol.com%2Findia%2Fstockpricequote%2FA|8Jn12DiZR08Dnl9DlCfqK7XeP0qT||c|CEF6fcC0282YCVndmFDDkQYzxqdUn|moneycontrol.com|',
            '__io_lv': '1738915068104',
        }

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            # 'cookie': 'A18ID=1735825619250.264983; MC_PPID_LOGIC=normaluser21193130293479932mcids; __io_r=freelancer.com; __io_first_source=freelancer.com; __io=672340ac8.2e690a47c_1735825621162; __io_pr_utm_campaign=%7B%22referrerHostname%22%3A%22www.freelancer.com%22%7D; _cb=uEdv6_posICHZXJZ; WZRK_G=b6165915d3ec415f91f896a307bcae61; _cc_id=68ba02dc438241c4aef7a25b279dc8cf; _gcl_au=1.1.1001301931.1735842582; __utmz=1.1737917515.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga_HXEC5QES15=GS1.1.1737924438.5.0.1737924438.0.0.0; _ga_8J9SC9WB3T=GS1.1.1737924403.5.1.1737924457.6.0.0; __utma=1.230106381.1735825620.1737921553.1738156826.3; __gads=ID=875140f57be95c97:T=1735825634:RT=1738156829:S=ALNI_MZkP9ZL5-LQc1rKXKFNJaLJQwIKvw; __gpi=UID=00000fc3f3247ce6:T=1735825634:RT=1738156829:S=ALNI_MY-2qPSsiJQArerekf4hLtPQNiUPQ; __eoi=ID=9233f3eceb4d4cf0:T=1735825634:RT=1738156829:S=AA-AfjZ0mScKAKYyIrVLt0zXIKmf; _is_in=0; verify=1%24%24%23%23%24%241; nnmc=DURGESH+Nemade; UIDHASH=74d2875064aeb528adcba5db48ca5e415f29765f538b2b8e324b39da8751877d; token-normal=xGQW9izz4G65y9e1ZoqT5CyjI7h250Zm33zQhJh4WX15GJF78u1otbyVRbjdioHQAErGuBzvRWcHtQwqOWboUQ; tvuid=Ym1WdFlXUmxaSFZ5WjJWemFBPT0%3D; __token__=st=1738156933~exp=1738160533~acl=/*~data=__1__1766860199~hmac=3c374466cb84e5409a8f91acdea9b82feeb57a4b39fbce15a0f3dd169498170e; mcpro=1; _abck=5DFAB8E02FBA9E0A2A8C8E706F58E13F~0~YAAQEKInF+TeErCUAQAAPQM6sg2EW37o/FNHYFMDlS44SKaHmrESvfbciReVv0vzBf9V30/Z9/2JjML3doOPDSQoUtaIhv4vckSrlccbdEuXLvXXymVvlsyK3Za03TpU9xMAnv9+4t8DGvxKa+rA7ZFGa4d02Kjd8chKJOvqeewvmsRCsM6s90tC32XQeMIZgyqD2gBsc5Z5pHntwgsCGLHJpkVMyAwjry+LXFoR1PCw19P507VqmoEWIH2nzcyWfNqWpxJ1e4k+1fgcAKwOWnYyIwqQAxd9cGNAvmOEibcx8zuP3PgeV/fOrQipmK5jBUkN/GnaAKdFLd4qG9NWivb4Q2hnAdGg3g282kGjzt21gZi9qPaSlzODK9GKSS4Whrbu41MYudY9NZpoTn1KwOubZlCwF2bRMtMrysB6XkavwWxF9ea1DYE9rXBu9qkzNv5SP+FDILE9xEDPvlFRFhwFxSneK+DWQxVzwGKw6mrZbQASZ93n+YVpoj6s1ipHc+WWDSlVURY2tDzvyE8u7b2AphfQeEWkxAo8cIYw9MYuZ3BjjVEieW3GlDyk9KY6BsfDc7y2YXrVr5+jp5eIiLhvEjMI3WVTJxduerJ7Naq2f5GashIvNIXxQg7kZJX7O7JCi8gFXiNzMkGw/qyDY2XkxPVMQOE5+YtJw+eyZdHjolLh7BvD1fChAOuZDt6IkgfNfXs6n8VP1hV4fklZifI=~-1~-1~-1; _ga_4S48PBY299=deleted; nousersess=81b9lm01yvbb0fjq; stocks=|Cyient.DLM_CD06~24%7CJ.G.Chemicals_CL10%7E6%7CABB.India_ABB%7E29%7CA.K.Spintex_AKS01%7E1%7CA.K.Capital.Ser_AKC01%7E2%7CUflex_FI08%7E1%7CA.G.Universal_U01%7E5%7CN_JB02%7E8%7C_F04%7E18%7C_U01%7E6; dtCookie=v_4_srv_3_sn_01E29794A8D36D94350FDA86DA52B61E_perc_100000_ol_0_mul_1_app-3A15ca68b27f59163f_1; _gid=GA1.2.1444747103.1738914975; PHPSESSID=mug5cci05ou0c2iktq1t08o4m0; cto_bundle=toqJ0V8xZjJFQ3pXQXJoNUlUY3JDcVNpeThZJTJGRXVQRTZKZDF5OTUlMkZjMVJVeWJpQSUyRmJjYTBpWiUyRnJyQWdpeWZJJTJGNm9OU2xDNDNONkVZOVlCeWtYWlpvQkd0S3RwZW84ZUV1ZUNmR0JrWXdjTmpsMlVBUllGbzJ5SDR4amxQN05qalExUjlBUlZ0TXd6cXVQRENKalIycklGUEdRSUFYYmhIdCUyQlF0eFh6JTJGa21oUFR2VlVzdXRiYU5rRUpyQVlaaTZHRUw4RzQyck0lMkJJd24lMkJLNTN5bXlzaGxGWlltaEo5NUElMkJoQ1R0UklnJTJGR3loVTZ6ZURrOXg2NGdhY29ibFVTMWxwVWtVYnpFTXhsYTJSSHJMRFdtekxMSUhEWUElM0QlM0Q; FCNEC=%5B%5B%22AKsRol-1auT8_Xkxjk_mMZZZBU3lwkouNi6_Cdx9V3igeq6fKYiX8-R6jPijbvGRshkqNhxTqfUZKp6eq5KjDwKaOx0VMfiQp02Jm-HEJCkt-kpGaiPQIuzPoOn8RrpynESeawyxCY1Kw0OMTNn79bwOhqQDJZceow%3D%3D%22%5D%5D; _ga_4S48PBY299=GS1.1.1738914975.22.1.1738915022.13.0.0; _ga=GA1.2.230106381.1735825620; _io_ht_r=1; __io_session_id=3f8a3ea39.2c2d248fc_1738915027054; __io_unique_43938=7; __io_visit_43938=1; _gat=1; __io_d=3_3330783724; __io_nav_state43938=%7B%22current%22%3A%22%2Findia%2Fstockpricequote%2F%22%2C%22currentDomain%22%3A%22www.moneycontrol.com%22%2C%22previous%22%3A%22%2Findia%2Fstockpricequote%2FA%22%2C%22previousDomain%22%3A%22www.moneycontrol.com%22%7D; _chartbeat2=.1735825621352.1738915052413.1001101110000111.CE0MfmBHX9KNDXWTW7B99WB0mxjNy.1; _cb_svref=external; WZRK_S_86Z-5ZR-RK6Z=%7B%22p%22%3A4%2C%22s%22%3A1738914981%2C%22t%22%3A1738915054%7D; _chartbeat5=99|1015|%2Findia%2Fstockpricequote%2F|https%3A%2F%2Fwww.moneycontrol.com%2Findia%2Fstockpricequote%2FA|8Jn12DiZR08Dnl9DlCfqK7XeP0qT||c|CEF6fcC0282YCVndmFDDkQYzxqdUn|moneycontrol.com|; __io_lv=1738915068104',
            'priority': 'u=0, i',
            'referer': 'https://www.moneycontrol.com/india/stockpricequote/',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
        }
        # for char in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        #      'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
            # print(chr(char))
        yield scrapy.Request(url=f"https://www.moneycontrol.com/india/stockpricequote/A", headers=headers, cookies=cookies, callback=self.parse ,)


    def parse(self, response):
        links = response.xpath('//a[@class="bl_12"]/@href').getall()



        cookies = {
            'A18ID': '1735825619250.264983',
            'MC_PPID_LOGIC': 'normaluser21193130293479932mcids',
            '__io_r': 'freelancer.com',
            '__io_first_source': 'freelancer.com',
            '__io': '672340ac8.2e690a47c_1735825621162',
            '__io_pr_utm_campaign': '%7B%22referrerHostname%22%3A%22www.freelancer.com%22%7D',
            '_cb': 'uEdv6_posICHZXJZ',
            'WZRK_G': 'b6165915d3ec415f91f896a307bcae61',
            '_cc_id': '68ba02dc438241c4aef7a25b279dc8cf',
            '_gcl_au': '1.1.1001301931.1735842582',
            '__utmz': '1.1737917515.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
            '_ga_HXEC5QES15': 'GS1.1.1737924438.5.0.1737924438.0.0.0',
            '_ga_8J9SC9WB3T': 'GS1.1.1737924403.5.1.1737924457.6.0.0',
            '__utma': '1.230106381.1735825620.1737921553.1738156826.3',
            '__gads': 'ID=875140f57be95c97:T=1735825634:RT=1738156829:S=ALNI_MZkP9ZL5-LQc1rKXKFNJaLJQwIKvw',
            '__gpi': 'UID=00000fc3f3247ce6:T=1735825634:RT=1738156829:S=ALNI_MY-2qPSsiJQArerekf4hLtPQNiUPQ',
            '__eoi': 'ID=9233f3eceb4d4cf0:T=1735825634:RT=1738156829:S=AA-AfjZ0mScKAKYyIrVLt0zXIKmf',
            '_is_in': '0',
            'verify': '1%24%24%23%23%24%241',
            'nnmc': 'DURGESH+Nemade',
            'UIDHASH': '74d2875064aeb528adcba5db48ca5e415f29765f538b2b8e324b39da8751877d',
            'token-normal': 'xGQW9izz4G65y9e1ZoqT5CyjI7h250Zm33zQhJh4WX15GJF78u1otbyVRbjdioHQAErGuBzvRWcHtQwqOWboUQ',
            'tvuid': 'Ym1WdFlXUmxaSFZ5WjJWemFBPT0%3D',
            '__token__': 'st=1738156933~exp=1738160533~acl=/*~data=__1__1766860199~hmac=3c374466cb84e5409a8f91acdea9b82feeb57a4b39fbce15a0f3dd169498170e',
            'mcpro': '1',
            '_abck': '5DFAB8E02FBA9E0A2A8C8E706F58E13F~0~YAAQEKInF+TeErCUAQAAPQM6sg2EW37o/FNHYFMDlS44SKaHmrESvfbciReVv0vzBf9V30/Z9/2JjML3doOPDSQoUtaIhv4vckSrlccbdEuXLvXXymVvlsyK3Za03TpU9xMAnv9+4t8DGvxKa+rA7ZFGa4d02Kjd8chKJOvqeewvmsRCsM6s90tC32XQeMIZgyqD2gBsc5Z5pHntwgsCGLHJpkVMyAwjry+LXFoR1PCw19P507VqmoEWIH2nzcyWfNqWpxJ1e4k+1fgcAKwOWnYyIwqQAxd9cGNAvmOEibcx8zuP3PgeV/fOrQipmK5jBUkN/GnaAKdFLd4qG9NWivb4Q2hnAdGg3g282kGjzt21gZi9qPaSlzODK9GKSS4Whrbu41MYudY9NZpoTn1KwOubZlCwF2bRMtMrysB6XkavwWxF9ea1DYE9rXBu9qkzNv5SP+FDILE9xEDPvlFRFhwFxSneK+DWQxVzwGKw6mrZbQASZ93n+YVpoj6s1ipHc+WWDSlVURY2tDzvyE8u7b2AphfQeEWkxAo8cIYw9MYuZ3BjjVEieW3GlDyk9KY6BsfDc7y2YXrVr5+jp5eIiLhvEjMI3WVTJxduerJ7Naq2f5GashIvNIXxQg7kZJX7O7JCi8gFXiNzMkGw/qyDY2XkxPVMQOE5+YtJw+eyZdHjolLh7BvD1fChAOuZDt6IkgfNfXs6n8VP1hV4fklZifI=~-1~-1~-1',
            '_ga_4S48PBY299': 'deleted',
            'nousersess': '81b9lm01yvbb0fjq',
            'stocks': '|Cyient.DLM_CD06~24%7CJ.G.Chemicals_CL10%7E6%7CABB.India_ABB%7E29%7CA.K.Spintex_AKS01%7E1%7CA.K.Capital.Ser_AKC01%7E2%7CUflex_FI08%7E1%7CA.G.Universal_U01%7E5%7CN_JB02%7E8%7C_F04%7E18%7C_U01%7E6',
            'dtCookie': 'v_4_srv_3_sn_01E29794A8D36D94350FDA86DA52B61E_perc_100000_ol_0_mul_1_app-3A15ca68b27f59163f_1',
            '_gid': 'GA1.2.1444747103.1738914975',
            'PHPSESSID': 'mug5cci05ou0c2iktq1t08o4m0',
            'cto_bundle': 'toqJ0V8xZjJFQ3pXQXJoNUlUY3JDcVNpeThZJTJGRXVQRTZKZDF5OTUlMkZjMVJVeWJpQSUyRmJjYTBpWiUyRnJyQWdpeWZJJTJGNm9OU2xDNDNONkVZOVlCeWtYWlpvQkd0S3RwZW84ZUV1ZUNmR0JrWXdjTmpsMlVBUllGbzJ5SDR4amxQN05qalExUjlBUlZ0TXd6cXVQRENKalIycklGUEdRSUFYYmhIdCUyQlF0eFh6JTJGa21oUFR2VlVzdXRiYU5rRUpyQVlaaTZHRUw4RzQyck0lMkJJd24lMkJLNTN5bXlzaGxGWlltaEo5NUElMkJoQ1R0UklnJTJGR3loVTZ6ZURrOXg2NGdhY29ibFVTMWxwVWtVYnpFTXhsYTJSSHJMRFdtekxMSUhEWUElM0QlM0Q',
            'FCNEC': '%5B%5B%22AKsRol-1auT8_Xkxjk_mMZZZBU3lwkouNi6_Cdx9V3igeq6fKYiX8-R6jPijbvGRshkqNhxTqfUZKp6eq5KjDwKaOx0VMfiQp02Jm-HEJCkt-kpGaiPQIuzPoOn8RrpynESeawyxCY1Kw0OMTNn79bwOhqQDJZceow%3D%3D%22%5D%5D',
            '_ga_4S48PBY299': 'GS1.1.1738914975.22.1.1738915022.13.0.0',
            '_ga': 'GA1.2.230106381.1735825620',
            '_io_ht_r': '1',
            '__io_session_id': '3f8a3ea39.2c2d248fc_1738915027054',
            '__io_unique_43938': '7',
            '__io_visit_43938': '1',
            '_cb_svref': 'external',
            '__io_d': '4_883510103',
            '__io_nav_state43938': '%7B%22current%22%3A%22%2Findia%2Fstockpricequote%2FA%22%2C%22currentDomain%22%3A%22www.moneycontrol.com%22%2C%22previous%22%3A%22%2Findia%2Fstockpricequote%2F%22%2C%22previousDomain%22%3A%22www.moneycontrol.com%22%7D',
            '_chartbeat2': '.1735825621352.1738915071941.1001101110000111.CE0MfmBHX9KNDXWTW7B99WB0mxjNy.2',
            'WZRK_S_86Z-5ZR-RK6Z': '%7B%22p%22%3A5%2C%22s%22%3A1738914981%2C%22t%22%3A1738915075%7D',
            # '_chartbeat5': '22|1214|%2Findia%2Fstockpricequote%2FA|https%3A%2F%2Fwww.moneycontrol.com%2Findia%2Fstockpricequote%2Fmiscellaneous%2Famfebcon%2FF03|CYP2rIBFnap3DbLv09oMJwRC-rIQE||c|D7JToOCy8BoKD-Hd7iDTT3qmCqcr0I|moneycontrol.com|',
            '__io_lv': '1738915335769',
        }

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            # 'cookie': 'A18ID=1735825619250.264983; MC_PPID_LOGIC=normaluser21193130293479932mcids; __io_r=freelancer.com; __io_first_source=freelancer.com; __io=672340ac8.2e690a47c_1735825621162; __io_pr_utm_campaign=%7B%22referrerHostname%22%3A%22www.freelancer.com%22%7D; _cb=uEdv6_posICHZXJZ; WZRK_G=b6165915d3ec415f91f896a307bcae61; _cc_id=68ba02dc438241c4aef7a25b279dc8cf; _gcl_au=1.1.1001301931.1735842582; __utmz=1.1737917515.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga_HXEC5QES15=GS1.1.1737924438.5.0.1737924438.0.0.0; _ga_8J9SC9WB3T=GS1.1.1737924403.5.1.1737924457.6.0.0; __utma=1.230106381.1735825620.1737921553.1738156826.3; __gads=ID=875140f57be95c97:T=1735825634:RT=1738156829:S=ALNI_MZkP9ZL5-LQc1rKXKFNJaLJQwIKvw; __gpi=UID=00000fc3f3247ce6:T=1735825634:RT=1738156829:S=ALNI_MY-2qPSsiJQArerekf4hLtPQNiUPQ; __eoi=ID=9233f3eceb4d4cf0:T=1735825634:RT=1738156829:S=AA-AfjZ0mScKAKYyIrVLt0zXIKmf; _is_in=0; verify=1%24%24%23%23%24%241; nnmc=DURGESH+Nemade; UIDHASH=74d2875064aeb528adcba5db48ca5e415f29765f538b2b8e324b39da8751877d; token-normal=xGQW9izz4G65y9e1ZoqT5CyjI7h250Zm33zQhJh4WX15GJF78u1otbyVRbjdioHQAErGuBzvRWcHtQwqOWboUQ; tvuid=Ym1WdFlXUmxaSFZ5WjJWemFBPT0%3D; __token__=st=1738156933~exp=1738160533~acl=/*~data=__1__1766860199~hmac=3c374466cb84e5409a8f91acdea9b82feeb57a4b39fbce15a0f3dd169498170e; mcpro=1; _abck=5DFAB8E02FBA9E0A2A8C8E706F58E13F~0~YAAQEKInF+TeErCUAQAAPQM6sg2EW37o/FNHYFMDlS44SKaHmrESvfbciReVv0vzBf9V30/Z9/2JjML3doOPDSQoUtaIhv4vckSrlccbdEuXLvXXymVvlsyK3Za03TpU9xMAnv9+4t8DGvxKa+rA7ZFGa4d02Kjd8chKJOvqeewvmsRCsM6s90tC32XQeMIZgyqD2gBsc5Z5pHntwgsCGLHJpkVMyAwjry+LXFoR1PCw19P507VqmoEWIH2nzcyWfNqWpxJ1e4k+1fgcAKwOWnYyIwqQAxd9cGNAvmOEibcx8zuP3PgeV/fOrQipmK5jBUkN/GnaAKdFLd4qG9NWivb4Q2hnAdGg3g282kGjzt21gZi9qPaSlzODK9GKSS4Whrbu41MYudY9NZpoTn1KwOubZlCwF2bRMtMrysB6XkavwWxF9ea1DYE9rXBu9qkzNv5SP+FDILE9xEDPvlFRFhwFxSneK+DWQxVzwGKw6mrZbQASZ93n+YVpoj6s1ipHc+WWDSlVURY2tDzvyE8u7b2AphfQeEWkxAo8cIYw9MYuZ3BjjVEieW3GlDyk9KY6BsfDc7y2YXrVr5+jp5eIiLhvEjMI3WVTJxduerJ7Naq2f5GashIvNIXxQg7kZJX7O7JCi8gFXiNzMkGw/qyDY2XkxPVMQOE5+YtJw+eyZdHjolLh7BvD1fChAOuZDt6IkgfNfXs6n8VP1hV4fklZifI=~-1~-1~-1; _ga_4S48PBY299=deleted; nousersess=81b9lm01yvbb0fjq; stocks=|Cyient.DLM_CD06~24%7CJ.G.Chemicals_CL10%7E6%7CABB.India_ABB%7E29%7CA.K.Spintex_AKS01%7E1%7CA.K.Capital.Ser_AKC01%7E2%7CUflex_FI08%7E1%7CA.G.Universal_U01%7E5%7CN_JB02%7E8%7C_F04%7E18%7C_U01%7E6; dtCookie=v_4_srv_3_sn_01E29794A8D36D94350FDA86DA52B61E_perc_100000_ol_0_mul_1_app-3A15ca68b27f59163f_1; _gid=GA1.2.1444747103.1738914975; PHPSESSID=mug5cci05ou0c2iktq1t08o4m0; cto_bundle=toqJ0V8xZjJFQ3pXQXJoNUlUY3JDcVNpeThZJTJGRXVQRTZKZDF5OTUlMkZjMVJVeWJpQSUyRmJjYTBpWiUyRnJyQWdpeWZJJTJGNm9OU2xDNDNONkVZOVlCeWtYWlpvQkd0S3RwZW84ZUV1ZUNmR0JrWXdjTmpsMlVBUllGbzJ5SDR4amxQN05qalExUjlBUlZ0TXd6cXVQRENKalIycklGUEdRSUFYYmhIdCUyQlF0eFh6JTJGa21oUFR2VlVzdXRiYU5rRUpyQVlaaTZHRUw4RzQyck0lMkJJd24lMkJLNTN5bXlzaGxGWlltaEo5NUElMkJoQ1R0UklnJTJGR3loVTZ6ZURrOXg2NGdhY29ibFVTMWxwVWtVYnpFTXhsYTJSSHJMRFdtekxMSUhEWUElM0QlM0Q; FCNEC=%5B%5B%22AKsRol-1auT8_Xkxjk_mMZZZBU3lwkouNi6_Cdx9V3igeq6fKYiX8-R6jPijbvGRshkqNhxTqfUZKp6eq5KjDwKaOx0VMfiQp02Jm-HEJCkt-kpGaiPQIuzPoOn8RrpynESeawyxCY1Kw0OMTNn79bwOhqQDJZceow%3D%3D%22%5D%5D; _ga_4S48PBY299=GS1.1.1738914975.22.1.1738915022.13.0.0; _ga=GA1.2.230106381.1735825620; _io_ht_r=1; __io_session_id=3f8a3ea39.2c2d248fc_1738915027054; __io_unique_43938=7; __io_visit_43938=1; _cb_svref=external; __io_d=4_883510103; __io_nav_state43938=%7B%22current%22%3A%22%2Findia%2Fstockpricequote%2FA%22%2C%22currentDomain%22%3A%22www.moneycontrol.com%22%2C%22previous%22%3A%22%2Findia%2Fstockpricequote%2F%22%2C%22previousDomain%22%3A%22www.moneycontrol.com%22%7D; _chartbeat2=.1735825621352.1738915071941.1001101110000111.CE0MfmBHX9KNDXWTW7B99WB0mxjNy.2; WZRK_S_86Z-5ZR-RK6Z=%7B%22p%22%3A5%2C%22s%22%3A1738914981%2C%22t%22%3A1738915075%7D; _chartbeat5=22|1214|%2Findia%2Fstockpricequote%2FA|https%3A%2F%2Fwww.moneycontrol.com%2Findia%2Fstockpricequote%2Fmiscellaneous%2Famfebcon%2FF03|CYP2rIBFnap3DbLv09oMJwRC-rIQE||c|D7JToOCy8BoKD-Hd7iDTT3qmCqcr0I|moneycontrol.com|; __io_lv=1738915335769',
            'priority': 'u=0, i',
            'referer': 'https://www.moneycontrol.com/india/stockpricequote/A',
            'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
        }
        print(len(links))
        for url in links:
            if url:
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

