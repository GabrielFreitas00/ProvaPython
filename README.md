# Prova Python
Me chamo Gabriel Bernardo Freitas, e aqui está a resolução da questão 4 para a explicação do projeto.

# Explicações para a Atividade 4

## Diretorio .venv

Esse diretório e responsável por criar um interpretador python virtual para o projeto em especifico, esse pratica e recomendada para evitar conflito de bibliotecas diferentes projetos, além que com o ambiente virtual e mais fácil de manipular o gerenciamento das bibliotecas

## Diretorio Log e arquivo logs.log

O diretório e o arquivo, são responsáveis por armazenar os logs do sistemas, mas só irá armazenar o que for registrado no código, e não tudo que foi printado no console, e necessário usar a biblioteca logging para poder armazenar os logs de forma pratica.

## Diretorio SCR

O diretório scr, são os módulos locais python, que tenham classe e métodos, também e utilizado para organização do projeto, onde podemos separar por exemplo, em sql.py, onde terá as classes e métodos necessários para realizar consultas sql, e não poluir a main.

## Arquivo __init__.py

Este arquivo e responsável para o python reconhecer o diretório e ou os arquivos como módulos python, ele e importante para podermos indicar quais módulos e classes queremos importar para a main.

## Arquivo ola_mundo.py

Este arquivo foi criado para a resolução da atividade, ele possui uma classe e um método para serem utilizados na main.py

## Arquivo .gitignore

Este arquivo e responsável para quando for dar push dos arquivos para o git ele ignorar certos tipos de arquivo, como o exemplo do .venv, que quando está no gitignore ele não será importado, ele pode ser usado para garantir a segurança de alguns arquivos de como .log, .env e etc, onde não queremos que eles sejam abertos para todos poderem ver.

## Arquivo main.py

Arquivo principal do projeto, nele será montado a estrutura do projeto que será rodado, onde também acontece as importações dos módulos que estão na pasta scr, sendo o arquivo principal, 

## Arquivo requirements.txt

Este arquivo e responsável para quando o projeto for montado, sabermos quais bibliotecas serão necessárias para projeto rodar além de suas respectivas versões, ele deve seguir um padrão no python para rodar corretamente no comando pip install requirements.txt

## Arquivo README.md

Este arquivo, e utilizado para ser uma apresentação inicial do projeto, nele normalmente vai conter, a ideia do projeto, como ele funciona, tecnologias iniciadas, como instalar/rodar o projeto, e mais informações inicias sobre o projeto.
