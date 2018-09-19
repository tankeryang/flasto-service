FROM python:3.6 AS build
MAINTAINER youngsyang@outlook.com
WORKDIR /opt/project
COPY . ./
RUN mkdir log && pip3 install --no-cache-dir -r requirements.txt
CMD ["gunicorn -c gun.py application:app"]

FROM scratch AS prod
COPY --from=build /opt/project/flasto-service ./
CMD ["gunicorn -c gun.py application:app"]
EXPOSE 5678