# syntax=docker/dockerfile:1
FROM ubuntu:latest
RUN apt-get update \
    && apt-get install -y \
        python3-pip \
    && pip install \
        tornado \
        Pillow
EXPOSE 51115
COPY . .
CMD ["python3", "host-app.py"]