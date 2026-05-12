# BookingHub

Plataforma backend de reservas e gestão de viagens desenvolvida com foco em arquitetura backend moderna, automação de ambiente e persistência de dados.

![BookingHub Architecture](docs/image.png)
---

## Arquitetura

O projeto segue uma arquitetura modular orientada a separação de responsabilidades, priorizando organização, escalabilidade e manutenção.



## Tecnologias

- Python
- FastAPI
- PostgreSQL
- Docker
- Docker Compose
- SQL

---

## Funcionalidades

- API REST
- Migrations automatizadas
- Seed automatizado
- Healthcheck entre containers
- Views SQL analíticas
- Persistência de dados
- Logs estruturados
- Documentação Swagger/OpenAPI

---

## Executando o projeto

### Subir ambiente

```bash
docker compose up --build
```

---

## Documentação da API

Swagger disponível em:

```text
http://localhost:8000/docs
```

---

## Banco de Dados

### Conexão PostgreSQL

| Configuração | Valor |
|---|---|
| Host | localhost |
| Port | 5433 |
| Database | bookinghub |
| User | booking |
| Password | secret |

---

## Estrutura do ambiente

O ambiente sobe automaticamente com:

- PostgreSQL
- Execução de migrations
- Seed de dados
- API FastAPI
- Healthchecks

---

## Objetivo

O projeto foi desenvolvido para simular um ambiente backend próximo de produção, explorando:

- Engenharia de software
- Automação de infraestrutura local
- Persistência relacional
- Observabilidade
- Escalabilidade
- Integração futura com Machine Learning
