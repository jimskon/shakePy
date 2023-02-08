# shakePy

A python microservice for looking up words in shakspeare

## Setup pip3, Flask and FLASK-CORS
https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
https://pypi.org/project/Flask-Cors/

## Set app (from command line)
 - sudo apt install python3-pip
 - sudo apt install python3-flask
 - pip3 install -U flask-cors
 - sudo mkdir /var/www/html/shakePy
 - sudo chown ubuntu /var/www/html/shakePy
 - make
 - ./start.sh

## To test port access
 - socat -u tcp-l:5001,fork system:./porttest.sh

Then web to the http://ip:port
