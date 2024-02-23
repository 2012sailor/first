from typing import IO
from tornado.httpserver import HTTPServer
from tornado.wsgi import WSGIContainer
from serverFlask import app
from tornado.ioloop import IOLoop

s=HTTPServer(WSGIContainer(app))
s.listen(5001)
IOLoop.current().start()