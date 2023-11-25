# install werkzeug version 2.1.1 from pip3
package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}

# install flask version 2.1.0 from pip3 and require werkzeug version 2.1.1
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['werkzeug'],
}
