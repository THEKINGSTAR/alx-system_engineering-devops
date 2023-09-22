# Using Puppet, create a file in /tmp.

$str = 'I love Puppet'

file { '/tmp/school':
  ensure  => file,
  content => $str,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744'
}
