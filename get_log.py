import os
import yaml
import logging
import logging.config

YAML_PATH = "../lib/logging.yaml"


# logging初始化
def setup_logging(
        defaultPath: str = YAML_PATH,  # logging默认路径
        defaultLevel=logging.INFO,  # logging默认日志级别
        **kwargs):
    if os.path.exists(defaultPath):
        with open(defaultPath, 'r', encoding='utf-8') as f:
            config = yaml.load(f)
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=defaultLevel)
        raise FileNotFoundError(f"{defaultPath}不存在")


# Logger初始化装饰器
def InitLogger(
        *,
        loggerName: str = None,  # Logger名称，对应不同配置
        **kwargs) :
    def decorator(func):
        def wrapper(*func_args, **func_kwargs):
            setup_logging()
            if loggerName is not None:
                logger = logging.getLogger(loggerName)
            return func(*func_args, logger=logger, **func_kwargs)

        return wrapper

    return decorator

# def LoggerIsExisted(logger: logging.Logger) -> bool:
#     if isinstance(logger, logging.Logger):
#         return True
#     else:
#         return False
