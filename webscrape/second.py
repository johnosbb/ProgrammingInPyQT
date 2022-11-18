
2
3
4
5
6
7
from urllib import request
from urllib.request import Request, urlopen
import re
import json


def parse_page(html):
    pattern = '<script type="text\/json" id="preloadedDataEl">.*?</script>'
    match_results = re.search(pattern, html, re.IGNORECASE)
    json_string = match_results.group()
    json_string = re.sub("<.*?>", "", json_string) # Remove HTML tags
    # print(json_string)
    f = open("sky.json", "a")
    f.write(json_string)
    f.close()
    json_obj = json.loads(json_string)
    json_obj["terms"].sort(key=lambda x: x["score"],reverse = True)
    print(json_obj)
    with open('sky_sorted.json', 'w') as f:
        json.dump(json_obj, f)

 
url = "https://describingwords.io/for/sky"
request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
webpage = urlopen(request_site).read()
# print(webpage[:500])
html = webpage.decode("utf-8")

target_string='<script type="text/json" id="preloadedDataEl">'
for line in html.split('\n'):
    if target_string in line:
        print("Identified:" +  line)
        parse_page(line)