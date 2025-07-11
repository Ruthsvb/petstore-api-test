from locust import HttpUser, task, between
import json


#se define una clase que simula el comportamiento de un usuario
class PetstoreUser(HttpUser):
    #se define el tiempo de espera entre las solicitudes
    wait_time = between(1, 3)

    #se define el host (URL base) de la API que se va a probar
    host = "https://petstore.swagger.io/v2"
    

    @task
    def create_pet(self):
        #Se carga el payload desde el archivo json new_pet.json
        with open("data/new_pet.json") as f:
            payload = json.load(f)

        #Se envia la solicitud POST para crear una mascota
        self.client.post("/pet",json=payload)

    @task   
    def create_order(self):
        #Se carga el payload desde el archivo json new_order.json
        with open("data/new_order.json") as f:
            payload = json.load(f)

        #Se envia la solicitud POST para crear un pedido
        self.client.post("/store/order", json=payload)

    @task   
    def create_user(self):      
        #Se carga el payload desde el archivo json new_user.json
        with open("data/new_user.json") as f:
            payload = json.load(f)

        #Se envia la solicitud POST para crear un usuario
        self.client.post("/user", json=payload)