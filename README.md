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
    ├── docker_deploy: docker部署脚本
    ├── schedule_service: 定时器任务, 用于清空tmp下生成的导出文件和redis缓存
    ├── query_service: 查询服务
    │   ├── apis: api 服务
    │   ├── resource: 资源文件
    │   ├── __init__.py: flask app 初始化
    │   ├── gun_config.py: gunicorn 配置
    │   ├── config.py: app 配置
    │   ├── exts.py: flask 插件
    │   └── app.py: app 启动脚本
    └── test: 测试脚本
    ```

## Start Up

### local with gunicorn

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

#### build base image and network

```bash
> $ sh build-base.sh
```

#### run redis container

```bash
> $ sh start-redis.sh
``` 

#### docker compose up

* __dev__
    ```bash
    > $ docker-compose -f docker_deploy/docker-compose.dev.yml up -d
    ```

* __prod__
    ```bash
    > $ docker-compose -f docker_deploy/docker-compose.prod.yml up -d
    ```

## Usage

* __query service__

    访问 `http://<host>:<port>/flasto/api` 查看 API 文档
