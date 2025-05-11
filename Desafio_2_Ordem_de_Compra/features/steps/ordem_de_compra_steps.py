from behave import *
import requests

from Desafio_2_Ordem_de_Compra.features.impl.ordem_de_compra import OrdemDeCompra


@given(u'que o usuário selecionou o animal desejado na petstore')
def step_impl(context):
    context.api = OrdemDeCompra()
    context.api.id = 10
    context.api.petId = 3
    context.api.quantidade = 2
    context.api.post_criar_uma_nova_ordem()

    assert context.api.status_code == 200
    print(f"Ordem de compra criado com sucesso. Via servico POST")


@then(u'o sistema valida se a ordem de pedido foi armazenada corretamente')
def step_impl(context):
    response = context.api.get_busca_order_id()
    assert response["id"] == context.api.id
    assert response["petId"] == context.api.petId
    assert response["quantity"] == context.api.quantidade
    assert response["status"] == "placed"
    assert response["complete"] is True

    assert context.api.status_code == 200
    print(f"Ordem de compra buscada com sucesso. Via servico GET")