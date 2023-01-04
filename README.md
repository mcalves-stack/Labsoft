# API para Administração de salas.

## Endpoints
### GET /games
Esse endpoint é responsável por retornar a listagem de todos os games cadastrados no banco de dados.
#### Paramêtros
Nenhum
#### Respostas
##### OK! 200
Caso essa resposta aconteça você vai receber a listagem de todos os games. Exemplos de resposta:
```
[
    {
        "id": 9,
        "title": "Call of duty MW",
        "year": 2019,
        "price": 10
    },
    {
        "id": 5,
        "title": "Sea of thieves",
        "year": 2018,
        "price": 80
    },
    {
        "id": 1,
        "title": "Need for speed",
        "year": 2020,
        "price": 20
    },
    {
        "id": 2,
        "title": "Minecraft",
        "year": 2017,
        "price": 40
    }
]

```
##### Falha na autenticação! 401
Caso essa resposta aconteça, isso significa que aconteceu alguma falha durante o processo. Motivos: Tokne inválido, Token expirado.

Exemplo de resposta: 
```
{
    "err": "Token Inválido!"
}

```

## Endpoints
### POST /auth
Esse endpoint é responsável por retornar o processo de Ligin de Usúarios.
#### Paramêtros
email: E-mail do usuário cadastrado no sistema.

password: Senha do usuário cadastrado no sistema com aquele determiando e-mail.

Exemplo:
```
{
    "email": "mateusalves@hotmail.com",
    "password": ""
}
```
#### Respostas
##### OK! 200
Caso essa resposta aconteça você vai receber o token JWT para conseguir acessar endpoints protegidos na API. 

Exemplos de resposta:
```
{
    "token": ""
}

```
##### Falha na autenticação! 401
Caso essa resposta aconteça, isso significa que aconteceu alguma falha durante o processo. Motivos: senha ou e-mail incorretos.

Exemplo de resposta: 
```
 {err: "Crendenciais inválidas"}
```

