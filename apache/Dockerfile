FROM httpd:2.4-alpine

COPY my-httpd.conf /usr/local/apache2/conf/extra/my-httpd.conf

RUN echo "Include conf/extra/my-httpd.conf" >> /usr/local/apache2/conf/httpd.conf \
    && sed -i "s/#LoadModule proxy_module/LoadModule proxy_module/g" /usr/local/apache2/conf/httpd.conf \
    && sed -i "s/#LoadModule proxy_http_module/LoadModule proxy_http_module/g" /usr/local/apache2/conf/httpd.conf

EXPOSE 80
