import yaml


def get_config() -> dict:
    """
    Load conf file
    :return: conf
    :rtype: dict
    """
    with open("config.yml", "r") as ymlfile:
        return yaml.load(ymlfile, Loader=yaml.FullLoader)


def get_sudo_pass() -> str:
    """
    Return sudopass value from conf
    :return: sudo password
    :rtype: str
    """
    return get_config()['sudopass']


def get_template() -> list:
    """
    Return exploded template file
    :return: File lines
    :rtype: list
    """
    with open("vhosttemplate", "r") as template:
        return template.readlines()


def set_vhost_name(conf, vhostname) -> None:
    """
    Set domain name on conf file
    :param conf: Exploded conf template
    :type conf: list
    :param vhostname: Virtual host domain name
    :type vhostname: str
    """
    for line_index in range(0, len(conf)):
        conf[line_index] = conf[line_index].replace("vhostname", vhostname)
        line_index += 1


def set_server_email(conf, email) -> None:
    """
    Set server email on conf file
    :param conf: Exploded conf template
    :type conf: list
    :param email: Virtual host email
    :type email: str
    """
    conf[3] = conf[3].replace("email", email)


def set_project_directory(conf, path) -> None:
    """
    Set virtual host root directory
    :param conf: Exploded conf template
    :type conf: list
    :param path: project parent directory path
    :type path: str
    """
    conf[4] = conf[4].replace("directory", path)
