import os

class Config:
    '''
    General configuartion parent class
    '''
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

    @staticmethod
    def init_app(app):
        pass



class ProdConfig(Config):
    '''
    Production configuration child class
    '''
    pass


class DevConfig(Config):
    '''
    Development configuration child class
    Args:
            config: The parent configuration class with general configuration settings
    '''
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}