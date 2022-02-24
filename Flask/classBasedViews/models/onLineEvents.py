from .events import Events


class OnLineEvent(Events):

    def __init__(self, name, _=''):
        place = f'https://tamarcado.com/eventos?id={OnLineEvent.id}'
        super().__init__(name, place)

    def show_informations(self):
        print(f'Event ID: {self.id}')
        print(f'Event name: {self.name}')
        print(f'Link to acess event: {self.localization}')
        print('-' * 20)


ev_1 = Events("Javascript class", "Florianópolis")
ev_2 = Events("Python class", "Rio grande do Sul")
ev_3 = OnLineEvent('Live coding Python')
ev_4 = OnLineEvent('Live coding JavaScript')

events = [ev_1, ev_2, ev_3, ev_4]
