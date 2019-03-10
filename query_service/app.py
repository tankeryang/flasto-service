from query_service import create_app


app = create_app('preprod')


if __name__ == '__main__':
    app.run(debug=True)
