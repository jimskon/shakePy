# shakePy
## A python microservice for looking up words in shakspeare
 - https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3
 - https://pypi.org/project/Flask-Cors/

## Prequisites
 - Apache2 muct be installed
 - Ports 5000-5005 must be open on the VM firewall

## Setup pip3, Flask and FLASK-CORS
 - ```sudo apt install python3-pip```
 - ```sudo apt install python3-flask```
 - ```pip3 install -U flask-cors```

## Edit Javascript IP address to your VM address
 - Edit ```shake.js``` so that ```baseUrl``` is your VM's IP address
 
## Setup app (from command line)
 - ```sudo mkdir /var/www/html/shakePy```
 - ```sudo chown ubuntu /var/www/html/shakePy```
 - ```make```
 - ```./start.sh```

## To test port access
 - ```socat -u tcp-l:5001,fork system:./porttest.sh```

Then web to the http://ip:port
