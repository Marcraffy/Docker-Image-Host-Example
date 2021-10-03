# syntax=docker/dockerfile:1
FROM ubuntu:latest
ENV PATH /usr/local/nginx/bin:$PATH
RUN apt-get update && apt-get install -y \
    nginx-common \
    nginx
COPY /nginx.conf /etc/nginx/nginx.conf
EXPOSE 8080
COPY . .
CMD ["nginx", "-g", "daemon off;"]