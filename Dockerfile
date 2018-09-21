FROM python:3.6-slim
MAINTAINER youngsyang@outlook.com
RUN mkdir /opt/flasto-service
WORKDIR /opt/flasto-service
COPY ./ ./
RUN pwd && ls -la && mkdir query_service/log && ls -la query_service && pip3 install --no-cache-dir -r requirements.txt
CMD ["gunicorn", "-c", "query_service/gun_query_app.py", "query_app:app"]
EXPOSE 5678