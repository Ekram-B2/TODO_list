from flask import Flask, Blueprint
from api.todo_list import ns as list_ns
from api import rest_api
from itemlist.listmanager import SimpleListManager
def create_app():
    # 1. Create a instance of flask
    app = Flask(__name__)
    # 2. Define root path
    @app.route("/")
    def root():
        print("the root path was pinged!")
        return "You have reached the todo list application. Welcome!"

    blueprint = Blueprint('api', __name__, url_prefix='/api')
    rest_api.init_app(blueprint)
    rest_api.add_namespace(list_ns)
    app.register_blueprint(blueprint)
    # 3. Return the app
    return app

if __name__ == "__main__":
    app = create_app()
    if not app:
        print("application was not successfully created")
    registry = SimpleListManager()
    print("The Application was successfully created.")
    app.run(host="0.0.0.0", port="8080")