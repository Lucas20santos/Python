# rotas e endepoint

## rotas 

O caminho que um pedido HTTP segue para chegar a um endpoint específico. O desenvolvedor da API define as rotas e especifica o método HTTP adequado para cada endpoint.

## endpoint

Os URIs definidos nas rotas para os quais as requisições podem ser enviadas. Os endpoints podem ser URLs ou localizadores de recursos uniformes.

## rotas com "/" barras no final e sem barra no final

Se for colocado a barra no final da url é vai chamar a página normalmente, enquanto sem a barra ele vai fazer um redicionamento

`

    @app.route('/projects/')
    def projects():
        return 'The project page'

`

quando eu for chamar essa página, preciso colocar a barra no final para não sofrer redirecionamento.
