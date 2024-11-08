# Conceito básico dos bancos de dados não relacionais

## Introdução aos Bancos de Dados Não Relacionais

O objetivo geral do curso é fornecer uma introdução aos Bancos de Dados não relacionais e desenvolver habilidades na criação, modelagem e consulta no MongoDB

### O que é um Banco de Dados não relacional ?

- Termo correto: **NOT Only SQL**
- Não seguem modelo de tabelas e relacionamentos
- Projetados para lidar com **alto volume de dados**, alta escablabilidade
- Alta **flexibilidade** na estrutura de dados
- Eles são amplamente utilizados em cenários onde a consistência imediata dos dados não é crítica.

### Diferença

- SQL
    - Modelo de dados fixo
    - Escalabilidade vertical (hardware)
    - Transações ACID 100%
    - Linguagem de consulta SQL
- NoSQL
    - Modelo de dados fléxivel
    - Escalabilidade horizontal
    - Transações ACID ausentes total ou parcial
    - Cada SGBD tem sua própria

### Vangegens dos bancos de dados NoSQL

- Flexibilidade na modelagem
- Alta escalabilidade
- Melhor desempelho em cenário de consulta intensiva
- Tolerância a falhas

### Desvantagens dos bancos de dados NoSQL

- Menor consitência de dados imediata
- Menor suporte a consultas complexas ** depende do SGBD

## Visão geral dos tipos de NoSQL

### Tipos

- Dey-Value -> Chave Valor
    - Armazena dados como pares de chave e valor, onde cada chave é um identificador único para acessar o valor correspondente
    - Exemplo de SGBD
        - Redis
        - Riak
        - Amazon DynamoDB
    - Uso: Um site pode usar um banco de dados Redis para armazenar informaçõe de sensão de usuário
- Documento > Documento
    - Armazena dados em documentos semiestruturados, geralmente em formato JSON ou BSON
    - Exemplo de SGDB
        - MongoDB
        - Couchbase
        - Apache CouchDB
    - Uso: Um catálogo de e-commece pode usar o MongoDB para armazenar informações de produtos, como nome, descrição, preço e atributos adicionais.
- Coluna
    - Armazenam dados em formato de colunas, o que permite alta escalabilidade e eficiência em determinados tipos de consultas
    - Exemplo de SGBD:
        - Apache Cassandra
        - ScyllaDB
        - HBase
    - Uso: Um sistema de registro de aplicativos pode usar o Apache Cassandra para armazenar registros de logo.
- Grafos
    - Armazenar e consultar dados interconectados, onde os relacionamentos entre os dados são tão importantes quanto os próprios dados.
    - Exemplo de SGBD: 
        - Neo4j
        - Amazon Neptunhe
        - JanusGraph
    - Uso: Uma rede social pode usar o Neo4j para armazenar os perfis dos usuário e suas conexões, permitindo consuiltas eficeintes encontrar amigos em comum.
- entre outros...

## Introdução ao MongoDB

### O que é o MongoDB

- Banco de dados NoSQL orientado a documentos.
- Grande volumes de dados, escalabilidade horizontal e modelagem flexível.
- Não exige um esquema
- Permite que os documentos sejam armazenados em formato BSON (Binary JSON), proporcionando uma estrutura semiestruturada.

### Vangens

- Flexibilidade na modelgem de dados
- Escalabilidade horizontal para lidar com grandes volumes de dados
- Consultas ricas e suporte a consultas complexas
- Alta disponibilidade e tolerância a falhas
- Comunidade ativa e recursos de suporte

### Desvantagens

- Menor consistência imediata em comparação com bancos de dados relacionais.
- Consultas complexas podem exigir um maior conhecimento e planejamento adequado.
- Maior consumo de espalo de armazenamento em comparação com bancos de dados relacionais devido á flexibilidade dos documentos.

### Onde o MongoDB é usado

- Aplicações web: Onde a flexibilidade e a escalabilidade são cruciais para lidar com volumes variávies de dados
- Análise de big data: Análise de grandes volumes de dados não estruturados ou semiestruturados, fonecendo uma plataforma para armazenar e processar esses dados.
- Armazenamento de dados semiestruturados: Permite a inserção de documentos com estruturas diferentes em uma mesma coleção.
- Casos de uso de geolocalização: Com suas funcionalidades de consulta geoespacial, é adequado para casos de uso que envolvem dados baseados em localização, como aplicativos de mapeamento e rastreamento.

### acesso ao banco de dados

- lucasssantoss210
- 5Rmrjwgf0GJhuzqr

## Modelegem de dados usando documentos

### Estrutura do MongoDB

Baseado em documentos
- Database
    - Documentos
        - Coleção:
            - Agrupamento lógico de documentos
            - Não exige esquema ou que os documentos tenham a mesma estrutura.

