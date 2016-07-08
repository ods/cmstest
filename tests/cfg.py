import ikcms.apps.web


class Cfg(ikcms.apps.web.Cfg):

    SITE_ID = 'tests'
    MYSQL_URL = 'mysql://root@localhost/test?charset=utf8'
    POSTGRESS_URL = 'postgress://root@localhost/test?charset=utf8'

    MEMCACHE_HOST = 'localhost'
    MEMCACHE_PORT = 11211


cfg = Cfg()
cfg.update_from_py()