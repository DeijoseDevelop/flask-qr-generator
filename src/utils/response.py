import json

from flask import Response


class CustomResponse(Response):
    def __init__(self, content='', status=200, headers=None, mimetype='application/json', **kwargs):
        super().__init__(response=json.dumps(content), status=status, headers=headers, mimetype=mimetype, **kwargs)