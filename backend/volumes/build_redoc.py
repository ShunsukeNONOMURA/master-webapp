import json
from pathlib import Path

from app.main import app

# export openapi
HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <title>My Project - ReDoc</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="shortcut icon" href="https://fastapi.tiangolo.com/img/favicon.png">
    <style>
        body {
            margin: 0;
            padding: 0;
        }
    </style>
    <style data-styled="" data-styled-version="4.4.1"></style>
</head>
<body>
    <div id="redoc-container"></div>
    <script src="https://cdn.jsdelivr.net/npm/redoc/bundles/redoc.standalone.js"> </script>
    <script>
        var spec = %s;
        Redoc.init(spec, {}, document.getElementById("redoc-container"));
    </script>
</body>
</html>
"""
path_output_html = "/root/docs/backend/api.html"
with Path(path_output_html).open("w") as fd:
    print(HTML_TEMPLATE % json.dumps(app.openapi()), file=fd)
path_output_openapi_json = "/root/docs/backend/openapi.json"
with Path(path_output_openapi_json).open("w") as f:
    api_spec = app.openapi()
    f.write(json.dumps(api_spec))
