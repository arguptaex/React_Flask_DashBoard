from flask import Flask, request
from flask_smorest import Api

from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint


app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

api.register_blueprint(ItemBlueprint)
api.register_blueprint(StoreBlueprint)


stores =  [
    {
        "name":"My Store",
        "items":[
            {
                "name":"chair",
                "price":15.99
            }
        ]
    }
]

@app.get("/checkllll")  #http://127.0.0.1:5000/store
def get_stores():
    return {"stores":stores}


@app.post("/store")
def create_store():
    request_data = request.get_json()  # when we got this json data it got automatically converted to pyhton dictionary

    new_store = {
        "name":request_data["name"],
        "items":[]
    }

    stores.append(new_store)
    return new_store, 201


@app.post("/store/<string:name>/item")
def create_item(name):
    return name