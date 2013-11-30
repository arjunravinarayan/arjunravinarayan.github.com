# -*- coding: latin-1 -*-

import xml.etree.ElementTree as ET

f = open("blogroll.md", "w")
str =  "---\n\
layout: post\n\
title: \"Blogroll\"\n\
category: blogroll\n\
tags: []\n\
---\n\
"
feedly = ET.parse('feedly.opml') # Change your filename here if you
                                 # aren't using feedly
root = feedly.getroot()
cats = root[1]

for cat in cats:
    str += "\n* " + cat.get("text")
    
    for feed in cat:
        str += "\n  * [" + feed.get("text") + "](" + feed.get("htmlUrl","") + ") [(RSS)](" + feed.get("xmlUrl") + ")"

print str.encode("utf8")
