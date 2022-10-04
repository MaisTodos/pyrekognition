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

## Como utilizar

Primeiramente você precisa fazer o seu setup das variáveis de ambiente, com acesso ao aws-rekognition

```python
REKOGNITION_AWS_ACCESS_KEY_ID = <a_very_long_key>
REKOGNITION_AWS_SECRET_ACCESS_KEY =<a_very_long_access>
```

Após isso, é apenas chamar o client com sua imagem

```python
validator = KYCValidate()

# Se tiver a imagem em url
url_origin = "url_da_imagem.png"
image = validator.convert_url_to_image(url_origin)

# Para extrair os textos da imagem
data = validator.extract_image_data(image)
# data = [lista com os textos]

# para validar se é uma CNH
is_driver_license = validator.validate_driver_license(image)
# is_driver_license True/False

# para validar se é uma carteira de identidade
is_id_card = validator.validate_id_cards(image)
# is_id_card True/False

# para comparar rostos das imagens
image_to_compare = "bytes image"
is_same_person = validade_faces(image, image_to_compare)
# is_same_person True/False
```
