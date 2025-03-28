# **Chatbot-Backend**
---

### **Overview**  

This repository contains the implementation of a **generic chatbot backend** using the **LangChain** framework for conversation management, **FastAPI** for building fast and scalable APIs, and **Docker** for project containerization. The chatbot is configured to run as **AWS Lambda functions**, with integration into **DynamoDB** for data persistence and interaction history storage.  

---

### **Technologies Used**  

- **LangChain**: A framework for building conversational agents based on language models.  
- **FastAPI**: A fast and efficient framework for creating RESTful APIs.  
- **Docker**: Containerization of the backend for easy deployment and execution.  
- **AWS Lambda**: Serverless execution to scale functions without managing servers.  
- **DynamoDB**: AWS NoSQL database for storing chatbot data and history.  

---

### **Features**  

- **AWS Lambda Integration**: The chatbot runs as Lambda functions, ensuring scalability and low operational costs.  
- **DynamoDB Storage**: Stores and retrieves chatbot interaction data, with easy expansion for storing histories, user preferences, and more.  
- **Generic Chatbot Model**: The chatbot can be customized for various use cases, including customer support, personal assistants, and more.  

---

### **Repository Structure**  

- **scripts/**: Contains the main backend code, including the FastAPI implementation and LangChain integration.  
- **Dockerfile**: Configuration file to build the project's Docker image.  
- **requirements.txt**: List of dependencies required to run the project locally.  
- **Makefile**: Deployment configurations for Lambda functions and AWS integration.  
- **.env**: Environment variables file (not included in the repository for security reasons).  

---

### **How to Run the Project**  

#### 1. **Clone the Repository**  

Clone the repository to your local machine:  

```bash
git clone https://github.com/micaelleos/chatbot.git
cd chatbot
```  

#### 2. **Install Dependencies**  

Install the required dependencies:  

```bash
pip install -r requirements.txt
```  

#### 3. **Run Locally with Docker**  

The project is configured to run inside a Docker container. To start the backend locally, use the following commands:  

```bash
docker build -t chatbot .
docker run -p 8000:8000 chatbot
```  
or run:  

```bash
uvicorn api:app --reload
```  

The FastAPI API will be available at `http://localhost:8000`.  

#### 4. **Deploy on AWS Lambda**  

To deploy on AWS Lambda, use the **Serverless Framework** by following these steps:  

- Configure your AWS credentials (`AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`).  
- Install the **Serverless Framework** globally:  

  ```bash
  npm install -g serverless
  ```  

- Deploy using the command:  

  ```bash
  serverless deploy
  ```  

This will deploy the backend to AWS Lambda functions.  

---

### **How It Works**  

1. **Chatbot Interaction**: The chatbot receives user queries via the FastAPI-based API, which is managed by Lambda functions.  
2. **Processing with LangChain**: LangChain is used to handle conversation logic, interacting with the language model to provide context-based responses.  
3. **Storage in DynamoDB**: Conversation history and additional data can be stored in DynamoDB for future queries.  

---

### **Contributing**  

If you want to contribute to this project, follow these steps:  

1. Fork this repository.  
2. Create a new branch (`git checkout -b my-new-feature`).  
3. Make your changes.  
4. Submit a pull request with a detailed description of the modifications.  

---

### **License**  

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.  

---

### **Contact**  

If you have any questions or suggestions, feel free to open an *issue* or contact me directly via email: [micaelle.osouza@gmail.com].  
