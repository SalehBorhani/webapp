FROM python:alpine
RUN mkdir -p /usr/src/api
WORKDIR /usr/src/api
COPY ./req.txt ./
RUN pip install -r req.txt
COPY ./api_redis.py ./
EXPOSE 80
ENTRYPOINT [ "python3", "api_redis.py" ]