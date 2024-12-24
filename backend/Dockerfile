# Ubuntu 24.04をベースイメージとして使用
FROM ubuntu:24.04

# 必要な依存パッケージをインストール
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    wget \
    git \
    software-properties-common \
    zlib1g-dev \
    libncurses5-dev \
    libgdbm-dev \
    libnss3-dev \
    libssl-dev \
    libreadline-dev \
    libffi-dev \
    libsqlite3-dev \
    libbz2-dev \
    tk-dev \
    uuid-dev \
    xz-utils \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Python 3.13のソースをダウンロードしてビルド
ENV PYTHON_VERSION=3.13.0
RUN wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tar.xz && \
    tar -xf Python-${PYTHON_VERSION}.tar.xz && \
    cd Python-${PYTHON_VERSION} && \
    ./configure --enable-optimizations && \
    make -j$(nproc) && \
    make altinstall && \
    cd .. && \
    rm -rf Python-${PYTHON_VERSION}*

# Python3.13をデフォルトに設定
RUN update-alternatives --install /usr/bin/python3 python3 /usr/local/bin/python3.13 1 && \
    update-alternatives --set python3 /usr/local/bin/python3.13

# pipを最新バージョンにアップグレード
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.13

# Poetryのインストール
RUN curl -sSL https://install.python-poetry.org | python3 -

# Poetryのパスの設定
ENV PATH /root/.local/bin:$PATH

# Poetryが仮想環境を生成しないようにする
RUN poetry config virtualenvs.create false

# app/pyproject.tomlからライブラリを初回導入
COPY volumes/pyproject.toml .
RUN poetry install --no-root