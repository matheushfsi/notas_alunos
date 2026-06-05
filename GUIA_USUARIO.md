# Guia do Usuário

## Pré-requisitos

* Docker Desktop
* Git

## Baixando o Projeto

```bash
git clone https://github.com/matheushfsi/notas_alunos.git
```

## Entrando na Pasta

```bash
cd notas_alunos
```

## Configurando o Ambiente

Copie:

```bash
cp .env.example .env
```

Preencha os dados do banco.

## Iniciando o Sistema

```bash
docker compose up -d
```

## Verificando os Containers

```bash
docker ps
```

## Acessando o Sistema

Abra:

```txt
http://localhost:5000
```

## Encerrando o Sistema

```bash
docker compose down
```
