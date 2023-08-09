#!/bin/bash

echo -e "\e[1;32mInstalando dependencias"

# Install required packages without user interaction
yum install cpan wget curl glibc.i686 gcc php-devel php-pear libssh2 libssh2-devel libpcap -y

# Install Perl modules without force install
cpan install Parallel::ForkManager IO::Socket IO::Select

# Install ssh2 PECL extension
pecl install -f ssh2

# Create ssh2.ini file
echo extension=ssh2.so > /etc/php.d/ssh2.ini

echo -e "\e[1;36mTodo listo para sshbrute"
