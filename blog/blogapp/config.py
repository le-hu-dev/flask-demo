import os


class Config(object):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/blogapp/"

    # mysql config
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{passw}@{host}:3306/{db}'.format(
        user=os.getenv('MYSQL_USER', 'admin'),
        passw=os.getenv('MYSQL_PASSWORD', 'admin#123'),
        host=os.getenv('MYSQL_HOST', '172.20.110.103'),
        db=os.getenv('MYSQL_DATABASE', 'camera_portal_db')
    )
    # for debug, default value is false
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
