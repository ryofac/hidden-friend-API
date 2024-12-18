# 🎉 Amigo Oculto API

## 📝 Descrição do Projeto
Uma API para realização do conhecido evento "amigo oculto", aplicando conceitos de arquitetura limpa utilizando Python.

Este projeto tem como objetivo facilitar a organização de eventos de amigo oculto, oferecendo funcionalidades para cadastrar participantes, realizar sorteios e gerenciar as configurações do evento. Tudo isso foi desenvolvido com foco em uma arquitetura limpa, modular e de fácil manutenção.

## 🛠️ Tecnologias Utilizadas

As principais tecnologias utilizadas neste projeto são:

- **[Litestar](https://litestar.dev/)**: Um framework web leve e flexível para construção de APIs rápidas e escaláveis.
- **[SQLAlchemy](https://www.sqlalchemy.org/)**: Um ORM (Object-Relational Mapper) do tipo data mapper, utilizado para gerenciar a interação com o banco de dados.

## 🚀 Funcionalidades
- Cadastro de participantes.
- Realização automática do sorteio para o amigo oculto.
- Visualização dos pares sorteados.
- Configuração de regras opcionais para o sorteio (como evitar pares específicos).

## 📂 Estrutura do Projeto
Este projeto foi construído com base nos princípios da arquitetura limpa, com camadas bem definidas para facilitar a compreensão e manutenção do código. A estrutura de diretórios é a seguinte:

```
.
├── src
│   ├── domain       # Camada de Domínio: Regras de negócio e entidades centrais
│   ├── application  # Camada de Aplicação: Casos de uso e orquestração
│   ├── infrastructure # Camada de Infraestrutura: Persistência e detalhes técnicos
│   └── interface    # Camada de Interface: Endpoints da API (Litestar)
├── docs             # Documentação do projeto
└── tests            # Testes automatizados
```
