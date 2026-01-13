FROM php:8.0-apache
WORKDIR /var/www/html

COPY . /var/www/html/

RUN rm -rf /var/www/html/.git
RUN rm -rf /var/www/html/.github

EXPOSE 80
