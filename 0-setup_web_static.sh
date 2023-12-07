#!/usr/bin/env bash
#sets up your web servers for the deployment of web_static

STATIC="server_name _;\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n}"
MATCH="server_name _;"

sudo apt -y update
sudo apt -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

sudo echo "<html>
  	<head>
    	</head>
	<body>
          Holberton School
	</body>
       </html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -fs /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo sed -i.backup "s|$MATCH|$STATIC|" /etc/nginx/sites-available/default

sudo service nginx restart
