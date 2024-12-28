from logging import DEBUG, Formatter, StreamHandler, getLogger

# import coloredlogs

fmt = "%(asctime)s %(name)s:%(lineno)s %(funcName)s [%(levelname)s]: %(message)s"
handler_format = Formatter(fmt)

stream_handler = StreamHandler()
stream_handler.setFormatter(handler_format)

logger = getLogger("main")
logger.setLevel(DEBUG)
logger.addHandler(stream_handler)

# coloredlogs.install(
#     level='DEBUG',
#     logger=logger,
#     fmt=fmt,
#     # datefmt='%Y/%m/%d %H:%M:%S'
# )
