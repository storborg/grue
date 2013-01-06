from gevent.wsgi import WSGIServer

from grue.app import make_app


app = make_app()
server = WSGIServer(('0.0.0.0', 8080), app)
server.serve_forever()
