class ToDo:
    id = 1

    from datetime import date

    def __init__(self, user, name, final_date, active=True):
        self.user_name = user.name
        self.id = ToDo.id
        self.name = name
        self.active = active
        self.create_day = self.date.today().strftime('%d/%m/%Y')
        self.final_date = final_date
        self.update_date = ''
        ToDo.id += 1

    def __str__(self):
        return f'Usuário:{self.user_name}, Tarefa:{self.name}, Ativo:{self.active}, Data de criação:{self.create_day}, Data de conclusão:{self.final_date}'  # noqa:E501
