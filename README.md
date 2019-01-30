# flasto-service

> presto 集群服务

基于 `flask`，`gunicorn`，`gevent` 调用 presto 资源进行查询或其它操作

## Installation

### git & virtualenv

```bash
> $ git clone http://gitlab.fp.bd14.com/bigdata/flasto-service.git
> $ cd flasto-service
> $ # <path-to-python3-interpreter> 为你的 python3 解释器路径, 如: /usr/local/bin/python3.6, 建议 python3.6+ 版本
> $ virtualenv -p <path-to-python3-interpreter> --no-site-packages venv
> $ source venv/bin/activate
(venv) > $ pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir -r requirements.txt
```

## Development

如果你要在本地对其进行开发，遵循以下步骤:

* 创建并启动虚拟环境，安装依赖
    ```bash
    > $ cd flasto-service
    > $ # <path-to-python3-interpreter> 为你的 python3 解释器路径, 如: /usr/local/bin/python3.6, 建议 python3.6+ 版本
    > $ virtualenv -p <path-to-python3-interpreter> --no-site-packages venv
    > $ source venv/bin/activate
    (venv) > $ pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir -r requirements.txt
    ```
    
* 目录结构
    ```
    flasto-service
    ├── docker_deploy: docker-compose 文件
    ├── aps_service: 定时器任务, 用于清空 tmp 下生成的导出文件
    ├── query_service: 查询服务
    │   ├── query_api: 查询接口定义
    │   ├── query_biz: 查询接口实现
    │   ├── query_web: web服务实现
    │   │   └── config.py: web app 配置
    │   ├── resource: 资源文件
    │   ├── gun_query_app.py: gunicorn 配置
    │   └── query_app.py: web app 启动脚本
    └── test: 测试脚本
    ```

## Start Up

### local

* __start up__

    ```bash
    > $ cd flasto-service
    > $ source venv/bin/activate
    (venv) > $ sh gunicorn-startup.sh
    ```

* __stop__

    ```bash
    > $ cd flasto-service
    > $ source venv/bin/activate
    (venv) > $ sh gunicorn-kill.sh
    ```

### docker

* __build & run on local__
    ```shell
    > $ docker-compose -f docker_deploy/docker-compose.build-local.yml up -d
    ```

* __build & run on remote(prod) server__
    ```shell
    > $ docker-compose -f docker_deploy/docker-compose.build-remote.yml up -d
    ```

* __run & develop on local (already build)__
    ```shell
    > $ docker-compose -f docker_deploy/docker-compose.dev.yml up -d
    ```

* __run on local (already build)__
    ```shell
    > $ docker-compose -f docker_deploy/docker-compose.local.yml up -d
    ```

* __run on remote(prod) server__
    ```shell
    > $ docker-compose -f docker_deploy/docker-compose.yml up -d
    ```

## Usage

* __query service__

    访问 `http://<host>:5678/flasto/api` 查看 API 文档
