# best practices

$content = "Host *\n\tIdentityFile ~/.ssh/school\n\tPasswordAuthentication no"

file { '/etc/ssh/ssh_config':
    ensure  => 'present',
    content => $content,
}