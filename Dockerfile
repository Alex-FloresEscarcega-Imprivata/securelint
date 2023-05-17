FROM node:18

RUN apt-get update
WORKDIR /securelint
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs  > /securelint/rustup.sh
RUN chmod 755 /securelint/rustup.sh
RUN /securelint/rustup.sh -y
RUN rm /securelint/rustup.sh
ENV PATH=$PATH:/root/.cargo/bin/
RUN cargo install lazy_static || true
RUN cargo install tree-sitter-cli@0.20.8


COPY package*.json ./

COPY grammar.js ./

RUN tree-sitter init-config
RUN tree-sitter generate

COPY rules/ ./rules/


ENTRYPOINT ["tree-sitter"] 
