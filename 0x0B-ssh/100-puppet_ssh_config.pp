#4. Client configuration file (w/ Puppet)
execute_code{'Turn off passwd auth':
	ensure => 'present',
	path   => '/etc/ssh/ssh_config',
	line   => 'PasswordAuthentication no',
	match  => 'PasswordAuthentication yes',
}
execute_code{'Turn off passwd auth':
        ensure => 'present',
        path   => '/etc/ssh/ssh_config',
        line   => 'IdentityFile ~/.ssh/school'
}
