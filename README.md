# Template para o framework Django

- [x] [Bootstrap 5.3](https://getbootstrap.com/).
- [x] [Django Bootstrap 5](https://github.com/zostera/django-bootstrap5).
- [x] [Environs](https://github.com/sloria/environs).
- [x] [Whitenoise](https://github.com/evansd/whitenoise).
- [x] [Django debug toolbar](https://github.com/jazzband/django-debug-toolbar).
- [x] [Django rosetta](https://pypi.org/project/django-rosetta/).

## Como usar

### Linux ou macOS

```bash
django-admin startproject \
--template https://github.com/natorsc/dj-tlp-bootstrap/archive/main.zip \
nome_do_projeto .
```

```bash
poetry add \
django \
whitenoise \
django-bootstrap5 \
django-rosetta \
environs[django]
```

```bash
poetry add \
pylint \
autopep8 \
isort \
django-debug-toolbar \
--group dev
```

### Microsof Windows

#### PowerShell

```ps
django-admin startproject `
--template https://github.com/natorsc/dj-tlp-bootstrap/archive/main.zip `
nome_do_projeto .
```

```ps
poetry add `
django `
whitenoise `
django-bootstrap5 `
django-rosetta `
environs[django]
```

```ps
poetry add `
pylint `
autopep8 `
isort `
django-debug-toolbar `
--group dev
```

## Configurar o projeto

Após instalar as dependências executar o arquivo `proj_conf.py` que está na pasta `_scripts`.

## Tradução

### Gettext

#### Microsoft Windows

- [Gettext iconv windows](https://mlocati.github.io/articles/gettext-iconv-windows.html).

> Adicionar o caminho `C:\Program Files\gettext-iconv\bin` na variável `path` do sistema operacional.

Exemplo de comando para gerar a tradução:

```bash
django-admin makemessages -l en_US
```

---

## Django

[Django](https://www.djangoproject.com/) é um framework web de alto nível, escrito em Python, que permite o desenvolvimento rápido de aplicações web seguras e escaláveis.

Ele segue o princípio do "batteries included", o que significa que vem com um conjunto abrangente de ferramentas e bibliotecas que facilitam a criação de sites complexos.

Algumas características-chave do Django incluem:

- ORM (Object-Relational Mapping): Django inclui um ORM que mapeia objetos Python para tabelas de banco de dados, simplificando o acesso e a manipulação de dados.
- Administração automática: O Django vem com um painel de administração automático que pode ser usado para gerenciar conteúdo de aplicativos sem a necessidade de escrever código.
- Padrão MTV (Model-Template-View): O Django segue o padrão MTV, semelhante ao padrão MVC (Model-View-Controller), que ajuda a separar a lógica de negócios da apresentação.
- Segurança: Django possui várias proteções integradas contra várias vulnerabilidades web, como ataques de injeção SQL, CSRF (Cross-Site Request Forgery) e XSS (Cross-Site Scripting).
- Escalabilidade: Django é altamente escalável e é usado em muitos sites de alto tráfego, como Instagram e Pinterest.
- Documentação abrangente: Django possui uma documentação detalhada e bem escrita, facilitando o aprendizado e o desenvolvimento com o framework.

---
