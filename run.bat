@ECHO OFF
docker run -d -p 8080:8080 --name image-host image-host
docker run -d -p 51115:51115 --name python-api python-api