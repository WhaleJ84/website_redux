FROM tiangolo/meinheld-gunicorn-flask:python3.8
COPY ./ /app
RUN pip install --upgrade pip \
&& pip install -r requirements.txt \
&& pip install -r dev-requirements.txt
