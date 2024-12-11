#!/usr/bin/env python3

import cgi
import os
import sys

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
if "file" not in form:
    print("<h1>Error: No file was uploaded</h1>")

file_item = form["file"]

if file_item.filename:
    upload_dir = "/var/www/html/uploaded_files"
    os.makedirs(upload_dir, exist_ok=True)

    file_path = os.path.join(upload_dir, os.path.basename(file_item.filename))

    with open(file_path, "wb") as output_file:
        output_file.write(file_item.file.read())

    print(f"<h1>File '{file_item.filename}' uploaded successfully!</h1>")
    print("<p><a href=\"/uploaded_files\">View the Uploaded Files</a></p>")

else:
    print("<h1>Error: File upload failed.</h1>")

