<h1 align="center"> Interpretador-Tiny</h1>
<div style="display: inline-block;">
<img align="center" height="20px" width="90px" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/> 
<img align="center" height="20px" width="90px" src="https://img.shields.io/badge/Made%20for-VSCode-1f425f.svg"/> 
<img align="center" height="20px" width="90px" src="https://img.shields.io/badge/Contributions-welcome-brightgreen.svg?style=flat"/>
</div>

## Introdução

O objetivo deste projeto é desenvolver um interpretador para a linguagem Tiny, a qual se caracteriza por ser uma linguagem de programação com uma sintaxe e semântica simples. Tal trabalho acadêmico, proposto pelos professores <a href="https://github.com/rimsa" target="_blank">Andrei Rimsa</a> (CEFET/MG) e <a href="https://github.com/DiegoAscanio" target="_blank">Diego Ascanio</a> (CEFET/MG) foi desenvolvido em Python, através da orientação a objetos, com o intuito de compreender os princípios fundamentais de interpretação de linguagens de programação. 

## Funcionalidades da Linguagem Tiny

- Comandos Suportados: O interpretador suporta quatro tipos de comandos: comandos condicionais (if), comandos de repetição (while), comandos de atribuição (id = expr) e comandos de saída (output expr).
- Expressões Lógicas e Aritméticas: A linguagem suporta expressões lógicas simples em comandos condicionais e de repetição, bem como expressões aritméticas sobre números inteiros.
- Variáveis e Entrada de Usuário: Identificadores (variáveis) podem ser usados para armazenar números inteiros. Além disso, a linguagem suporta leitura de valores inteiros do usuário (read).
- Operadores Aritméticos e Lógicos Suportados: Adição (+), subtração (-), multiplicação (*), divisão (/), resto da divisão (%), igual (==), diferente (!=), menor (<), maior (>), menor ou igual (<=) e maior ou igual (>=).

<strong><h4>Exemplo de programa em Tiny: Somatorio.tiny :</h4></strong>
```
program
    sum = 0;
    i = read;
    while i > 0 do
        sum = sum + i;
        i = read;
    done;
    output sum;
```

## Estrutura do Projeto

- ```Lexema.py```: Define a estrutura de dados para representar um token durante a análise léxica.
- ```Tipos_de_Tokens.py```: Enumera todos os tipos de tokens que podem ser encontrados durante a análise léxica.
- ```Tabela_de_Tokens.py```: Associa os tipos de tokens com os seus respectivos tokens.
- ```Maquina_de_Estados.py```: Implementa a lógica para análise léxica da linguagem Tiny usando uma máquina de oito estados de transição.
- ```Parser.py```: Arquivo responsável pela análise sintática do código fonte Tiny e pela geração da árvore de análise sintática.
- ```Expressoes.py```: Contém classes para representar expressões aritméticas e lógicas, bem como variáveis e entrada de usuário.
- ```Comandos.py```: Contém as classes que representam os diferentes tipos de comandos suportados pela linguagem Tiny, como atribuição, saída, condicionais e loops.
- ```main.py```: Arquivo de Execução

<strong><h4>Classe base: Lexeme.py :</h4></strong>

```python
class Lexema:
    
    def __init__(self, token, tipo_token, linha):
        self.token = token
        self.tipo_token = tipo_token
        self.linha = linha
```

## Instruções de Execução

No terminal, execute as seguintes instruções:
```
cd Interpretador_Tiny
python3 main.py
```
- Para modificar o arquivo teste, modifique a string ```nome_arq```, substituindo "somatorio.tiny" por qualquer um dos nove arquivos contidos na pasta ```Testes_Interpretador```.

<strong><h4>main.py:</h4></strong>

```python
def main ():
    nome_arq = 'Testes_Interpretador/somatorio.tiny'
    Interpretador = Parser()
    object_interpretador = Interpretador.inicio(nome_arq)
    object_interpretador.executar()
```

## Especificações do Dispositivo Utilizado

| Componentes            | Detalhes                                                                                         |
| -----------------------| -----------------------------------------------------------------------------------------------  |
|  `Processador`         | Intel(R) Core(TM) i7-1065G7 CPU @ 1.30GHz   1.50 GHz                                             |
|  `RAM Instalada`       | 8.0 GB (Utilizável: 7.8 GB)                                                                      |
|  `Tipo de Sistema`     | Sistema Operacional de 64 bits, processador baseado em x64                                       |
|  `Sistema Operacional` | Edição Windows 11 Home Single Language, versão 22H2                                              |

## Referências

[1] RIMSA, ANDREI - Repositório GitHub, @rimsa: tiny - Disponível em: https://github.com/rimsa/tiny. Acessado em 14 de Outubro de 2023.

[2] ASCANIO, DIEGO - Repositório GitHub, @DiegoAscanio: interpretador tiny incompleto - Disponível em: https:https://github.com/DiegoAscanio/interpretador-tiny-incompleto. Acessado em 11 de Outubro de 2023.

[3] ASCANIO, DIEGO - Repositório GitHub, @DiegoAscanio: analizador lexico exemplo - Disponível em: https:https://github.com/DiegoAscanio/analisador-lexico-exemplo. Acessado em 10 de Outubro de 2023.

[4] W3Schools - Python Tutorial. Disponível em: <https://www.w3schools.com/python/default.asp>. Acessado em: 09 de Outubro de 2023.
