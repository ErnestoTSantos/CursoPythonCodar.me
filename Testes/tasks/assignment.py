from datetime import date, timedelta


class Assignment:
    def __init__(self, title, description="", date=None, date_notification=None):
        self.title = title
        self.description = description
        self.date = date
        self.date_notification = date_notification
        self.completed = False

    def conclude(self):
        """
        Define essa tarefa como concluida.
        """
        self.completed = True

    def add_description(self, description):
        """
        Adiciona uma descrição para a tarefa.
        """
        self.description = description

    def defer_notification(self, minutes):
        """
        Adia a notificação em uma certa quantidade de minutos.
        Notificacao: 25/02/2022, 14h30
        adiar_notificacao(15)
        => Notificacao: 25/02/2022, 14h45
        """
        if self.date_notification is None:
            return

        self.date_notification += timedelta(minutes=minutes)

    def late(self):
        """
        Diz se tarefa está atrasada. Ou seja, data < hoje.
        """
        dt_td = date.today()

        return dt_td > self.date
