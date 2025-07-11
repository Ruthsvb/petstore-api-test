from locust import HttpUser, task, between
from petstore_api import PetStoreAPI


#se define una clase que simula el comportamiento de un usuario
class PetstoreUser(HttpUser):
    #se define el tiempo de espera entre las solicitudes
    wait_time = between(1, 3)
    
   
    def on_start(self):
    #Se ejecuatara cuando el usuario virtual "arranca"
    #Se inicializa la instancia de PetstoreAPI
        self.api = PetstoreAPI()

        @task
        def create_pet(self):
            #Se envia la solicitud para crear una mascot
            self.api.create_pet("data/create_pet.json")

        @task   
        def create_order(self):
            #Se envia la solicitud para crear un pedido
            self.api.create_order("data/create_order.json")

        @task   
        def create_user(self):
            #Se envia la solicitud para crear un usuario
            self.api.create_user("data/create_user.json")
