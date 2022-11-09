from configparser import ConfigParser

config = ConfigParser()
config.read("./config.ini")

db_host = config["MySQL"]['host']
db_port = config["MySQL"]['port']
db_pass = config["MySQL"]['password']
db_user = config["MySQL"]['username']
