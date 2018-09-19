# flasto-service

> presto 查询接口

基于 `flask`，`gunicorn`，`gevent` presto 查询服务

## Installation

### git

```shell
> $ git clone http://gitlab.fp.bd14.com/bigdata/flasto-service.git
```

## Development

如果你要在本地对其进行开发，遵循以下步骤:

* 创建并启动虚拟环境，安装依赖
    ```shell
    > $ cd flasto-service
    > $ virtualenv -p <path-to-python3-interpreter> --no-site-packages venv
    > $ source venv/bin/activate
    (venv) > $ pip3 install --no-cache-dir -r requirements.txt
    ```
    
* 功能程序按照目录结构进行对应开发
    ```text
    query_api
    ├── <project name>
    │   ├── __init__.py
    │   ├── db_utils <数据库工具模块>
    │   │   ├── __init__.py
    │   │   └── <your module>.py
    │   ├── entity <flask-restplus 解析的实体>
    │   │   ├── dto <request 参数实体>
    │   │   │   ├── __init__.py
    │   │   │   └── xxx_req_dto.py
    │   │   └── po <response 结果实体>
    │   │       ├── __init__.py
    │   │       └── <your response name>.py
    │   └── service <服务接口>
    │       └── xxx_service.py
    └── resources <资源文件，包括查询 sql 和 pandas 的 dtype 字典>
        └── <project name>
            ├── dtypes
            │   ├── __init__.py
            │   └── dtypes_<your response name>_data.py
            └── query_sql
                ├── __init__.py
                └── query_<your response name>_data.py
    ```
    
* `config.py`: flask app 配置

* `gun.py`: gunicorn 配置

## Start Up

### local

```shell
cd predict-service
gunicorn -c gun.py application:app
```

### docker

```shell
docker-compose up -d
```

## Usage

访问 `http://<服务启动机器的ip>:5678/flasto/api` 查看 API 文档
