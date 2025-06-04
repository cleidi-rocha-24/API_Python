# language: pt

Funcionalidade: Efetuar automação do login da Petstore

  Cenário: Criar usuários com uma lista
    Dado que eu cadastro usuario
    Quando retornar 200 no response
    Entao o corpo da resposta deve possuir o campo message com o valor "ok"


  Cenário: Obter detalhes de um usuário
    Dado que eu cadastro usuario
    Quando eu faço uma requisição get para obter o usuário
    Então deve retornar código 200 no response body de get


  Cenário: Atualizar dados de um usuário
    Dado que eu cadastro usuario
    Quando eu faço uma requisição put para atualizar os dados do usuário
    Então deve retornar código 200, retornando com sucesso os detalhes do usuário via get


  Cenário: Excluir um usuário
    Dado que eu cadastro usuario
    Quando eu faço uma requisição delete para excluir o usuário
    Então deve retornar código 200, retornando sucesso na exclusão do usuário