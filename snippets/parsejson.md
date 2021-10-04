---
title: parse json from url
tags: json,beginner
---

parse json from url

```py
import urllib.request
import json
url = link of the server 
#Taking response and request  from url

r = urllib.request.urlopen(url)
#reading and decoding the data
data = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))


for json_inner_array in data:
        for json_data in json_inner_array:
                    print("id: "+json_data["id"])


