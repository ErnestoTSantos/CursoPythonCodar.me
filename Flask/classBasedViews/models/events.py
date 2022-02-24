import json


class Events:
    id = 1
    day = 10

    def __init__(self, name, localization=''):
        self.name = name
        self.localization = localization
        self.id = Events.id
        Events.id += 1

    def show_informations(self):
        print(f'Event ID: {self.id}')
        print(f'Event name: {self.name}')
        print(f'Event localization: {self.localization}')
        print('-' * 20)

    def toJSON(self):
        return json.dumps(self.__dict__)

    @staticmethod
    def calculate_people_limit(area):
        if 5 <= area < 10:
            return 5
        elif 10 <= area < 20:
            return 15
        elif area >= 20:
            return 30
        else:
            return 0
