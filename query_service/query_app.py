from query_service.query_web import create_app


app = create_app('development')

if __name__ == '__main__':
    app.run(host="0.0.0.0")
    # app.run(debug=True)
