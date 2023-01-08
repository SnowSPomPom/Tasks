import requests
from lxml import etree
url = "https://itawenya.cn"
resp = requests.get(url)
resp.encoding = 'UTF- 8'

et = etree.HTML(resp.text)

result0 = et.xpath("//ul[@id='top-nav']/li/a/text()")
result0 = ''.join(result0)
with open("snosp-geek-text.txt", "a", encoding='utf-8')as f:
    f.write('\n'+"part1"+'\n'+result0)

with open("snosp-geek-text.txt", "a", encoding='utf-8')as f:
    f.write('\n'+"part2")

result1 = et.xpath("//div[@class='modal-text']")
for item in result1:
    h1 = ''.join(item.xpath("./h1/text()")[0])
    h2 = ''.join(item.xpath("./h2/text()")[0])
    p = ''.join(item.xpath("./p/text()")[0])
    with open("snosp-geek-text.txt", "a", encoding='utf-8')as f:
        f.write('\n' + h1 + h2 + p)

result3 = et.xpath("//div[@class='slider']/ul/li/p/text()")
result3 = ''.join(result3)

result4 = et.xpath("//div[@id='contact-text']/p/text()")
result4 = ''.join(result4)

with open("snosp-geek-text.txt", "a", encoding='utf-8')as f:
    f.write('\n'+"part3"+'\n'+result3+'\n'+"part4"+'\n'+result4)

with open("snosp-geek-text.txt", "a", encoding='utf-8')as f:
    f.write('\n'+"part5")

result5 = et.xpath("//ul[@id='QA-ul']/li")
for item in result5:
    a = ''.join(item.xpath("./a/text()")[0])
    p = ''.join(item.xpath("./p/text()")[0])
    with open("snosp-geek-text.txt", "a", encoding='utf-8')as f:
        f.write('\n' + a + p)

print("over!")
