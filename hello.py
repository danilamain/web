def app(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    data =[bytes(i + '\n') for i in environ['QUERY_STRING'].split('&')]
    start_response(status, headers)
    return data
