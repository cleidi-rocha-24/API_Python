import requests


class TestPetStoreUserAPI:
    base_url = "https://petstore.swagger.io/v2"
    headers = {"Content-Type": "application/json", "accept": "application/json"}

    body = {
        "id": 0,
        "username": "joana",
        "firstName": "jo",
        "lastName": "Silva",
        "email": "tst@tst.com.br",
        "password": "12345",
        "phone": "51999999999",
        "userStatus": 0
    }

    body_atualizacao = {
        "id": 0,
        "username": "cleidoca",
        "firstName": "CleidiUpdate",
        "lastName": "SilvaUpdate",
        "email": "tst2@tst2.com.br",
        "password": "54321",
        "phone": "51988888888",
        "userStatus": 0
    }

    def test_post(self):
        response = requests.post(
            f"{self.base_url}/user",
            json=self.body,
            headers=self.headers
        )

        print(f"\n\nExecutando POST, via url: {self.base_url}/user")
        print(f"Criação de usuário via serviço POST. Esperando status code 200. Retornado:{response.status_code}")
        print(f"Response body POST:{response.text}")

        assert response.status_code == 200
        print(f"Usuário criado com sucesso. Via servico POST")

        json = response.json()

        assert json["code"] == 200
        assert json["type"] == "unknown"
        assert "message" in json

    def test_get(self):
        username = self.body["username"]
        response = requests.get(
            f"{self.base_url}/user/{username}",
            headers=self.headers
        )

        print(f"\n\nExecutando GET, via url: {self.base_url}/user/{username}")
        print(f"Busca de usuário via serviço GET. Esperando status code 200. Retornado:{response.status_code}")
        print(f"Response body GET:{response.text}")

        assert response.status_code == 200

        json = response.json()

        assert json["username"] == self.body["username"]
        assert json["email"] == self.body["email"]
        assert json["firstName"] == self.body["firstName"]
        assert json["lastName"] == self.body["lastName"]

    def test_put(self):
        response = requests.put(
            f"{self.base_url}/user/{self.body['username']}",
            json=self.body_atualizacao,
            headers=self.headers
        )

        print(f"\n\nExecutando PUT, via url: {self.base_url}/user/{self.body['username']}")
        print(f"Atualização de usuário via serviço PUT. Esperando status code 200. Retornado:{response.status_code}")
        print(f"Response body PUT:{response.text}")

        assert response.status_code == 200, "Falha ao atualizar usuário"

    def test_verifica_atualizacao(self):
        novo_usuario = self.body_atualizacao["username"]
        response = requests.get(
            f"{self.base_url}/user/{novo_usuario}",
            headers=self.headers
        )

        print(f"\n\nExecutando GET para verificar atualizaçao, via url: {self.base_url}/user/{novo_usuario}")
        print(f"Busca de usuário via serviço GET. Esperando status code 200. Retornado:{response.status_code}")
        print(f"Response body GET:{response.text}")

        assert response.status_code == 200

        json = response.json()

        assert json["username"] == self.body_atualizacao["username"]
        assert json["email"] == self.body_atualizacao["email"]
        assert json["firstName"] == self.body_atualizacao["firstName"]
        assert json["lastName"] == self.body_atualizacao["lastName"]


    def test_delete(self):
        usuario = self.body_atualizacao['username']
        response = requests.delete(
            f"{self.base_url}/user/{usuario}",
            headers=self.headers
        )

        print(f"\n\nExecutando DELETE, via url: {self.base_url}/user/{usuario}")
        print(f"Remoção de usuário via serviço DELETE. Esperando status code 200. Retornado:{response.status_code}")
        print(f"Response body DELETE:{response.text}")

        assert response.status_code == 200
        print("Usuário deletado com sucesso")

        response = requests.get(
            f"{self.base_url}/user/{usuario}",
            headers=self.headers
        )
        assert response.status_code == 404, "Usuário ainda existe após deleção"
        print("Usuário não encontrado após deleção (como esperado)")
