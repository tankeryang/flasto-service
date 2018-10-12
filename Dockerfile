FROM python:3.6-slim
MAINTAINER youngsyang@outlook.com
WORKDIR /opt/flasto-service
COPY ./ ./
RUN mkdir query_service/log \
    && pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir -r requirements.txt \
    && chmod +x entrypoint.sh
ENTRYPOINT ["sh", "entrypoint.sh"]
EXPOSE 5678