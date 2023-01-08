import requests
from lxml import etree
import urllib3
urllib3.disable_warnings()
url = "https://itawenya.cn"
resp = requests.get(url)
resp.encoding = 'UTF- 8'

domain = "https://itawenya.cn"
et = etree.HTML(resp.text)
img = et.xpath("//img/@src")
for item in img:
    url = domain+item
    name = url.split("/")[-1]
    print(name+url)
    resp_img = requests.get(url, verify=False)
    with open(f"image2/{name}", mode="wb") as f:
        f.write(resp_img.content)
