#!/usr/bin/env bash
#sets up your web servers for the deployment of web_static

STATIC="server_name _;\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n}"
MATCH="server_name _;"
mkdir /data/
mkdir /data/web_static/
mkdir /data/web_static/releases/
mkdir /data/web_static/releases/test/
mkdir /data/web_static/shared/

echo "<html>
  	<head>
    	</head>
	<body>
          Holberton School
	</body>
       </html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -fs /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo sed -i.backup "s|$MATCH|$STATIC|" /etc/nginx/sites-available/default

sudo service nginx restart
