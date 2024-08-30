FROM python:3.12.3
LABEL authors="kevin"

WORKDIR /opt/dl-subsidiary

COPY . /opt/dl-subsidiary/

ENTRYPOINT ["sh", "./bin/startup.sh"]

EXPOSE 18088