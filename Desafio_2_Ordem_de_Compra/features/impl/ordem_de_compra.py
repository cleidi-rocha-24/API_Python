import requests
from datetime import datetime


class OrdemDeCompra:
    def __init__(self):
        self.base_url_petstore_order = 'https://petstore.swagger.io/v2/store/order'
        self.id = None
        self.petId = None
        self.quantidade = None
        self.data = datetime.now().isoformat()
        self.status_code = None

        self.header = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }
    def post_criar_uma_nova_ordem(self):

        data = {
            "id": self.id,
            "petId": self.petId,
            "quantity": self.quantidade,
            "shipDate": self.data,
            "status": "placed",
            "complete": True
        }


        response = requests.post(self.base_url_petstore_order, headers=self.header, json=data)
        self.status_code = response.status_code
        return response

    def get_busca_order_id(self):

        response = requests.get(f"{self.base_url_petstore_order}/{self.id}", headers=self.header)
        self.status_code = response.status_code
        return response.json()
