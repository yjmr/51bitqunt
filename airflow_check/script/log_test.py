from loguru import logger
logger.add("file.log", format="{time} {level} {message}", filter="", level="INFO",encoding='utf-8')
logger.debug("这是一条debug日志")
logger.info("这是一条info日志")
logger.info("这是一条info2日志")