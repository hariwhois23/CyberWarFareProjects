FROM busybox:stable

LABEL version="Busybox" 

COPY ./index.html /www/index.html

CMD ["httpd", "-f", "-p", "8000", "-h", "/www"]