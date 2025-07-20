# Todo List API

Essa é uma API para gerenciar tarefas. Ela foi desenvolvida com Django e utiliza o padrão de arquitetura REST.

## Arquitetura

A arquitetura da aplicação é dividida em 4 camadas:

- **Controller**: responsável por receber as requisições e enviá-las para a camada de serviço.
- **Service**: responsável por realizar as operações de negócios, como CRUD de tarefas, projetos e categorias.
- **Repository**: responsável por realizar as operações de acesso a dados, como SELECT, INSERT, UPDATE e DELETE.
- **Infra**: responsável por fornecer as dependências necessárias para a aplicação, como o banco de dados e o framework web.

## Como rodar

Para rodar a aplicação, você precisará ter o Python 3.12 e o Django instalados em sua máquina.



1. Clone o repositório e navegue até a pasta do projeto.
2. Crie um arquivo `.env` com a variável de ambiente SECRET_KEY.

# 🐍 Projeto Django - Instruções de Instalação

Este documento descreve como configurar e executar o projeto localmente utilizando `virtualenv`, `requirements.txt` e os comandos do Django para migração e execução do servidor.

---

## 📦 Ambiente Virtual

Antes de iniciar, certifique-se de ter o **Python 3.12** e o **pip** instalados na sua máquina.

### 1. Instale o virtualenv (caso não tenha)

```bash
pip install virtualenv
```

### 2. Crie o ambiente virtual

```bash
python -m venv venv
```

### 3. Ative o ambiente virtual

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

---

## 📄 Instalação das Dependências

Com o ambiente virtual ativado, instale as bibliotecas do projeto:

```bash
pip install -r requirements.txt
```

---

## 🔧 Migrações do Banco de Dados

Execute os seguintes comandos para criar e aplicar as migrações:

```bash
python manage.py makemigrations api
python manage.py migrate
```

---

## 🚀 Rodando o Servidor de Desenvolvimento

Inicie o servidor local com o comando abaixo:

```bash
python manage.py runserver
```

## 🚀 Ou se preferir pode rodar com o docker

```bash
docker compose up --build
```

Acesse no navegador:

```
http://localhost:8000
```

---

## ✅ Pronto!

Agora você pode testar o projeto localmente.


## Rondando testes

para rodar os testes do projeto utilize:

```bash
python -m pytest --verbose
```
ou apenas

```bash
pytest --verbose
```


