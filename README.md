# Sistema de Consulta de Notas

## Descrição

Sistema web desenvolvido em Flask e MySQL para consulta de notas e faltas de alunos.

O projeto foi containerizado utilizando Docker e Docker Compose, permitindo sua execução de forma simples em qualquer ambiente compatível.

---

## Tecnologias Utilizadas

* Python 3.13
* Flask
* MySQL 8.0
* Docker
* Docker Compose
* HTML5
* CSS3

---

## Funcionalidades

* Login de usuários
* Consulta de notas
* Consulta de faltas
* Integração com banco de dados MySQL
* Execução em containers Docker

---

## Estrutura do Projeto

```text
notas_alunos/
│
├── database/
│   └── notas.sql
│
├── static/
├── templates/
│
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── README.md
└── GUIA_USUARIO.md
```

---

## Como Instalar

### 1. Clonar o repositório

```bash
git clone https://github.com/matheushfsi/notas_alunos.git
cd notas_alunos
```

### 2. Criar o arquivo .env

Windows:

```powershell
copy .env.example .env
```

Linux:

```bash
cp .env.example .env
```

---

## Como Executar

### 1. Abrir o Docker Desktop

Certifique-se de que o Docker Desktop esteja em execução.

Verifique:

```bash
docker --version
docker compose version
```

### 2. Iniciar os containers

```bash
docker compose up -d
```

### 3. Verificar os containers

```bash
docker ps
```

### 4. Acessar o sistema

Abra o navegador:

```text
http://localhost:5000
```

---

## Usuário de Teste

```text
Usuário: matheus
Senha: 123
```

---

## Docker Hub

Imagem publicada:

https://hub.docker.com/r/matheusginc/notas-alunos

---

## AWS EC2

Após a publicação, o sistema pode ser executado em uma instância AWS EC2 utilizando Docker Compose.

A aplicação poderá ser acessada por:

```text
http://IP_PUBLICO:5000
```
