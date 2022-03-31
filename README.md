# CELERO BACK END TEST

### SPECIFICAÇÕES

- Python 3.7.2
- Django 3.2.12

### SETUP INICIAL E RODANDO LOCALMENTE

1. Clonar esse repo
2. Instalar Python 3.7.2 (o Python 3.6 ou 3.7 devem funcionar)
3. Criar um ambiente virtual
4. Ativar o ambiente virtual
5. Instalar as dependencias listadas no requirements.txt
6. Rodar o comando `python manage.py runserver` para iniciar o servidor local celerochallenge
7. Pode ser acessado direto no browser com o endereço localhost:8000/celero/

### ORGANIZAÇÃO DO REPO

- Uma pasta do projeto (celerobackend)
- Uma pasta para o app (celerochallenge)

### PREPARAÇÃO DA BASE DE DADOS LOCAL 

Utilizando o comando `python manage.py populate_data` será possivel popular a base de dados local, mas o arquivo .csv deverá estar na raiz do
projeto, com o mesmo nome e header.

###### COMO RODAR TESTES AUTOMATIZADOS

Para rodar os testes deverá ser utilizado o script `python manage.py test celerochallenge.tests.test_views` para os testes relacionados a views
e para os testes relacionados ao serializer `python manage.py test celerochallenge.tests.test_serializer`
