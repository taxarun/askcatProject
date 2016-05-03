#!/usr/bin/env python
import os
import sys
import cgi
from cgi import parse_qs

form = b'''
    <html>
        <head>
            <title>GET & POST Hello World!</title>
        </head>
        <body>
            <form method="POST">
                <label>Method POST</label>
                <input type="text" name="examplePost">
                <input type="submit" value="Go">
                <p>
    '''

def app(environ, start_response):
    
    html = form
    
    if environ['REQUEST_METHOD'] == 'POST':
        post_env = environ.copy()
        post_env['QUERY_STRING'] = ''
        post = cgi.FieldStorage(
                                fp=environ['wsgi.input'],
                                environ=post_env,
                                keep_blank_values=True
                                )
        html += b'Your POST parameter: ' + post['examplePost'].value + ';'

    if environ['REQUEST_METHOD'] == 'GET':
        params = parse_qs(environ['QUERY_STRING'])
        for key, values in params.iteritems():
            html += b'Your GET parameter: ' + key + ' has values: '
            for value in values:
                html += b'' + value + ', </br>'

    end = b'''
                </p>
                </form>
            </body>
        </html>
    '''
    html += end

    start_response('200 OK', [('Content-Type', 'text/html')])
    return [html]

if __name__ == '__main__':
    try:
        from wsgiref.simple_server import make_server
        httpd = make_server('127.0.0.1', 8081, app)
        print('Server is up on port 8081')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print(' Oh no, I died .-.')
