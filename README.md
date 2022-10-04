# Eventext

Sistema de Eventos encomendado pela Morena.

## Como desenvolver ?
1. Clone o repositório.
2. Crie um virtualenv com Python
3. Ative o virtualenv.
4. Configure a instância com .env
5. Execute os testes.

```console
git clone https://github.com/molimpio/eventex wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer deploy ?
1. Crie uma instância no heroku.
2. Envie as configurações para o heroku.
3. Defina uma SECRET_KEY segura para instância.
4. Defina DEBUG=False
5. Configure o serviço de email.
6. Envie o código para heroku.

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configurar o email
git push heroku master
```