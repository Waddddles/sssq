import requests
import re
import csv
import time

def millisecond_to_time(millis):
    return time.strftime('%d日%H:%M',time.localtime(float(str(millis)[0:10])))

def cj_sww_sssq():
    url = "http://www.cjh.com.cn/sqindex.html"

    resp = requests.get(url)
    page_content = resp.text

    header = ["站名","水势","水位(m)","流量(m3/s)(入)","流量(m3/s)(出)","时间"]
    obj = re.compile(r".*?var sssq = (.+);.*?var sqHtml",re.S)
    obj2 = re.compile(r'"oq":"(?P<oq>.*?)".*?"q":"(?P<q>.*?)".*?"stnm":"(?P<stnm>.*?)","tm":(?P<tm>.*?),"wptn":"(?P<wptn>.*?)".*?"z":"(?P<z>.*?)"',re.S)
    sssq = obj.findall(page_content)[0]
    sssq2 = obj2.findall(sssq)

    f = open("长江水文网实时水情.csv",mode="w",encoding="utf-8-sig",newline="")
    writer = csv.writer(f)
    writer.writerow(header)

    for num in sssq2:
        wptn = int(num[4])
        if wptn == 4:
            wptn = "落"
        elif wptn == 5:
            wptn = "平"
        elif wptn == 6:
            wptn = "涨"
        tm = millisecond_to_time(num[3])
        data = [num[2],wptn,num[5],num[1],num[0],tm]
        writer.writerow(data)
    f.close()
    resp.close()