from .constants import LOGPATH
import logging

logging.basicConfig(
    filename=LOGPATH,
    level=logging.INFO,
    format="%(message)s"
)


def makeLog(item, logtype):
    logging.log(
        logging.INFO,
        f"[{item.date} - {item.hour}] {logtype}: {item.name}"
    )
