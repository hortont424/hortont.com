git --git-dir /var/www/hortont.com/.git --work-tree /var/www/hortont.com pull
cd /var/www/hortont.com
NOPREFIX=1 make
chown -R www-data /var/www
/usr/bin/supervisord -n