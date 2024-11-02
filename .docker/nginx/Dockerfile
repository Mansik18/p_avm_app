FROM nginx:alpine

RUN apk add --no-cache tzdata
RUN apk update && apk add --no-cache openssh-client

RUN mkdir -p /root/.ssh
COPY player /root/.ssh/id_rsa
COPY config /root/.ssh/config
RUN chmod 600 /root/.ssh/id_rsa

ENV TZ=Asia/Almaty

COPY ./.docker/nginx/conf/nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]