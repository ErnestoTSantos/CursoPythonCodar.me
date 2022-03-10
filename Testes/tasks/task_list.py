from datetime import date


class TaskList:
    def __init__(self):
        """
        _atributo indica que "_atributo" não deve ser acessado diretamente fora dessa classe.
        Vamos criar métodos que retornam esses atributos de acordo com uma certa lógica.
        """
        self._tasks = []
        self._number_of_tasks = 0

    def add_task(self, task):
        """
        Adiciona uma tarefa na lista (_tarefas.append).
        """
        self._tasks.append(task)

    def get_tasks(self, include_completed=False):
        """
        Retorna lista de tarefas restantes.
        Se incluir_concluidas for passado como True, inclui as tarefas concluídas.
        """
        unfinished_tasks = []
        for task in self._tasks:
            if not task.completed:
                unfinished_tasks.append(task)
        return unfinished_tasks

    def get_late_tasks(self):
        """
        Retorna a lista de tarefas atrasadas. Ver método: Tarefa.atrasada.
        """
        late_tasks = []

        dt_td = date.today()

        for task in self._tasks:
            if dt_td > task.date:
                late_tasks.append(task)

        return late_tasks

    def get_tasks_for_today(self):
        """
        Retorna a lista de tarefas que tenham data = hoje.
        """
        day_tasks = []

        dt_td = date.today()

        for task in self._tasks:
            if dt_td == task.date:
                day_tasks.append(task)

        return day_tasks
