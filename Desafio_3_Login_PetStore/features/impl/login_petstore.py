import requests


class LoginPetstore:
    base_url = "https://petstore.swagger.io/v2"
    headers = {
        "Content-Type": "application/json",
        "accept": "application/json"
    }

    def __init__(self):
        self.status_code = None
        self.id = None
        self.username = None
        self.firstName = None
        self.lastName = None
        self.email = None
        self.password = None
        self.phone = None
        self.userStatus = None

    def post_login(self, body):
        url_post_login_list = f"{self.base_url}/user/createWithList"
        response = requests.post(
            url_post_login_list,
            json=body,
            headers=self.headers
        )

        print(f"\n\nExecutando POST, via url: {url_post_login_list}")
        print(f"Criação de usuário via serviço POST. Status code retornado:{response.status_code}")
        print(f"Response body POST:{response.text}")

        self.status_code = response.status_code
        return response.json()

    def get_login(self, username):
        url_get_login_list = f"{self.base_url}/user/{username}"
        response = requests.get(
            url_get_login_list,
            headers=self.headers
        )

        print(f"\n\nExecutando GET, via url: {url_get_login_list}")
        print(f"Busca de usuário via serviço GET. Status code retornado:{response.status_code}")
        print(f"Response body GET:{response.text}")

        return response

    def put_login(self, username, body):
        url_put_login_list = f"{self.base_url}/user/{username}"
        response = requests.put(
            url_put_login_list,
            json=body,
            headers=self.headers
        )

        print(f"\n\nExecutando PUT, via url: {url_put_login_list}")
        print(f"Atualização de usuário via serviço PUT. Status code retornado:{response.status_code}")
        print(f"Response body PUT:{response.text}")

        return response

    def delete_login(self, username):
        url_delete_login = f"{self.base_url}/user/{username}"
        response = requests.delete(
            url_delete_login,
            headers=self.headers
        )

        print(f"\n\nExecutando DELETE, via url: {url_delete_login}")
        print(f"Remoção de usuário via serviço DELETE. Status code retornado:{response.status_code}")
        print(f"Response body DELETE:{response.text}")

        return response
