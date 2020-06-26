from api import rest_api
from flask_restplus import Resource, abort
from flask import request, jsonify
from itemlist.listmanager import registry


ns = rest_api.namespace('tasks', description='task management endpoints')

@ns.route('/')
class Tasks(Resource):
    def get(self):
        tasks = registry.get_all_tasks()
        resp = jsonify(tasks)  
        resp.status_code = 200
        return resp

    def post(self):
        if "task" not in request.form:
             abort(400, "SYSTEM-ERROR: no task provided")
             return
        task = request.form["task"]
        tasks = registry.insert_task(task=task)
        resp = jsonify(tasks)
        resp.status_code = 200
        return resp

    def delete(self):
        if "task" not in request.args:
            abort(400, "SYSTEM-ERROR: no task provided")
            return
        task = request.args["task"]
        tasks = registry.delete_task(task=task)
        resp = jsonify(tasks)
        resp.status_code = 200 
        return resp
       