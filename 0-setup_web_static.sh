#!/usr/bin/env bash
#Setup web server for web static deployment

sudo apt-get update
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "<h1>Fucking Mirey 👽<h1/>" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
old_string="server_name _;"
new_string="server_name _;#\\nlocation /hbnb_static {\\n\\t\\talias /data/web_static/current/;\\n\\t\\tautoindex off;\\n\\t}"
sudo sed -i "s|$old_string|$new_string|" /etc/nginx/sites-available/default
sudo ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
sudo service nginx restart
