# Using Puppet, install flask from pip3.

exec {"ISNTALL FLASK FROM PIP3":
command  => 'pip3 install flask 2.1.0',
provider => shell,
}
