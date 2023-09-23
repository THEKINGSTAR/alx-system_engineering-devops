# Using Puppet, install flask from pip3.

package { 'python3-pip':
  ensure => present,
}

exec { 'Flask':
  command  => 'pip3 install flask==2.1.0',
  provider => shell,
  path     => '/usr/local/bin:/usr/bin',
  unless   => 'pip3 show Flask | grep Version | grep -q 2.1.0',
  require  => Package['python3-pip'],
}
