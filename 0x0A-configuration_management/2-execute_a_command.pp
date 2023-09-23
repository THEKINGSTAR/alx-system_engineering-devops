# Using Puppet, create a manifest that kills a process named killmenow.

exec {"killmenow":
        command  => 'pkill -x killmenow',
        provider => shell,
        path     => '/usr/local/bin:/usr/bin'
}
