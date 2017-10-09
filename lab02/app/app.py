import os
import redis 

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response, FileResponse

r = redis.Redis(host='redis')

CONTAINER_ID = os.environ['HOSTNAME']

def puppy(request):
   return FileResponse(
             '/var/puppy.jpg',
             request=request,
             content_type='image/jpg'
          )

def home(request):
    r.incr(CONTAINER_ID, amount=1)
    return {
        'container_id': CONTAINER_ID,
        'count': int(r.get(CONTAINER_ID))
    }

if __name__ == '__main__':
    with Configurator() as config:

        r.set(CONTAINER_ID,0)

        config.include('pyramid_jinja2')
        config.add_route('home', '/')
        config.add_route('puppy','puppy.jpg')
        config.add_view(home, route_name='home',renderer='index.jinja2')
        config.add_view(puppy, route_name='puppy')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
