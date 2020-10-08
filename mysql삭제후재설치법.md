```shell
apt-get purge mysql-server

apt-get purge mysql-common

rm -rf /var/log/mysql

rm -rf /var/log/mysql.*

rm -rf /var/lib/mysql

rm -rf /etc/mysql

sudo apt autoremove

apt-get install mysql-server --fix-missing --fix-broken 
```



mysql-완전삭제-후-재설치



/usr/local/bin/charm