# best practices

$content = "Include /etc/ssh/ssh_config.d/*.conf\nHost *\n\tPasswordAuthentication no"

file {
    '/tmp/school':
    mode    => '0744',
    owner   => www-data,
    group   => www-data,
    content => $content,
}