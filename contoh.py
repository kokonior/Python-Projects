#!/usr/bin/env python
# encoding: utf-8

import lxml.etree
import lxml.html
import requests

xml_sample = """<?xml version="1.0" encoding="UTF-8"?>
<foo:Results xmlns:foo="http://www.foo.com" xmlns="http://www.bah.com">
<foo:Recordset setCount="2">
<foo:Record setEntry="0">
<foo:Title>First title</foo:Title>
</foo:Record>
<foo:Record setEntry="1">
<foo:Title>Second title</foo:Title>
</foo:Record>
<Record setEntry="2">
<Title>Third title</Title>
</Record>
<Record setEntry="3">
<Title>Fourth title</Title>
</Record>
</foo:Recordset>
</foo:Results>
""".encode("utf-8")

def main():
    print("Demonstrating xpath on HTML")
    print("===========================")

    r = requests.get("http://www.ianhopkinson.org.uk")
    root = lxml.html.fromstring(r.content)
    title = root.xpath('/html/body/div/div/div[2]/h1') 
    print("My blog title is: '{}'".format(title[0].text.strip()))

    title = root.xpath('//div[2]/h1') 
    print("We can use the // shortcut to get the same thing more easily: '{}'".format(title[0].text_content().strip()))

    ids = root.xpath('//li/@id')
    print("We can get the id attributes of all the <li> elements. There are {} of them, the first one is {}".format(len(ids), ids[0]))

    tagcloud = root.xpath('//*[@class="tagcloud"]') 
    print("We can get the parent element of the tagcloud using an attribute selector: {}".format(tagcloud))

    title = root.xpath("//h1[contains(., 'SomeBeans')]")
    print("Another way to get the title is to select by element text content: '{}'".format(title[0].text.strip()))

    subtitle = root.xpath('//h1[contains(@class,"header_title")]/../h2')
    print("We can use the .. operator is select the subtitle: '{}'".format(subtitle[0].text.strip()))

    subtitle = root.xpath('//h1[contains(@class,"header_title")]/following-sibling::h2')
    print("Or we can use following-sibling to same effect: '{}'".format(subtitle[0].text.strip()))     

    print("\nDemonstrating xpath on XML")
    print("============================")

    print("Processing XML is pretty similar except for namespaces")

    namespace = "http://www.foo.com"
    namespace_c = "{" + namespace + "}"
    NSMAP = {"foo": namespace}
    root = lxml.etree.fromstring(xml_sample)

    record_count = root.xpath('//@setCount')[0]

    print("Attributes are easy, this is the @setCount: {}".format(record_count))

    print("These are the elements defined by the XML string at the top of this program:")

    for i, element in enumerate(root.getiterator()):
        print(element.tag)

    print("We can select elements by defining a namespace in our queries")
    records = root.xpath('//foo:Title', namespaces = {"foo": "http://www.foo.com"})

    for record in records:
        print(record.text)

    print("Without defining the default namespace, we get nothing")
    records = root.xpath('//Title')    
    for record in records:
        print(record.text)

    print("With the default namespace, we get something")
    records = root.xpath('//bah:Title', namespaces = {"bah": "http://www.bah.com"})    
    for record in records:
        print("Element name: {}, element text '{}'".format(record.tag, record.text))

if __name__ == "__main__":
    main()