FROM python:3.11.0-alpine3.17

RUN apk update \
  && apk add --no-cache gcc libc-dev python3 py3-pip python3-dev \
  && pip install --upgrade pip \
  && pip install mkdocs mkdocs-material plantuml-markdown python-markdown-math pygments pymdown-extensions

RUN pip install python-markdown-math mkdocs-awesome-pages-plugin mkdocs-autolinks-plugin mkdocs-macros-plugin

RUN mkdir -p /root/projects