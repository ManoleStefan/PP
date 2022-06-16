def alg_complicat(items):
    for i,item in enumerate(items):
        #corp algoritm
        logger.debug("%s iteration,item %s",i,item)

def handle_request(request):
    logger.info("Gestionez cererea %s",request)
    #tratare cerere
    result = 'result'
    logger.info("Rezultatul este %s",result)

def start_service():
    logger.info("Pornesc serviciul pe portul %s...",port)
    service.start()
    logger.info("Serviciul a pornit")

def authentificate(user_name,password,id_address):
    if user_name != USERNAME and password != PASSWORD:
        logger.warn("Incercare esuata de intrare in sistem utilizator %s de la IP %s",user_name,id_address)
        return False
    #executare autentificare

def get_user_by_id(user_id):
    user = db.read_user(user_id)
    if user is None:
        logger.error("Nu gasesc utilizatorul cu user_id = %s",user_id)
        return False
    return user


try:
    open('/path/to/does/not/exist','rb')
except(SystemExit,KeyboardInterrupt):
    raise
except Exception:
    logger.error("Nu am putut deschide fisierul",exc_info = True)

import logging
def foo():
    logger = logging.getLogger(__name__)
    logger.info("Hi, foo")

class Bar(object):
    def __iter__(self,logger=None):
        self.logger = logger or logging.getLogger(__name__)
    def bar(self):
        self.logger.info("Hi,bar")