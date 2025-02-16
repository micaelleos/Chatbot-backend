### Visão Geral

Este repositório contém a implementação do **backend** de um **chatbot genérico** utilizando o framework **LangChain** para gerenciamento de conversas, **FastAPI** para criação de APIs rápidas e escaláveis, e **Docker** para containerização do projeto. O chatbot foi configurado para ser executado como **funções Lambda da AWS**, com integração ao **DynamoDB** para persistência de dados e histórico de interações.

### Tecnologias Utilizadas

- **LangChain**: Framework para construir agentes conversacionais baseados em modelos de linguagem.
- **FastAPI**: Framework rápido e eficiente para criação de APIs RESTful.
- **Docker**: Containerização do backend para fácil deploy e execução.
- **AWS Lambda**: Execução serverless para escalar funções sem a necessidade de gerenciar servidores.
- **DynamoDB**: Banco de dados NoSQL da AWS para armazenamento de dados e histórico do chatbot.

### Funcionalidades

- **Integração com AWS Lambda**: O chatbot roda em funções Lambda, permitindo escalabilidade e baixo custo operacional.
- **Armazenamento em DynamoDB**: Armazena e recupera dados de interação do chatbot, podendo ser facilmente expandido para armazenar históricos, preferências de usuários, entre outros.
- **Modelo Genérico de Chatbot**: O chatbot pode ser personalizado para diversos casos de uso, incluindo atendimento ao cliente, assistentes pessoais e mais.

### Estrutura do Repositório

- **app/**: Contém o código principal do backend, incluindo a implementação do FastAPI e integração com LangChain.
- **Dockerfile**: Arquivo de configuração para construir a imagem Docker do projeto.
- **requirements.txt**: Dependências necessárias para rodar o projeto localmente.
- **serverless.yml**: Configurações para deploy das funções Lambda e integração com AWS.
- **.env**: Arquivo de variáveis de ambiente (não incluído no repositório por questões de segurança).

### Como Rodar o Projeto

#### 1. **Clonando o Repositório**

Clone o repositório para a sua máquina local:

```bash
git clone https://github.com/micaelleos/chatbot.git
cd chatbot
```

#### 2. **Instalando Dependências**

Instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

#### 3. **Rodando Localmente com Docker**

O projeto está configurado para ser executado dentro de um container Docker. Para rodar o backend localmente, use os seguintes comandos:

```bash
docker build -t chatbot .
docker run -p 8000:8000 chatbot
```

A API do FastAPI estará disponível em `http://localhost:8000`.

#### 4. **Deploy no AWS Lambda**

Para rodar no AWS Lambda, utilize o **Serverless Framework** para deploy. Siga os passos abaixo:

- Configure suas credenciais AWS (`AWS_ACCESS_KEY_ID` e `AWS_SECRET_ACCESS_KEY`).
- Instale o **Serverless Framework** globalmente:

  ```bash
  npm install -g serverless
  ```

- Faça o deploy utilizando o comando:

  ```bash
  serverless deploy
  ```

Isso vai fazer o deploy do backend para as funções Lambda da AWS.

### Como Funciona

1. **Interação do Chatbot**: O chatbot recebe as perguntas dos usuários via API FastAPI, que é gerida pelas funções Lambda.
2. **Processamento com LangChain**: O LangChain é utilizado para gerenciar a lógica de conversação, interagindo com o modelo de linguagem e permitindo uma resposta adequada baseada no contexto.
3. **Armazenamento em DynamoDB**: O histórico de conversas ou dados adicionais podem ser armazenados no DynamoDB para consultas futuras.

### Contribuindo

Se você deseja contribuir para este projeto, siga os seguintes passos:

1. Faça um fork deste repositório.
2. Crie uma nova branch (`git checkout -b minha-nova-feature`).
3. Faça suas alterações.
4. Envie um pull request com uma descrição detalhada das mudanças.

### Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

### Contato

Se você tiver dúvidas ou sugestões, sinta-se à vontade para abrir uma *issue* ou me contatar diretamente através do e-mail [micaelle.osouza@gmail.com].

---

### Descrição Curta para o GitHub:

**Backend de Chatbot Genérico com LangChain e AWS Lambda**: Este repositório contém o backend de um chatbot genérico utilizando **LangChain**, **FastAPI** e **AWS Lambda**. O projeto usa **Docker** para containerização e **DynamoDB** para armazenamento de dados e histórico de conversas. É uma base escalável e de fácil deploy para criar chatbots personalizados e serverless.

---

Esse **README** fornece uma explicação clara do projeto, destacando as principais tecnologias utilizadas, funcionalidades e como rodar o projeto localmente ou na AWS. Se precisar de mais ajustes ou detalhes, só avisar!
