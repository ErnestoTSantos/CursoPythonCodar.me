from flask import Flask, abort, jsonify, request, url_for

from models.events import Events
from models.onLineEvents import OnLineEvent, events

app = Flask(__name__)


@app.route("/api/eventos/")
def listar_eventos():
    eventos_dict = []
    for ev in events:
        eventos_dict.append(ev.__dict__)
    return jsonify(eventos_dict)


def get_event(id):
    # TODO: implementar get_evento
    for ev in events:
        if ev.id == id:
            return ev
    abort(404, "Evento não encontrado")


@app.route("/api/eventos/<int:id>/")
def detalhar_evento(id):  # view
    ev = get_event(id)
    return jsonify(ev.__dict__)


@app.route("/api/eventos/", methods=["POST"])
def criar_evento():
    json_data = request.get_json()
    name = json_data.get("name", None)
    localization = json_data.get("localization", None)
    if not name:
        abort(400, "'name' deve ser informado")

    if localization:
        new_event = Events(name=name, localization=localization)
    else:
        new_event = OnLineEvent(name=name)

    events.append(new_event)
    return {
        "url": url_for('detalhar_evento', id=new_event.id),
        "id": new_event.id,
        "name": new_event.name,
        "localization": new_event.localization,
    }


@app.route("/api/eventos/<int:id>/", methods=["DELETE"])
def deletar_evento(id):
    evento = get_event(id)  # Vai parar no `abort`
    events.remove(evento)
    return (jsonify(id=evento.id), 200)


# Aceita tanto PATCH quanto PUT
@app.route("/api/eventos/<int:id>/", methods=["PATCH", "PUT"])
def editar_evento(id):
    # TODO: implementar a edição de eventos com PATCH e com PUT
    # Se for PUT, editar o evento completamente
    # Se for PATCH, editar o evento parcialmente

    data = request.get_json()
    name = data.get("name", None)
    localization = data.get("localization", None)

    event = get_event(id)

    if request.method == "PATCH":
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
    elif request.method == "PUT":
        if not name:
            abort(400, "'name' precisa ser informado!")

        if not localization:
            abort(400, "'localization' precisa ser infromada!")

        event.name = name
        event.localization = localization

    return jsonify(event.__dict__)


@app.errorhandler(400)
@app.errorhandler(404)
def handle_status(erro):
    return (jsonify(erro=erro.description), erro.code)
