FROM prestashop/prestashop:8.0.0

RUN apt update -y
RUN apt install -y memcached
RUN apt install -y libz-dev libmemcached-dev
RUN pecl install memcached
RUN echo extension=memcached.so >> /usr/local/etc/php/conf.d/memcached.ini

RUN rm -r /var/www/html/*
COPY prestashop /var/www/html

COPY ssl /etc/ssl/dlugierozdzki
COPY default-ssl.conf /etc/apache2/sites-available/default-ssl.conf
RUN ln -s /etc/apache2/sites-available/default-ssl.conf /etc/apache2/sites-enabled/default-ssl.conf
RUN a2enmod ssl

RUN chmod -R 777 /var/www/html/var
#RUN chmod -R 777 /var/www/html/install
#RUN rm -rf /var/www/html/install
EXPOSE 80
