from flask import Flask, abort, jsonify, make_response
from modules.events import Events
from modules.onLineEvents import OnLineEvent, events

app = Flask(__name__)


class RoutesEvents:
    # Como se fosse um método estático
    @app.route("/")
    def index():
        return "<h1>Flask configurado com sucesso!</h1>"

    @app.route("/api/events/")
    def listing_events():
        events_dict = []
        for event in events:
            events_dict.append(event.__dict__)

        return jsonify(events_dict)

    @app.errorhandler(404)
    def not_found(error):
        return (jsonify(error=str(error)), 404)

    @app.route("/api/events/<int:id>/")
    def detail_event(id):
        for event in events:
            if event.id == id:
                return jsonify(event.__dict__)

        abort(404, f"Evento com id: {id}, não pode ser encontrado!")
