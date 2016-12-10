from pyramid.response import FileResponse
from pyramid.config import Configurator
from wsgiref.simple_server import make_server

def about_page(request):
    page = FileResponse('about/aboutme.html', request=request, content_type='text/html')
    return page
def index_page(request):
    page = FileResponse('index.html', request=request, content_type='text/html')
    return page

if __name__ == '__main__':
    configur = Configurator()
    configur.add_view(index_page, route_name='index')
    configur.add_route("index",'/')
    configur.add_view(about_page, route_name='aboutme')
    configur.add_route('aboutme', 'about/aboutme.html')
    make_server('localhost', 8000, configur.make_wsgi_app()).serve_forever()