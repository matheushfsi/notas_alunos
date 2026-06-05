# Notas Alunos

## Descrição

Sistema web para consulta de notas e faltas escolares desenvolvido com Flask e MySQL.

## Tecnologias Utilizadas

* Python
* Flask
* MySQL
* HTML5
* CSS3
* Docker
* Docker Compose

## Funcionalidades

* Login de usuários
* Consulta de notas
* Consulta de faltas
* Encerramento de sessão (logout)

## Estrutura do Projeto

```txt
notas_alunos/
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
│
├── static/
│   ├── style.css
│   ├── login.js
│   └── imagens/
│
└── templates/
    ├── index.html
    ├── login.html
    ├── aluno.html
    └── contato.html
```

## Instalação

```bash
git clone https://github.com/matheushfsi/notas_alunos.git
cd notas_alunos
```

## Configuração

Crie o arquivo .env:

```env
DB_HOST=mysql
DB_USER=root
DB_PASSWORD=root
DB_NAME=notas
```

## Executando com Docker

```bash
docker compose up -d
```

## Acessando

Abra o navegador:

```txt
http://localhost:5000
```
