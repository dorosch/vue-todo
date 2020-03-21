FROM node:lts-alpine as build-stage

WORKDIR /app

COPY service /app

RUN npm install --no-package-lock && \
    npm run build


FROM nginx:stable-alpine

COPY --from=build-stage /app/dist /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]
