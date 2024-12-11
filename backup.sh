#/usr/bin/sh
echo "Backing up the python files..."
cp /usr/lib/cgi-bin/* python
echo "done."
echo "Backing up the HTML file..."
cp /var/www/html/* html
echo "done."
