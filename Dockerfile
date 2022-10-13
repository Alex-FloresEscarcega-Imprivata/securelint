FROM node:18
WORKDIR /usr/src/securelint

COPY package*.json ./

RUN npm install --save nan
RUN npm install --save-dev tree-sitter-cli
ENV PATH=$PATH:./node_modules/.bin


COPY grammar.js ./

RUN tree-sitter init-config
RUN tree-sitter generate

COPY rules/ ./rules/


CMD tree-sitter query rules/* inputs/*
