from packages import utils
import os
from .constants import SAVEPATH

def save(data):
    os.makedirs(os.path.dirname(SAVEPATH), exist_ok=True)
    newdata = []

    for item in data:
        newdata.append(item.todict())

    utils.writeJson(SAVEPATH, newdata)