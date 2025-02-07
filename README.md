# vpwa
Vulnerably Python Web Apps to practice simple exploits.
## Install the latest Ubuntu Server LTS
Install Ubuntu Server as a Virtual Machine or on bare metal.  You can download [Ubuntu Server here](https://ubuntu.com/download/server).
## Set Up the Web Server
These are the commands to set up a web server on Ubuntu Server to serve web apps written in Python.
1. `sudo apt update`
2. `sudo apt upgrade`
3. `sudo apt install apache2 -y`
4. `sudo systemctl status apache2`
5. `sudo a2enmod cgi`
6. `sudo systemctl restart apache2`
7. `sudo apt install python3 -y`
8. `python3 --version`
9. `sudo systemctl restart apache2`
## Upload the Web Application Files
1. Upload the python files in the "python" folder of this repository in the following directory: `/usr/lib/cgi-bin`
2. Upload the HTML files in the "html" folder of this repository in the following directory: `/var/www/html`
3. Make the directory to store files uploaded by the python web app: `mkdir /var/www/html/uploaded_files`
4. Have the Apache2 user own the "uploaded_files" directory so that it can write to it: `chown www-data:www-data /var/www/html/uploaded_files`
## Access the Web Files with a Web Browser
Go to: `http://<web server ip or hostname>/index.html`
