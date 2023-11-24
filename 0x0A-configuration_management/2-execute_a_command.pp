# kill process

exec { 'killmenow':
  command => '/bin/pkill killmenow',
}
