# MySQL

O MySQL é um sistema de gerenciamento de banco de dados relacional de código aberto amplamente utilizado.

Ele é especialmente popular para aplicativos da web e é uma parte essencial do LAMP (Linux, Apache, MySQL, PHP/Python/Perl), um conjunto de software comumente usado para executar servidores web.

O MySQL é conhecido por sua confiabilidade, escalabilidade e facilidade de uso, tornando-o uma escolha popular para desenvolvedores e organizações que precisam de um banco de dados robusto.

## mysqlclient

O `mysqlclient` é uma biblioteca Python que fornece uma interface para se comunicar com o banco de dados MySQL a partir de programas Python.

Ele é uma implementação do MySQL C API e é comumente usado em conjunto com o ORM (Object-Relational Mapping) Django para permitir que aplicativos Python se conectem e interajam com bancos de dados MySQL de forma eficiente e fácil.

## Instalação

### Binário

```bash
poetry add --only-binary :all: mysqlclient
```

### Compilado

#### Dependências

##### Arch Linux

```bash
sudo pacman -S \
python-mysqlclient
```

##### Ubuntu e derivados

```bash
sudo apt install \
python3-dev \
default-libmysqlclient-dev \
build-essential
```

Após realizar instalação das dependêcias:

```bash
poetry add mysqlclient
```

---

## Env file

### PythonAnywhere

```env
DATABASE_URL='mysql://DBUSER:PASSWORD@USER-NAME.mysql.pythonanywhere-services.com::3306/DATABASE-NAME'
```

---
