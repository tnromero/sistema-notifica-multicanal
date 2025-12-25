# Sistema Notifica Multicanal

Este projeto é um sistema de notificações multicanal.

## Pré-requisitos

- python >= 3.12

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/sistema-notifica-multicanal.git
    cd sistema-notifica-multicanal
    ```
    Se primeira execução, executar:
    ```bash
    [linux]
    python -m venv venv
    source venv/bin/activate

    [windows]
    python -m venv venv
    venv\bin\activate.bat
    ```
    Senão, executar:
    ```bash
    [linux]
    source venv/bin/activate

    [windows]
    venv\bin\activate.bat
    ```

2. Instale as dependências:
    ```bash
    pip install -e .[dev]
    pre-commit install
    ```

## Executando os testes

Para rodar os testes, utilize:

```bash
pytest
```
ou
```bash
python -m pytest
```
