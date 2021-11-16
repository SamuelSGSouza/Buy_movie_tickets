from utils.browsers import MyBrowser


class BuyTicket:
    def __init__(self, browser_opened: MyBrowser, tickets_required: int) -> None:
        self.browser = browser_opened
        self.tickets_required = tickets_required

    def select_seat(self):
        '''pegar lista todos os assentos disponíveis, ou pegar lista todos os assentos
        ocupados e todos os assentos da sala e subtrair assentos ocupados da lista de todos

        separar assentos por letra

        fileiras verificar quais possuem o número de cadeiras solicitadas

        pegar a fileira (fila) do meio

        se houverem cadeiras vazias no meio, selecionar quaisquer cadeiras. Senão,
        verificar uma fileira acima e uma abaixo até encontrar disponibilidade

        '''

    def fill_registration(self):
        '''
        verificar informações requeridas ao cadastro

        acessar arquivo com informações e enviar dados para o browser
        '''

    def buy(self):
        '''Chama fill_registration() e depois clica em pagar'''
