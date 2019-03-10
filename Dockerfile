FROM flasto-service-base:latest
MAINTAINER youngsyang@outlook.com
WORKDIR /opt/flasto-service
COPY ./ ./
RUN mkdir query_service/log \
    && mkdir query_service/tmp \
    && chmod +x docker-entrypoint.sh
ENTRYPOINT ["sh", "docker-entrypoint.sh"]
EXPOSE 5678
