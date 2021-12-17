from datetime import datetime
import json

def app(environ, start_response):
    url = str(environ['wsgi.url_scheme']) + '://' + str(environ["SERVER_NAME"]) + ":" + str(environ["SERVER_PORT"]),
    str(environ["PATH_INFO"])

    time = str(datetime.now(tz=None))
    data = json.dumps({'url': url[0], 'time': time}).encode()

    start_response("200 OK",
                   [("Content-Type", "application/json"),
                    ("Content-Length", str(len(data)))])

    return iter([data])
  
