FROM nginx:1.19.0-alpine
#FROM nginxinc/nginx-unprivileged:1-alpine

COPY ./default.conf /etc/nginx/conf.d/default.conf

RUN mkdir -p /vol/static
RUN chmod 755 /vol/static

#USER root
#RUN mkdir /tapp
#RUN rm /etc/nginx/conf.d/default.conf
#COPY ./default.conf /etc/nginx/conf.d/
#
#
#WORKDIR /tapp
#USER nginx