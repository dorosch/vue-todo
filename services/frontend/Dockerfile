FROM node:lts-alpine

WORKDIR /app

COPY service /app

RUN npm install --no-package-lock && npm update vue-template-compiler

ENV NODE_OPTIONS=--openssl-legacy-provider

CMD ["npm", "run", "serve"]
