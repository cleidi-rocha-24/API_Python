from behave import *

from Desafio_3_Login_PetStore.features.impl.login_petstore import LoginPetstore


@given(u'que eu cadastro usuario')
def step_impl(context):
    context.login_um = LoginPetstore()
    context.login_dois = LoginPetstore()

    context.login_um.id = 11
    context.login_um.username = "http"
    context.login_um.firstName = "NaoSei"
    context.login_um.lastName = "da Silva"
    context.login_um.email = "naosei@tst.com.br"
    context.login_um.password = "98765"
    context.login_um.phone = "88888888"
    context.login_um.userStatus = 0

    context.login_dois.id = 21
    context.login_dois.username = "www"
    context.login_dois.firstName = "Teste"
    context.login_dois.lastName = "Rocha"
    context.login_dois.email = "teste@tst.com.br"
    context.login_dois.password = "12345"
    context.login_dois.phone = "5199999999"
    context.login_dois.userStatus = 0

    context.usuario1 = {"id": context.login_um.id, "username": context.login_um.username,
                        "firstName": context.login_um.firstName, "lastName": context.login_um.lastName,
                        "email": context.login_um.email, "password": context.login_um.password,
                        "phone": context.login_um.phone, "userStatus": context.login_um.userStatus}

    context.usuario2 = {"id": context.login_dois.id, "username": context.login_dois.username,
                        "firstName": context.login_dois.firstName, "lastName": context.login_dois.lastName,
                        "email": context.login_dois.email, "password": context.login_dois.password,
                        "phone": context.login_dois.phone, "userStatus": context.login_dois.userStatus}

    context.body = [context.usuario1, context.usuario2]
    context.login = LoginPetstore()
    context.response_body = context.login.post_login(context.body)


@when(u'eu faço uma requisição get para obter o usuário')
def step_impl(context):
    context.response_body_get = context.login.get_login(context.body[0]['username'])


@when(u'eu faço uma requisição put para atualizar os dados do usuário')
def step_impl(context):
    context.login.id = 21
    context.login.username = "www"
    context.login.firstName = "Teste"
    context.login.lastName = "Rocha"
    context.login.email = "teste@tst.com.br"
    context.login.password = "12345"
    context.login.phone = "5199999999"
    context.login.userStatus = 0


    context.body_atualizacao = {"id": context.login_um.id, "username": context.login_um.username,
                        "firstName": context.login_um.firstName, "lastName": context.login_um.lastName,
                        "email": context.login_um.email, "password": context.login_um.password,
                        "phone": context.login_um.phone, "userStatus": context.login_um.userStatus
    }

    context.response_body_atualizacao = context.login.put_login(context.body[0]['username'],
                                                                context.body_atualizacao)


# post:
@when(u'retornar 200 no response')
def step_impl(context):
    assert context.login.status_code == 200
    print(f"Usuário criado com sucesso. Via servico POST")
    assert context.response_body["code"] == 200


@then(u'o corpo da resposta deve possuir o campo message com o valor "ok"')
def step_impl(context):
    assert context.response_body["type"] == "unknown"
    assert context.response_body["message"] == "ok"


# get
@then(u'deve retornar código 200 no response body de get')
def step_impl(context):
    assert context.response_body_get.status_code == 200, 'Falha ao buscar usuário'
    json = context.response_body_get.json()

    assert json["id"] == context.body[0]["id"]
    assert json["username"] == context.body[0]["username"]
    assert json["firstName"] == context.body[0]["firstName"]
    assert json["lastName"] == context.body[0]["lastName"]
    assert json["email"] == context.body[0]["email"]
    assert json["password"] == context.body[0]["password"]
    assert json["phone"] == context.body[0]["phone"]


# put
@then(u'deve retornar código 200, retornando com sucesso os detalhes do usuário via get')
def step_impl(context):
    assert context.response_body_atualizacao.status_code == 200, 'Falha ao atualizar usuário'
    response_get = context.login.get_login(context.body_atualizacao['username'])
    assert response_get.status_code == 200, 'Falha ao buscar usuário'

    json = response_get.json()

    assert json["id"] == context.body_atualizacao["id"]
    assert json["username"] == context.body_atualizacao["username"]
    assert json["firstName"] == context.body_atualizacao["firstName"]
    assert json["lastName"] == context.body_atualizacao["lastName"]
    assert json["email"] == context.body_atualizacao["email"]
    assert json["password"] == context.body_atualizacao["password"]
    assert json["phone"] == context.body_atualizacao["phone"]


# delete
@when(u'eu faço uma requisição delete para excluir o usuário')
def step_impl(context):
    context.response_body_delete = context.login.delete_login(context.body[1]['username'])


@then(u'deve retornar código 200, retornando sucesso na exclusão do usuário')
def step_impl(context):
    assert context.response_body_delete.status_code == 200
    print("Usuário deletado com sucesso")
    response_body_get = context.login.get_login(context.body[1]['username'])
    json = response_body_get.json()
    assert response_body_get.status_code == 404
    assert json["code"] == 1
    assert json["type"] == "error"
    assert json["message"] == "User not found"
