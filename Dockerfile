FROM prestashop/prestashop:8.0.0
#RUN chmod -R 775 . 
#RUN chown -R www-data:www-data /var/www/html
#RUN rm -rf /var/www/html/install
#RUN ls /var/www/html
#RUN rm -rf /var/www/html/install
#RUN ls /var/www/html
#RUN apt-get update && apt-get install memcached libmemcached-dev zlib1g-dev -y
#RUN pecl install memcached
#RUN echo extension=memcached.so >> /usr/local/etc/php/php.ini
#RUN /etc/init.d/apache2 restart
#BEG
#RUN chmod -R 775 /var/www/html
RUN rm -r /var/www/html/*
RUN ls /var/www
RUN ls /var/www/html
COPY prestashop /var/www/html
COPY ssl /etc/ssl/dlugierozdzki
COPY default-ssl.conf /etc/apache2/sites-available/default-ssl.conf
RUN ln -s /etc/apache2/sites-available/default-ssl.conf /etc/apache2/sites-enabled/default-ssl.conf
#END
#RUN rm -f /etc/apache2/sites-available/000-default.conf
#RUN chmod -R 777 /etc/ssl
#COPY ssl/000-default.conf /etc/apache2/sites-available/000-default.conf
#COPY ssl/apache-selfsigned.crt /etc/ssl/certs/apache-selfsigned.crt
#COPY ssl/apache-selfsigned.key /etc/ssl/private/apache-selfsigned.key
#COPY selenium/photo_import /var/www/html/img/products
#COPY parameters.php /var/www/html/app/config/parameters.php
#RUN rm -rf /var/www/html/var/cache/prod/*
RUN a2enmod ssl
#RUN a2enmod rewrite
RUN chmod -R 777 /var/www/html
RUN rm -rf /var/www/html/install
EXPOSE 80
