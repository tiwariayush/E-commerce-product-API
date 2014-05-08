import configparser

config = configparser.ConfigParser()
config.read("site.ini")

print config.sections()
