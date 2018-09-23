import logging
from codeitsuisse import app
from codeitsuisse.routes import square
from codeitsuisse.routes import bryan
from codeitsuisse.routes import deeplearn_linreg
from codeitsuisse.routes import dino
logger = logging.getLogger(__name__)


@app.route('/', methods=['GET'])
def default_route():
    return deeplearn_linreg.kk()


logFormatter = logging.Formatter("%(asctime)s [%(filename)s] [%(funcName)s] [%(lineno)d] [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger()

rootLogger.setLevel(logging.INFO)

fileHandler = logging.FileHandler("team.log")
fileHandler.setFormatter(logFormatter)
rootLogger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)

logger.info("Starting application ...")
# comment out when push to heroku
app.run()

