import app as boot
from config import Config
from gevent.pywsgi import WSGIServer
app = boot.create_app()

if __name__ == "__main__":
    http_server = WSGIServer((Config.APP_HOST, Config.APP_PORT), app)
    http_server.serve_forever()
