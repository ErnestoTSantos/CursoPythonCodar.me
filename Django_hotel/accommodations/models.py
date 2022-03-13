from django.db import models


class Company(models.Model):

    STATES_CHOICE = (
        ('DT', 'Default'),
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    )

    name = models.CharField('Nome da empresa', max_length=40, unique=True)
    since = models.DateField('Fundação da empresa')
    description = models.TextField('Descrição da empresa')
    addition_date = models.DateField('Data de adição', auto_now_add=True)
    state = models.CharField('Estado', default='DT', choices=STATES_CHOICE, max_length=20)  # noqa:E501
    address = models.CharField('Endereço', max_length=50)

    def __str__(self):
        return self.name

    @classmethod
    def create_company(cls, name, since, description, state, address):

        if not name:
            raise ValueError('A empresa precisa de um nome!')

        if not since:
            raise ValueError('A empresa precisa ter a data que foi fundada!')

        if not state:
            raise ValueError(
                'A empresa preicsa ter o estado que está localizada!')

        if not address:
            raise ValueError('A empresa precisa ter um endereço!')

        company = Company(name=name, since=since, description=description, state=state, address=address)  # noqa:E501

        company.save()

        return company


class Accommodation(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Empresa')  # noqa:E501
    accommodation_name = models.CharField('Nome do quarto/casa', max_length=20)
    description = models.TextField('Descrição do quarto/casa')
    addition_date = models.DateField('Data de adição do quarto/casa', auto_now_add=True)  # noqa:E501
    times_rented = models.IntegerField('Número de vezes alugado', default=0, blank=True)  # noqa:E501
    price = models.FloatField('Preço')
    number_of_people = models.IntegerField('Acomodações')

    def __str__(self):
        return f'{self.accommodation_name}'

    @classmethod
    def create_accommodation(cls, company, name, description, price, people):

        if not isinstance(company, Company):
            raise ValueError('O quarto/casa precisa ter uma empresa!')

        if not name:
            raise ValueError('O quarto/casa precisa ter um nome!')

        if not description:
            raise ValueError('O quarto/casa precisa de uma descrição!')

        if not price:
            raise ValueError('O quarto precisa ter um preço!')

        if not people:
            raise ValueError('O quarto/casa precisa ter um número de pessoas!')

        accommodation = Accommodation(company=company, accommodation_name=name, description=description, price=price, number_of_people=people)  # noqa:E501

        accommodation.save()

        return accommodation
