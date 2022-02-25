from flask import Flask, abort, jsonify, request
from flask.views import MethodView

from models.events import Events
from models.onLineEvents import OnLineEvent, events

app = Flask(__name__)


def get_element(id):
    for event in events:
        if event.id == id:
            return event
    abort(404, f'Não foi possível encontrar o elmento de id:{id}!')


class RouteEvent(MethodView):

    @app.errorhandler(400)
    @app.errorhandler(404)
    def not_found(error):
        return (jsonify(error=error.description), error.code)

    def get(self):
        events_list = []

        for event in events:
            events_list.append(event.__dict__)

        return jsonify(events_list)

    def get_element(self, id):
        event = get_element(id)
        return jsonify(event.__dict__)

    def post(self):
        data = request.get_json()
        name = data.get('name')
        localization = data.get('localization')

        if not name:
            abort(400, "'name' precisa ser informado!")

        if localization:
            event = Events(name, localization)
        else:
            event = OnLineEvent(name)

        events.append(event)

        return {
            "id": event.id,
            "name": event.name,
            "url": f"/api/events/{event.id}/"
        }

    def delete(self, id):
        event = get_element(id)
        events.remove(event)
        return (jsonify(id=event.id), 200)

    def put(self, id):
        data = request.get_json()
        name = data.get('name', None)
        localization = data.get('localization', None)

        event = get_element(id)
        if not name:
            abort(400, "'name' precisa ser informado!")

        if not localization:
            abort(400, "'localization' precisa ser infromada!")

        event.name = name
        event.localization = localization

        return jsonify(event.__dict__)

    def patch(self, id):
        data = request.get_json()

        event = get_element(id)

        if "name" in data.keys():
            name = data.get("name")
            if not name:
                abort(400, "'name' precisa ser informado!")
            elif name is None:
                abort(400, "'name' precisa ser informado!")
            event.name = name

        if "localization" in data.keys():
            localization = data.get("localization")
            if not localization:
                abort(400, "'localization' precisa ser informado!")
            elif localization is None:
                abort(400, "'localization' precisa ser informado!")
            event.localization = localization

        return jsonify(event.__dict__)


app.add_url_rule('/api/events/', view_func=RouteEvent.as_view('events'))
app.add_url_rule('/api/events/<int:id>/',
                 view_func=RouteEvent.as_view('eventsDetails'))
