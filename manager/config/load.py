from packages import utils, models
from .constants import SAVEPATH

def load() -> list:
    try:
        toformat = utils.openJson(path=SAVEPATH)
        toreturn = [models.item.fromdict(c) for c in toformat]

        return toreturn
    
    except Exception as er:
         return []