FROM python:3.11
WORKDIR /app
COPY ./requirements.txt ./ 
RUN pip3 install -r requirements.txt
COPY ./app.py ./
EXPOSE 5000
ENTRYPOINT [ "python3", "app.py" ]