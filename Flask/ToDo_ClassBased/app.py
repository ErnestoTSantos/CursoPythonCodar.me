from flask import Flask, abort, jsonify, request
from flask.views import MethodView

from models.to_do import ToDo
from models.users import chores, users

app = Flask(__name__)


def get_element_or_404(name, id):
    chore_list = []
    if name != '' and id != 0:
        for chore in chores:
            if chore.id == id:
                if chore.user_name == name:
                    if chore.active is True:
                        return chore.__dict__
    elif name != '':
        for chore in chores:
            if chore.active is True:
                if chore.user_name == name:
                    chore_list.append(chore.__dict__)

        return chore_list
    else:
        for chore in chores:
            if chore.active is True:
                chore_list.append(chore.__dict__)

        return chore_list

    abort(404, f'Não foi possível encontrar o elemento de id:{id}! Verifique as informações e envie novamente!')  # noqa:E501


def update_element_or_404(name, id):
    for chore in chores:
        if chore.user_name == name:
            if chore.id == id:
                return chore

    abort(404, f'Não foi possível encontrar o elemento de id:{id}! Verifique as informações e envie novamente!')  # noqa:E501


def get_user_or_404(name):
    for user in users:
        if user.name == name:
            return user

    abort(404, f'Não foi possível encontrar o usuário:{name}! Verifique as informações e envie novamente!')  # noqa:E501


def delete_chore(name, id):
    for chore in chores:
        if chore.user_name == name:
            if chore.id == id:
                chores.remove(chore)
                return jsonify(id=chore.id)
            else:
                abort(404, f'Não foi possível encontrar a tarefa de id: {id}')
        else:
            abort(404, f'Não foi possível encontrar o usuário: {name}')


class ToDoRoutes(MethodView):

    from datetime import date

    @app.errorhandler(400)
    @app.errorhandler(404)
    def errors(error):
        return (jsonify(error=error.description), error.code)

    def get(self, name='', id=0):
        chore = get_element_or_404(name, id)

        return jsonify(chore)

    def post(self, name):
        data = request.get_json()
        active = True

        if 'name' not in data.keys():
            abort(400, "'name' precisa ser informado!")

        if 'final_date' not in data.keys():
            abort(400, "'final_date' precisa ser informada!")

        if 'active' in data.keys():
            active = data.get('active')

        user = get_user_or_404(name)

        chore_name = data.get('name')
        final_date = data.get('final_date')

        new_chore = ToDo(user, chore_name, final_date, active)

        chores.append(new_chore)

        return {
            'id': new_chore.id,
            'name': new_chore.name,
            'active': new_chore.active
        }

    def delete(self, name, id):
        return delete_chore(name, id)

    def put(self, name, id):
        data = request.get_json()

        if 'name' not in data.keys():
            abort(400, "'name' precisa ser informado!")

        if 'final_date' not in data.keys():
            abort(400, "'final_date' precisa ser informada!")

        if 'active' not in data.keys():
            abort(400, "'active' precisa ser informado!")

        chore = update_element_or_404(name, id)

        chore_name = data.get('name')
        final_date = data.get('final_date')
        active = data.get('active')
        update_date = self.date.today().strftime('%d/%m/%Y')

        chore.name = chore_name
        chore.final_date = final_date
        chore.active = active
        chore.update_date = update_date

        return jsonify(chore.__dict__)

    def patch(self, name, id):
        data = request.get_json()

        chore = update_element_or_404(name, id)

        if 'name' in data.keys():
            chore_name = data.get('name')

            if not chore_name:
                abort(400, "'name' precisa ser informado!")
            elif chore_name is None:
                abort(400, "'name' precisa ser informado!")

            chore.name = chore_name

        if 'final_date' in data.keys():
            final_date = data.get('final_date')

            if final_date is None:
                abort(400, "'final_date' precisa ser informado!")

            chore.final_date = final_date

        if 'active' in data.keys():
            active = data.get('active')

            if active is None:
                abort(400, "'active' precisa ser informado!")

            chore.active = active

        update_date = self.date.today().strftime('%d/%m/%Y')
        chore.update_date = update_date

        return jsonify(chore.__dict__)


app.add_url_rule('/api/chores/',
                 view_func=ToDoRoutes.as_view('chores'))
app.add_url_rule('/api/chores/<string:name>/',
                 view_func=ToDoRoutes.as_view('choresUsers'))
app.add_url_rule('/api/chores/<string:name>/<int:id>/',
                 view_func=ToDoRoutes.as_view('choresDetails'))
