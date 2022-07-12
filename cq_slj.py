import requests
import csv

def cq_slj():
    url = "http://cqsw.slj.cq.gov.cn/hydrologyapi/stRiverR/dayWaterNotice"

    resp = requests.post(url)

    dic = resp.json()
    info = dic['data']

    f = open("重庆水利局.csv",mode="w",encoding="utf-8-sig",newline="")
    header = ["站名","河流","所在区县","水位(米)","水势"]
    writer = csv.writer(f)
    writer.writerow(header)

    for num in info:
        wptn = "0"
        potential = int(num['wptn'])
        if potential == 4:
            wptn = "落"
        elif potential == 5:
            wptn = "平"
        elif potential == 6:
            wptn = "涨"
        data = [str.strip(num['stnm']),str.strip(num['rVNM']),num['addvnm'],num['z'],wptn]
        writer.writerow(data)
        
    f.close()
    resp.close()
