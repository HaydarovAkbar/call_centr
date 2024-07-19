from decouple import config

env_name = config('ENV_NAME', default='development')

if env_name == 'development':
    from .dev import *
elif env_name == 'production':
    from .prod import *
else:
    from .base import *