#dockerfile
FROM tiangolo/uwsgi-nginx-flask:python3.6
COPY requirements.txt /tmp/
ENV STATIC_PATH /app/app/base/static
ENV STATIC_URL /static
RUN pip install -U pip
RUN pip install -r /tmp/requirements.txt
COPY . /app