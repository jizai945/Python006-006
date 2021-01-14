from configparser import ConfigParser

def read_db_config(filename = 'config.ini', section = 'mysql'):
    ''' Read database configuration file and return a dictionary
    :param filename: name of the configuration file
    :param section: name of the configuration
    :return: a dictionary of database paramters 
    '''

    # create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to mysql
    if parser.has_section(section):
        items = parser.items(section)
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))
    print(items)    # 列表套元组的格式
    return dict(items)  # 强转成字典的形式

if __name__ == '__main__':
    print(read_db_config())