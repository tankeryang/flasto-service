from query_service.query_web import create_app


app = create_app('preproduction')


if __name__ == '__main__':

    app.run()
