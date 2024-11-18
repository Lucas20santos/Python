# Autenticação e Autorização em Flask

## Entendendo Autenticação e Autorização

Autenticação e autorização são dois conceitos cruciais na segurança de APIs REESTful. Embora frequentemente usados de forma intercambiábel, eles se referem a processos distintos.

### Autenticação

Refere-se ao processo de verificar a identidade de um usuário. É como o sistema reconhece quem você é. Isso geralmente é feito através de um nome de usuário e senha, mas também pode incluir outros métodos, como tokens ou impressões digitais.

### Auttorização

Após a autenticação, a autorização determina quais recursos um usuaŕio autenticado tem permissão para acessar. Basicamente, é sobre o que você está autorizado a fazer. Por exemplo, um usaŕio administrador pode ter acesso a mais funcionalidades em comparação com um usuário comum.

### JWT (JSON Web Token)

JSON Web Tokens (JWT) é um padrão aberto (RFC 7519) que define uma maneira compacta e independente de transmitir informações de forma segura entre as partes como um objeto JSON.

#### Característica do JWT

- **Compacto**: Pode ser enviado através de uma URL, parâmetro POST ou no cabeçalho HTTP.

- **Autocontido:** A carga útil contém todas as informações necessáris sobre o usuário, evitando a necessidade de soncultar o banco de dados mais de uma vez.


