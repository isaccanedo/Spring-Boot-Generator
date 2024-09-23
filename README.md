### Spring Boot Project Generator

Este script Python gera automaticamente a estrutura básica de um projeto Spring Boot com uma API REST simples. É uma alternativa leve e personalizável ao Spring Initializr (https://start.spring.io/).

## Funcionalidades

- Cria a estrutura de diretórios para um projeto Spring Boot
- Gera um arquivo `pom.xml` com dependências básicas
- Cria uma classe principal da aplicação Spring Boot
- Adiciona um controlador REST de exemplo
- Cria um arquivo `application.properties` básico

## Requisitos

- Python 3.x

## Como usar

1. Salve o script como `spring_boot_generator.py`.
2. Execute o script no terminal:
3. Insira o nome do projeto quando solicitado.
4. Insira o nome do pacote quando solicitado.

O script criará um novo diretório com o nome do projeto contendo a estrutura básica do projeto Spring Boot.

## Estrutura do projeto gerado

project_name/
│

├── src/

│ └── main/

│ ├── java/

│ │ └── com/

│ │ └── example/

│ │ └── project_name/

│ │ ├── ProjectNameApplication.java

│ │ └── controller/

│ │ └── HelloController.java

│ │
│ └── resources/

│ └── application.properties

│
└── pom.xml

## Detalhes do script

### Funções principais

1. `create_directory(path)`: Cria um diretório se ele não existir.

2. `create_file(path, content)`: Cria um arquivo com o conteúdo fornecido, garantindo que o diretório pai exista.

3. `create_spring_boot_project(project_name, package_name)`: Função principal que orquestra a criação do projeto.

### Processo de geração

1. Cria a estrutura de diretórios base.
2. Gera o arquivo `pom.xml` com as dependências necessárias.
3. Cria a classe principal da aplicação (`ProjectNameApplication.java`).
4. Adiciona um controlador REST de exemplo (`HelloController.java`).
5. Cria um arquivo `application.properties` básico.

## Personalização

Você pode facilmente personalizar este script para incluir dependências adicionais, configurações específicas ou estruturas de projeto personalizadas. Algumas ideias de extensão:

- Adicionar mais opções de dependências
- Permitir a seleção da versão do Java
- Incluir configurações de banco de dados
- Gerar testes unitários básicos
