from engines import capulet_engine as c
from engines import willoughby_engine as w
from engines import sterman_engine as s

class Engine(c.CapuletEngine, w.WilloughbyEngine, s.StermanEngine ):
    def needs_service(self):
        pass