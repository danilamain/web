sudo mysql -uroot -e "create database ask character set utf8"
sudo mysql -uroot -e "create user 'vbox'@'localhost'"
sudo mysql -uroot -e "grant all privileges on ask.* to 'vbox'@'localhost'"
sudo mysql -uroot -e "flush privileges"
