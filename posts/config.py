class DevelopmentConfig(object):
    DATABASE_URI = "postgresql://ericsokolov:thinkful@localhost:5432/posts"
    DEBUG = True

class TestingConfig(object):
    DATABASE_URI = "postgresql://ericsokolov:thinkful@localhost:5432/posts-test"
    DEBUG = True
