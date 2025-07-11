# Se importan los módulos que se van a utilizar 
import requests
import json
from pathlib import Path

class PetStoreAPI:
    #URL base de la API de PetStore
    BASE_URL = "https://petstore.swagger.io/v2"

    def __init__(self):
        #Encabezados que se va a utilizar para todas las solicitudes post (tipo JSON)
        self.headers = {
            "Content-Type": "application/json"
        }

    
    #Método reutilizable para cargar archivos JSON y evitar duplicar lógica en cada método de solicitud
    def _load_payload(self, json_path):
        # Se carga y retorna el contenido de un archivo JSON
        file_path = Path(json_path)
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
        
    def create_pet(self, json_path):
        #Realizar una solicitud POST para crear una mascota
        payload = self._load_payload(json_path)
        response = requests.post(f"{self.BASE_URL}/pet",
                                headers=self.headers, 
                                json=payload)
        
        return response 
    
    def create_order(self, json_path):
        #Realizar una solicitud POST para crear un pedido
        payload = self._load_payload(json_path)
        response = requests.post(f"{self.BASE_URL}/store/order",
                                headers=self.headers, 
                                json=payload)
        
        return response
    
    def create_user(self, json_path):
        #Realizaruna solicitud POST para crear un usuario
        payload = self._load_payload(json_path)
        response = requests.post(f"{self.BASE_URL}/user",
                                headers=self.headers, 
                                json=payload)
        
        return response