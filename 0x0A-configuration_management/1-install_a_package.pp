# puppet declarative script to install flask from pip3.

# install_flask.pp

package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  unless  => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
}
