Aqui está uma versão em **português mais profissional**, escrita com foco em portfólio e para chamar atenção de recrutadores.

---

# PyBrasil Terminal

## Visão geral

O PyBrasil Terminal é um simulador de terminal desenvolvido em Python que reproduz um ambiente de shell inspirado em sistemas Unix/Linux. Ele implementa um sistema de arquivos virtual em estrutura de árvore, permitindo navegação, criação e manipulação de diretórios e arquivos.

O objetivo do projeto é simular conceitos fundamentais de sistemas operacionais e interpretadores de comandos, utilizando apenas recursos nativos do Python, sem dependências externas.

---

## Funcionalidades

* Sistema de arquivos virtual em estrutura de árvore
* Interface de linha de comando (CLI) estilo shell
* Navegação entre diretórios (`cd`, `pwd`)
* Criação e remoção de diretórios (`mkdir`, `rmdir`)
* Criação, leitura, edição e remoção de arquivos (`touch`, `read`, `write`, `rm`)
* Listagem de conteúdo (`ls`)
* Comando de ajuda (`help`)
* Identificação do usuário (`whoami`)
* Limpeza de terminal (`clear` simulado)
* Interpretador de comandos baseado em loop principal

---

## Por que este projeto é interessante

Este projeto simula conceitos reais utilizados em sistemas operacionais:

* Estrutura hierárquica de sistema de arquivos (árvore)
* Interpretação de comandos de forma sequencial
* Manipulação de estado interno de um sistema
* Simulação de comportamento de shell real
* Separação entre lógica de sistema e interface de usuário

## Exemplo de comandos

```bash id="j8xq1m"
ls              Lista arquivos e diretórios
cd Documents    Acessa um diretório
mkdir Projetos  Cria uma nova pasta
touch file.txt  Cria um arquivo
write file.txt  Edita um arquivo
read file.txt   Lê o conteúdo de um arquivo
rm file.txt     Remove um arquivo
pwd             Mostra o diretório atual
clear           Limpa a tela
whoami          Mostra o usuário atual
exit            Encerra o terminal
```

---

## Estrutura do sistema

O sistema utiliza uma estrutura em árvore para representar diretórios e arquivos:

```text id="q2k8lm"
~
├── Desktop
├── Documents
│   └── Projetos
├── Downloads
```

Cada diretório contém:

* Subdiretórios
* Arquivos com conteúdo textual

---

## Aspectos técnicos

* Desenvolvido inteiramente em Python puro
* Sem uso de bibliotecas externas
* Estrutura baseada em dicionários (árvore dinâmica)
* Interpretador de comandos baseado em loop principal
* Manipulação de estado em tempo real

---

## O que este projeto demonstra

* Conhecimento de estruturas de dados (árvores e dicionários)
* Capacidade de construir sistemas interativos
* Entendimento básico de como shells funcionam
* Organização de código em nível intermediário
* Pensamento orientado a sistemas

---

## Como executar

```bash id="w1k9np"
python pybrasil.py
```

Nenhuma dependência externa é necessária.

---


## por [Guilherme Sodré](github.com/guisodre12/)

