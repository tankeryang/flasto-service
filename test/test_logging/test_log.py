from test.test_logging.web_service.web_app import create_app

app = create_app('production')


if __name__ == '__main__':

    app.run(debug=True)