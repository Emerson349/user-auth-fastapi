# User Auth FastAPI

Projeto de autenticação usando **FastAPI**, **JWT**, **SQLAlchemy** e **SQLite**.  
Fornece rotas para criação de usuários, login, geração e validação de tokens JWT.

## 📚 Sumário
- [Como rodar o projeto](#-como-rodar-o-projeto)
- [Configuração do arquivo .env](#-configure-o-arquivo-env)
- [Estrutura do projeto](#-estrutura-resumida-do-projeto)
- [Funcionalidades](#️-funcionalidades-principais)
- [Requisitos](#-requisitos)
- [Licença](#-licença)

---

## 🚀 Como rodar o projeto

### 1. Clone o repositório
```bash
git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
cd NOME_DO_REPOSITORIO
````

## 2. Crie e ative o ambiente virtual
```bash
python -m venv venv
venv\Scripts\activate
````
## 3. Instale as dependências
Crie um arquivo .env na raiz do projeto com:
```bash
pip install -r requirements.txt
```
## 🔐 Configure o arquivo .env
```init
SECRET_KEY="SUA_SENHA_FORTE_AQUI"
ACCESS_TOKEN_EXPIRE_MINUTES=60
ALGORITHM="HS256"
```
## 🔒 SECRET_KEY
* Gere uma senha forte em: https://passwordsgenerator.net/
* Recomenda-se 32 caracteres ou mais.

## 🕒 ACCESS_TOKEN_EXPIRE_MINUTES
* O projeto utiliza o algoritmo HS256 e deve permanecer assim.

## 🔐 ALGORITH
O projeto utiliza o algoritmo HS256 e deve permanecer assim

## ▶️ Execute o servidor
```bash
uvicorn src.app.main:app --reload
```
Acesse:
* API: http://127.0.0.1:8000

## 📁 Estrutura resumida do projeto
```bash
project/
│
├── src/
│   ├── app/
│   │   ├── main.py
│   │   ├── db/
│   │   │   ├── database.py
│   │   │   ├── dependencies.py
│   │   ├── models/
│   │   ├── routes/
│   │   ├── schemas/
│   │
│   ├── ...
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

📌 Sobre cada diretório

app/main.py — Inicia a aplicação e carrega as rotas.
db/ — Configuração do banco e dependências.
models/ — Modelos SQLAlchemy.
routes/ — Endpoints da API.
schemas/ — Schemas Pydantic usados para validação.

✔️ Funcionalidades principais

Criar usuários
Login com validação
Geração de token JWT
Verificação de token para rotas protegidas
CRUD de exemplo

📌 Requisitos

Python 3.11+
FastAPI
Uvicorn
SQLAlchemy
python-dotenv
python-jose
