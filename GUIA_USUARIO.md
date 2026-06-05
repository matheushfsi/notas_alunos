# Guia do Usuário

## Pré-requisitos

Antes de executar o sistema, instale:

* Git
* Docker Desktop

Verifique a instalação:

```bash
git --version
docker --version
docker compose version
```

---

## Baixando o Projeto

```bash
git clone https://github.com/matheushfsi/notas_alunos.git
cd notas_alunos
```

---

## Configurando o Arquivo .env

Windows:

```powershell
copy .env.example .env
```

Linux:

```bash
cp .env.example .env
```

---

## Iniciando o Sistema

Certifique-se de que o Docker Desktop esteja aberto.

Execute:

```bash
docker compose up -d
```

---

## Verificando os Containers

```bash
docker ps
```

Os containers esperados são:

```text
notas_alunos
mysql_notas
```

---

## Acessando o Sistema

Abra o navegador:

```text
http://localhost:5000
```

Utilize:

```text
Usuário: matheus
Senha: 123
```

---

## Encerrando o Sistema

Para parar os containers:

```bash
docker compose down
```

Para remover também o banco de dados:

```bash
docker compose down -v
```

---

## Solução de Problemas

### Erro: ".env not found"

Crie o arquivo:

```bash
cp .env.example .env
```

ou

```powershell
copy .env.example .env
```

### Erro relacionado ao Docker

Verifique se o Docker Desktop está aberto e totalmente inicializado.

Teste:

```bash
docker ps
```

Se o comando funcionar, o Docker está pronto para uso.
