import requests
import re
import csv

def sc_hdsq():
    url = "https://www.scsqzx.com/newApp/pub/scw/Query/GetHDriver.srdbselect"

    resp = requests.get(url)
    page_content = resp.text

    find_col_name = re.compile(r"<ColName>(.+)</ColName>",re.S)
    find_rows = re.compile(r"<Data>(.+)</Data>",re.S)

    col_name = find_col_name.findall(page_content)[0].split(",")
    rows = find_rows.findall(page_content)[0].split(",")

    f = open("四川河道水情表.csv",mode="w",encoding="utf-8-sig",newline="")
    writer = csv.writer(f)
    writer.writerow(col_name)
    for row in rows:
        single_row = row.split("|")
        writer.writerow(single_row)

    f.close()
    resp.close()