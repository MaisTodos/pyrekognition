# pyrekognition

Helper para manipular o boto, os método do rekognition
<https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html>

## Rodando o projeto local

Primeiramente você deve instanciar o docker com o comando

```bash
make build
```

Após o build, é só rodar os testes

```bash
make test
```

## Testes

Importante salientar que o boto não é mockável, até por segurança da AWS, etc. Para os testes na aplicação vamos mockar todos os resultados (para não escalar em custo também), e o ideal seria fazer o teste meio que na mão e ver resultado da AWS (enviando documentos reais, etc)
