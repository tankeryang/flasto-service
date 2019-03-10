#!/usr/bin/env bash
echo "create docker network erm_gw_service..." \
&& docker network create --subnet=192.16.253.1/24 emr_gw_service \
&& echo "build docker image flasto-service-base..." \
&& docker build -t flasto-service-base:latest ./Dockerfile