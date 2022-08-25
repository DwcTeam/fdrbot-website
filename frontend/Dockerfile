FROM node:16.14.2 as build-stage

WORKDIR /app

COPY . /app

RUN yarn

ENV PATH /app/src/node_modules/.bin:/usr/bin:$PATH

RUN yarn build

# Nginx
FROM nginx

WORKDIR /usr/share/nginx/html

RUN rm -rf ./*

COPY nginx.conf /etc/nginx/nginx.conf

COPY --from=build-stage /app/build .

ENTRYPOINT [ "nginx", "-g", "daemon off;" ]

