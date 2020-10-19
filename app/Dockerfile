#dockerfile
FROM tiangolo/uwsgi-nginx-flask:python3.6
ARG ENV
COPY requirements.txt /tmp/
RUN pip install -U pip
RUN pip install -r /tmp/requirements.txt
COPY . /app
RUN if [ "$ENV" = "test" ] ; then mv proxy.py main.py ; else mv run.py main.py && rm proxy.py ; fi