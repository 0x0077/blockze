from sanic import Sanic
from sanic_cors import CORS
from sanic.response import text, html


app = Sanic(__name__)
app.static('/assets', './assets')

app.config.FORWARDED_SECRET = "SERVER_KEY"
app.config['CORS_AUTOMATIC_OPTIONS'] = True

CORS(app)


@app.route("/")
async def index(request):
    with open("templates/index.html", "r") as f:
        html_content = f.read()
    return html(html_content)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, fast=True, debug=True, access_log=False)

