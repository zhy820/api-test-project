from utils.http_client import request
import logging

logger = (logging.getLogger(__name__))

#args
def demo(*args):
    logger.info(f"demo 被调用，参数: {args}")

def demeo2(**kwargs):
    #print(kwargs)
    logger.info(f"demo 被调用，参数: {kwargs}")



if __name__ == "__main__":
    logger.info("程序开始")

    demo(1,2,3,4,5)
    demeo2(**{"user": "admin", "password": "123456"})

    logger.info("程序结束")
