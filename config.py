# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

WTF_CSRF_ENABLED = False

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"

# MONGO CONFIG
MONGO_DB = "db_product"
MONGO_SERVER = '127.0.0.1'
MONGO_PORT = '27017'
MONGO_SERVER_AUTH = False
MONGO_SERVER_USE_SSL = False
MONGO_USER = ""
MONGO_PASSWORD = ""

MONGO_URL_CONNECTION = ''

if MONGO_SERVER_AUTH and MONGO_SERVER_USE_SSL:
    MONGO_URL_CONNECTION = 'mongodb://%s:%s@%s:%s/?ssl=true' % (MONGO_USER, MONGO_PASSWORD, MONGO_SERVER, MONGO_PORT)
elif MONGO_SERVER_AUTH and not MONGO_SERVER_USE_SSL:
    MONGO_URL_CONNECTION = 'mongodb://%s:%s@%s:%s/' % (MONGO_USER, MONGO_PASSWORD, MONGO_SERVER, MONGO_PORT)
else:
    MONGO_URL_CONNECTION = 'mongodb://%s:%s/' % (MONGO_SERVER, MONGO_PORT)