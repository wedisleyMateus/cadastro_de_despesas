# Projeto Cadastro de Despesas

## Visão Geral
O Projeto Cadastro de Despesas é um serviço que possibilita a gestão de despesas diárias ou semanais, dependendo da preferência do usuário. Ele foi desenvolvido utilizando Django e uma API Restful, com foco em um código simples e completo, aproveitando ao máximo os recursos da ferramentas utilizadas.

## Instruções de Instalação

Para configura o ambiente de desenvolvimento, siga os passos a baixo.

1- Clone o repositório do GitHub:

    git clone https://github.com/wedisleyMateus/cadastro_de_despesas.git

2- Acesse o diretorio do projeto:

    cd .../.../cadastro_de_despesas

3- Crie um ambiente virtual:

    python3 -m venv venv
    source venv/bin/activate #Ativa o ambiente virtual

4- Instalação de dependencias do projeto:

    pip install Django #instala o Django no projeto

    pip install djangorestframework #instala o framework Rest pra uso de API

    pip install drf-yasg #instala as dependencias para o uso de documentação em Swagger

## Uso do sistema:

Para inicializar o projeto deve-se rodar:

    python manage.py runserver

Após iniciar o servidor, você pode acessar a API em http://127.0.0.1:8000/api/expenses/ . Depois já é possive fazer requisições para API utilizando ou o Navegador ou um Postman conforme for nescessário.

## Documentação a API

A documentação da API ta disponivel via Swagger, para acessala siga os passos abaixo.

1- Inicie o projeto:

    python manage.py runserver

2- Abra o navegador e acesse o caminho http://127.0.0.1:8000/swagger/ para visualizar a documentação Swagger.


## Estrutura do projeto

O Foco principal do projeto se localiza em <b>App</b> que é uma aplicação totalmente desenvolvida em <b>DJango</b>, dentro dele segue alguns arquivos nescessarios:

1- <b>model:</b> Modelagem ou Campos de dados necessário.

2- <b>views:</b> Regra de negocio e Funcionamento da aplicação.

3- <b>serializer:</b> Serialização e Deserialização dos Objetos para o uso em minha API.

4- <b>urls:</b> Controle de rotas a serem usadas na WEB ou Ferramentas de Testes.

5- <b>migrations:</b> Diretorio que contém as migrações pro meu banco de dados.

## Contribuição

Se deseja contribuir com o projeto, siga esses passos:

1- Faça um <b>Fork</b> do repositorio e clone-o na sua máquina local.

2- Crie uma breach para suas alteraçoes ou correções.

3- Seguir o padão do código do projeto.

4- Depois de efetuar alterações ou correções suba para o seu <b>Fork</b>.

5- Envie usando <b>pull request</b> para o repositorio original.