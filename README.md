# Calculadora Científica em Python com PyQt6

Uma calculadora científica desenvolvida com Python e PyQt6, com interface gráfica, organização em múltiplos arquivos e foco em boas práticas de programação.

Este projeto foi criado como estudo prático de desenvolvimento desktop com Python, trabalhando conceitos como:

- Interface gráfica com PyQt6
- Separação de responsabilidades
- Organização de projeto em módulos
- Lógica matemática isolada da interface
- Código limpo e fácil de manter

> Todo o código foi escrito à mão, linha por linha, como forma de aprendizado e prática real de programação.

---

## Preview

A aplicação possui uma interface simples e funcional, com botões para operações comuns e funções científicas.

Funções disponíveis:

- Soma
- Subtração
- Multiplicação
- Divisão
- Potência
- Raiz quadrada
- Porcentagem
- Fatorial
- Seno
- Cosseno
- Tangente
- Logaritmo
- Logaritmo natural
- Constantes pi e e
- Último resultado com Ans

---

## Tecnologias utilizadas

- Python
- PyQt6
- Módulo math

---

## Estrutura do projeto

bash calculadora_cientifica/ ├── main.py ├── requirements.txt └── app/     ├── __init__.py     ├── calculator.py     ├── styles.py     └── ui.py 

---

## Organização do código

O projeto foi separado em arquivos para facilitar manutenção e evolução.

### main.py

Arquivo principal da aplicação.  
Responsável por iniciar o programa e abrir a janela da calculadora.

### app/ui.py

Responsável pela interface gráfica.  
Aqui ficam a janela, o display, os botões e os eventos de clique.

### app/calculator.py

Responsável pela lógica matemática.  
Esse arquivo calcula as expressões e mantém o último resultado.

### app/styles.py

Responsável pelos estilos visuais da aplicação.  
Aqui ficam as cores, tamanhos e aparência dos botões e do display.

---

## Como instalar e rodar

### 1. Clone o repositório

bash git clone https://github.com/seu-usuario/seu-repositorio.git 

### 2. Entre na pasta do projeto

bash cd calculadora_cientifica 

### 3. Crie um ambiente virtual

bash python -m venv venv 

### 4. Ative o ambiente virtual

No Windows:

bash venv\Scripts\activate 

No macOS ou Linux:

bash source venv/bin/activate 

### 5. Instale as dependências

bash pip install -r requirements.txt 

### 6. Execute o projeto

bash python main.py 

---

## Exemplos de uso

text sin(90) = 1 cos(0) = 1 sqrt(25) = 5 log(100) = 2 ln(e) = 1 2**3 = 8 5**2 = 25 

As funções trigonométricas foram configuradas para trabalhar em graus, como em uma calculadora comum.

---

## Sobre o desenvolvimento

Esse projeto foi feito com o objetivo de praticar programação de verdade, escrevendo cada parte do código manualmente.

A ideia não foi apenas criar uma calculadora, mas também aprender como estruturar melhor um projeto Python, separando:

- Regra de negócio
- Interface gráfica
- Estilos
- Arquivo principal de execução

Esse tipo de organização deixa o código mais profissional e mais fácil de expandir no futuro.

---

## Possíveis melhorias futuras

Algumas ideias para evoluir o projeto:

- Adicionar histórico de cálculos
- Criar tema escuro
- Adicionar suporte ao teclado físico
- Melhorar o tratamento de erros
- Criar instalador para Windows
- Gerar executável com PyInstaller
- Adicionar testes automatizados
- Criar uma versão com layout responsivo

---

## Aprendizados

Durante o desenvolvimento deste projeto, foram praticados conceitos importantes como:

- Criação de interfaces desktop
- Manipulação de eventos
- Uso de classes
- Organização em pacotes
- Separação de responsabilidades
- Uso controlado de expressões matemáticas
- Estilização com Qt Style Sheets

---

## Autor

Desenvolvido por Deivid Moretto.

Projeto criado como parte da minha evolução como desenvolvedor, praticando Python, interface gráfica e boas práticas de organização de código.

---

## Considerações

Obrigado por visitar este repositório.

Este projeto representa prática, estudo e evolução constante na programação.

Cada linha foi escrita com o objetivo de aprender mais e melhorar como desenvolvedor.