from django.http import HttpResponse
from django.utils.html import escape
import os
import sys
import cgi
from cgi import parse_qs

def hello(request):
    data = '''Hello, world! </br>
        <form method="POST">
            <label>Method POST</label>
            <input type="text" name="examplePost">
            <input type="submit" value="Go">
        </form>
        '''
    get_data = request.GET
    
    post_data = request.POST.get("examplePost", "")
    output = data + "</br>Your POST data: "  + post_data + "</br>"

    for key, values in get_data.iteritems():
        output += b'Your GET parameter: ' + key + ' has values: '
        for value in values:
            output += b'' + value + ', </br>'
    
    return HttpResponse((output))

def index(request):
    return HttpResponse((output))