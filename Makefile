# MakeFile to deploy the Sample US CENSUS Name Data 
# server using Python Microservice
# For MATH318 Software Development

all: PutHTML

PutHTML:
	cp shake.html /var/www/html/shakePy/
	cp shake.css /var/www/html/shakePy/
	cp shake.js /var/www/html/shakePy/

	echo "Current contents of your HTML directory: "
	ls -l /var/www/html/shakePy/
