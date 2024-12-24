FROM postgres:17.2

RUN apt update && \
    apt-get update && \
    apt-get install -y git make gcc postgresql-server-dev-17


RUN cd /tmp && \
    git clone --branch v0.8.0 https://github.com/pgvector/pgvector.git && \
    cd ./pgvector && \
    make && \
    make install && \
    cd ../ && rm -rf pgvector

RUN apt install -y -V ca-certificates lsb-release wget && \
    wget https://apache.jfrog.io/artifactory/arrow/$(lsb_release --id --short | tr 'A-Z' 'a-z')/apache-arrow-apt-source-latest-$(lsb_release --codename --short).deb && \
    apt install -y -V ./apache-arrow-apt-source-latest-$(lsb_release --codename --short).deb && \
    wget https://packages.groonga.org/debian/groonga-apt-source-latest-$(lsb_release --codename --short).deb && \
    apt install -y -V ./groonga-apt-source-latest-$(lsb_release --codename --short).deb && \
    apt update
    
RUN apt install -y -V postgresql-17-pgdg-pgroonga groonga-tokenizer-mecab

# NOTE: 起動後にDatabase上での有効化が必要
# CREATE EXTENSION IF NOT EXISTS vector;
# CREATE EXTENSION IF NOT EXISTS pgroonga;