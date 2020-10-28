import os
import config_manager
import user_input_manager


def exec_with_sudo(command) -> int:
    """
    Execute commande with superuser permissions
    :param command: A shell command
    :type command: str
    :return: The command status code
    :rtype: int
    """
    return os.system('echo %s|sudo -S %s' % (config_manager.get_sudo_pass(), command))


def generate_apache_conf_vhost() -> None:
    """
    Generate virtual host file
    Enable configuration
    Check configuration
    Cancel procedure if configuration error
        else reload apache and add domain to host file
    """
    conf_file = config_manager.get_template()
    domain_name = user_input_manager.get_vhost_name_choice()
    config_manager.set_vhost_name(conf_file, domain_name)
    config_manager.set_server_email(conf_file, user_input_manager.get_server_email_choice())
    config_manager.set_project_directory(conf_file, user_input_manager.get_project_directory_choice())

    with open('./' + domain_name + '.conf', 'w') as fh:
        for line in conf_file:
            fh.write(line)

    exec_with_sudo('mv ./' + domain_name + '.conf /etc/apache2/sites-available/')
    exec_with_sudo('a2ensite ' + domain_name)

    if not exec_with_sudo('apache2ctl configtest'):
        exec_with_sudo('systemctl reload apache2')
        exec_with_sudo("sed -i '1i127.0.0.1       " + domain_name + '\' /etc/hosts')
    else:
        print("Apache config error, the new conf will be disable and remove")
        exec_with_sudo('rm /etc/apache2/sites-available/' + domain_name + '.conf')

    print('Done')


if __name__ == '__main__':
    generate_apache_conf_vhost()