#### Coleção:
- Agrupamento lógico de documentos
- Não exige esquema ou que os documentos tenham a mesma estrutura.

#### Características

- Os nomes das coleções devem seguir algumas regras:
    - Devem começar com uma letra ou um underscore(_)
    - Podem conter letras, números ou underscores
    - Não podem ser vazios.
    - Não podem ter mais de 64 bytes de comprimento

#### Documentos

- São armazenados em documentos BSON (BInary JSON), que são estrutures flexíveis e semiestruturas.
- Cada documento possui um identificar único chamado "_id"
- É composto por pares de chaves e valores
- Tamanho máximo:
    - Cada documento no mongodb pode ter um tamanho máximo de 16 MB
- Aninhamento de documentos
- Flexibilidade na evolução do esquema

#### TIpos de Dados SImples

- String
- Number
- Boolean
- Date
- Null
- Objectld

#### TIpos de Dados complexas

- Array
- Documento Embutido (Embedded Document)
- Referência (Reference)
- GeoJSON

#### Estrutura de um documento

`

    {
        _id: Objectld(""),
        "nome_campo": "valor_campo",
        ...
    }

`

## Estratégias de modelagem de dados eficientes e escaláveis

### Modelgem orientada por consultas

- A modelagem de dados no MongoDB deve ser orientada pelas consultas que serão realizadas com mais frequência

### Inner Documents

No MongoDB, é comum **denormalizar** os dados para evitar operações de junção (join) custosas. Isso significa que os dados relacionados podem ser armazenados juntos em um único documento, em vez de serem distribuídos em várias coleções.

### Quando usar

- Os dados aninhados são específicos para o documento pai.
- Os dados aninhados são sempre acessados juntamente com o documento pai.
- A cardinalidade do relacionamento é um-para-muitos (um usuário pode ter várias reservas.)

### Quando não usar

- Se os dados aninhados precisarem ser consultados e atualizados independentemente do documento pai, é mais adequado utilizar coleções separadas.

### Referência

- Forma de relacionar os documentos entre si.

### Quando usar

- Os dados têm seu próprio significado e podem ser acessados independentemente do documento pai.
- Os dados têm uma cardinalidade mais alta (por exemplo, vários usuários podem ter reservas).

### Quando não usar

- Se os dados aninhados precisarem ser consultados e atualizados independentemente do documento pai, é mais adequado utilizar coleções separados.

## Operações no MongoDB

### Criando um DataBase

use{{nome_do_banco}}

Enquanto o database não tiver uma collection ele não será apresentado na lista

### Crinao uma collection

- db.createCollection("usuario")
- db.createCollection("destinos")

### Inserindo documentos

- db.usuarios.insertOne({});
- db.usuarios.insertMany({});

### Consultando Documentos

- db.usuario.find({})
- db.usuario.findOne({})
- db.usuario.findOneAndUpdate({})
- db.usuario.findOneAndDelete({})

### Atualizando Documentos

- db.usuarios.updateOne({})
- db.usuarios.updateMany({})
- db.usuarios.replaceOne({})

### Operadores de Update

- $inc
- $push
- $set
- $unset
- $rename

### Excluindo Documentos

- db.usuarios.deleteOne({})
- db.usuarios.deleteMany({})

## Consultas simples operadores

### Igualdade

- Realiza consultas baseadas em um valor especifico para um campo
- db.usuarios.find({"endereco.cidade":"Recife"})

### Operadores Lógicos

Realiza consultas baseados em um valor especifico para um campo.

- $and
- $or
- $not

### Operadores de comparação

- $eq: ==
- $ne: !=
- $gt: >
- $gte: >=
- $It: <
- $Ite: <=
- $in: []
- $nin: []

### Projeções

Definir quais campos devem ser retornados em uma consulta.

### Ordenação

Ordenar os resultados de uma consulta com base em um ou mais campos.

### Limitação

Limitar o número de documentos retornados em uma consulta

### Paginação

- db.usuarios.find().skip(10).limit(5)

## Breve apresentação do Redis

### O que é o Redis ?

O Redis é um sistema de armazenamento de dados em memoria de alto desempenho.

### Principais caracteristicas do Redis

- Armazenamento em memoria
- Estrutura de Dados Versátil
- Operações Atômicas
- Cache de alto desempenho
- Pub/Sub (Publicação/Assinatura)

### Principais utilizações do Redis

- Cache de dados
- Filas de mensagens
- contagem de acessos e estatisticas em tempo real
- gerenciamento de sessoes
- cache de resultados de consultas

### Principais comando

- SET
- GET
- DEL
- EXISTS
- KEYS
- INCR
- DECR
