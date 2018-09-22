# flasto-service

> presto 集群服务

基于 `flask`，`gunicorn`，`gevent` 调用 presto 资源进行查询或其它操作

## Installation

### git & virtualenv

```shell
> $ git clone http://gitlab.fp.bd14.com/bigdata/flasto-service.git
> $ cd flasto-service
> $ virtualenv -p <path-to-python3-interpreter> --no-site-packages venv
> $ source venv/bin/activate
(venv) > $ pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir -r requirements.txt
```

## Development

如果你要在本地对其进行开发，遵循以下步骤:

* 创建并启动虚拟环境，安装依赖
    ```shell
    > $ cd flasto-service
    > $ virtualenv -p <path-to-python3-interpreter> --no-site-packages venv
    > $ source venv/bin/activate
    (venv) > $ pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir -r requirements.txt
    ```
    
* 目录结构
    ```
    flasto-service
    ├── docker_compose: docker-compose 文件
    ├── query_service: 查询服务
    │   ├── query_api: 查询接口定义
    │   ├── query_biz: 查询接口实现
    │   ├── query_web (web服务):
    │   │   └── config.py: web app 配置
    │   ├── resource: 资源文件
    │   ├── gun_query_app.py: gunicorn 配置
    │   └── query_app.py: web app 启动脚本
    └── test: 测试脚本
    ```

## Start Up

### local

* __query service__

    ```shell
    > $ cd flasto-service
    > $ source venv/bin/activate
    (venv) > $ gunicorn -c query_service/gun_query_app.py query_app:app
    ```

### docker

* __build & run__
    ```shell
    > $ docker-compose -f docker_compose/docker-compose.build.yml up -d
    ```

* __local testing__
    ```shell
    > $ docker-compose -f docker_compose/docker-compose.local.yml up -d
    ```

* __prod deploy__
    ```shell
    > $ docker-compose -f docker_compose/docker-compose.yml up -d
    ```

## Usage

* __query service__

    访问 `http://<host ip>:5678/flasto/api` 查看 API 文档
