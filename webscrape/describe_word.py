from urllib import request
from urllib.request import Request, urlopen
import re
import json



BASE_URL = "https://describingwords.io/for/"
TARGET_TAG_REGEX='<script type="text\/json" id="preloadedDataEl">.*?</script>'
TARGET_TAG_STRING='<script type="text/json" id="preloadedDataEl">'

class DescribeWord():
    def __init__(self,word,number=10):
        self.word =word
        self.numberOfWords=number
        self.descriptions = []
        self.json_object = {}
        self.numberOfDescriptions = 10
        self.recordName = "{}.json".format(self.word)
        self.topTen = []


    def parse_page(self,html):
        pattern = TARGET_TAG_REGEX
        match_results = re.search(pattern, html, re.IGNORECASE)
        json_string = match_results.group()
        json_string = re.sub("<.*?>", "", json_string) # Remove HTML tags
        # print(json_string)
        # f = open("sky.json", "a")
        # f.write(json_string)
        # f.close()
        self.json_object = json.loads(json_string)
        self.json_object["terms"].sort(key=lambda x: x["score"],reverse = True)
        # print(self.json_object)
        for index, element in enumerate(self.json_object["terms"]):
            self.topTen.append(element["word"])
            if index == self.numberOfWords:
                break

        with open(self.recordName, 'w') as file:
            json.dump(self.json_object, file)
            
            
    def get_data(self):
        url = "{}{}".format(BASE_URL,self.word)
        request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        webpage = urlopen(request_site).read()
        # print(webpage[:500])
        html = webpage.decode("utf-8")
        target_string=TARGET_TAG_STRING
        for line in html.split('\n'):
            if target_string in line:
                # print("Identified:" +  line)
                self.parse_page(line)        