class Config:
    FLASK_DEBUG = True

    SECRET_KEY = "lc+lb_^62*cfxf!5r32kd-obejem8rsejw=!l!v+tvfk00ivux"


class Development(Config):
    DATABASE_URI = "sqlite:////tmp/test.db"
    TESTING = True
    HOST = "0.0.0.0"
