# Projeto de Teoria da Computação - GCC108

Este projeto prático foi desenvolvido como parte da disciplina de Teoria da Computação, ministrada pelo professor [Rafael Serapilha Durelli](https://campusvirtual.ufla.br/presencial/user/view.php?id=22355&course=50378) na [Universidade Federal de Lavras (UFLA)](https://ufla.br).

O objetivo do trabalho consistiu na implementação de Máquinas de Turing por meio de uma REST API, utilizando a framework FastAPI, e posteriormente na dockerização da aplicação com o Docker.

Documentação utilizada para o desenvolvimento das Máquinas de Turing: [automata](https://github.com/caleb531/automata)

### Membros do Grupo:

- [Diogo Carrer de Macedo](https://campusvirtual.ufla.br/presencial/user/view.php?id=42061&course=50378)
- [João Victor Carvalho dos Santos](https://campusvirtual.ufla.br/presencial/user/view.php?id=42033&course=50378)

### Docker Image

```cmd

# Versão em inglês do retorno da API
docker container run -p 8000:8000 jaocarvalho/fastapi-teoria-da-computacao:v0

# Versão em português do retorno da API
docker container run -p 8000:8000 jaocarvalho/fastapi-teoria-da-computacao:v1
````


## Pré-requisitos

Antes de começar, certifique-se de ter instalado as seguintes ferramentas:

- [Visual Studio Code (VSCode)](https://code.visualstudio.com/) ou [PyCharm](https://www.jetbrains.com/pycharm/)
- [Python](https://www.python.org/) (python:3.9)

## Instalação

Siga os passos abaixo para configurar seu ambiente de desenvolvimento:

### Passo 0: Escolha sua IDE

Escolha entre Visual Studio Code (VSCode) ou PyCharm para desenvolver seu projeto.

### Passo 1: Instale o Python

Certifique-se de ter o Python instalado. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).

### Passo 2: Instale o FastAPI

Você precisa instalar o FastAPI. Para fazer isso, execute os seguintes comandos no terminal:

```bash
pip install fastapi
pip install "uvicorn[standard]"

### Passo 3: Crie o arquivo main.py

Crie um arquivo chamado `main.py` e adicione o seguinte código:

```python
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

### Passo 4: Execute o servidor FastAPI

Para iniciar o servidor FastAPI, execute o seguinte comando no terminal:

```bash
uvicorn main:app --reload

### Passo 5: Acesse o aplicativo no navegador

Abra seu navegador e acesse [http://127.0.0.1:8000/items/5?q=somequery](http://127.0.0.1:8000/items/5?q=somequery). Você verá a seguinte resposta JSON:

```json
{"item_id": 5, "q": "somequery"}


### Passo 6: Instale a biblioteca Automata

Para instalar a biblioteca Automata, execute o seguinte comando no terminal:

```bash
pip install automata-lib


### Passo 7: Copie o arquivo main.py

Agora, copie o arquivo `main.py` do repositório para o seu projeto. O arquivo `main.py` contém o código FastAPI necessário para configurar seu aplicativo. Certifique-se de que o arquivo esteja em seu diretório de projeto.


### Passo 8: Teste seu projeto

Você pode testar seu projeto usando ferramentas como o [Postman](https://www.postman.com/) ou o [Insomnia](https://insomnia.rest/), enviando uma solicitação HTTP com o JSON fornecido no repositório.

Certifique-se de que o servidor FastAPI esteja em execução usando o comando `uvicorn main:app --reload` e que o arquivo `main.py` e as dependências estejam configuradas corretamente antes de realizar os testes.

Isso permitirá que você verifique se seu projeto está funcionando conforme o esperado e que as rotas estão respondendo corretamente.

