FROM debian
MAINTAINER Tim Horton <hortont424@gmail.com>

RUN echo "deb http://ftp.debian.org/debian stable main" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y nginx git-core make python python-genshi supervisor

RUN mkdir -p /var/www
RUN mkdir -p /var/log/supervisor

RUN git clone --depth 1 https://github.com/hortont424/hortont.com.git /var/www/hortont.com

WORKDIR /var/www/hortont.com
RUN NOPREFIX=1 make
RUN chown -R www-data /var/www

ADD nginx.conf /etc/nginx/nginx.conf
ADD supervisord.conf /etc/supervisor/supervisord.conf

EXPOSE 80

CMD ["/usr/bin/supervisord", "-n"]