#!/usr/bin/python3
# install flask vesrion 2.1.0 from pip3

package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
