@ECHO OFF

docker rm -f image-host python-api
docker run -d -p 8080:8080 --name image-host image-host
docker run -d -p 51115:51115 --volume C:/Users/bbdnet2476/"OneDrive - BBD Software Development"/Desktop/pythonInDocker/pythonAPI/images:/data --name python-api python-api