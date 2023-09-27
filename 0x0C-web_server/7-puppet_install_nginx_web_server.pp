# Install Nginx package
package { 'nginx':
  ensure => present,
}

# Execute commands to configure Nginx
exec { 'Nginx_Configuration':
  command  => "sudo apt-get update && sudo apt-get install nginx -y && sudo ufw allow 'Nginx HTTP' && echo 'Hello World!' | sudo tee /var/www/html/index.html && sudo service nginx restart && sudo service nginx reload",
  path     => '/usr/bin:/bin',
  creates  => '/var/www/html/index.html',
  require  => Package['nginx'],
}

