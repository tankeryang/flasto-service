FROM python:3.6-slim
MAINTAINER youngsyang@outlook.com
WORKDIR /opt/flasto-service
COPY ./ ./
RUN mkdir query_service/log \
    && mkdir query_service/tmp \
    && pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir -r requirements.txt \
    && chmod +x docker-entrypoint.sh
ENTRYPOINT ["sh", "docker-entrypoint.sh"]
EXPOSE 5678