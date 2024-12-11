#!/usr/bin/env python3

import cgi
import cgitb
import os

print("Content-Type: text/html")
print()

form = cgi.FieldStorage()
ip = form.getvalue("ip")

cmd = "ping -c 5 " + ip

result = ""

with os.popen(cmd) as output:
    result = output.read()

print("<pre>")
print(result)
print("</pre>")
