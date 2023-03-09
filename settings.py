import logging


# class NewFunctionFilter(logging.Filter):
#    def filter(self, record) -> bool:
#        return True

class MegaHandler(logging.Handler):
    def __init__(self, filename):
        logging.Handler.__init__(self)
        self.filename = filename

    def emit(self, record):
        message = self.format(record)
        with open(self.filename, 'a') as file:
            file.write(message + '\n')


logger_config = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'std_format': {
            'format': '{asctime} - {levelname} - {name} - {module}:{funcName}:{lineno} - {message}',
            'style': '{'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'std_format',
            # 'filters': ['new_filter']
        },
        'file': {
            '()': MegaHandler,
            'level': 'WARNING',
            'filename': 'debug.log',
            'formatter': 'std_format'
        }
    },
    'loggers': {
        'app_logger': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
            # 'propagate': False
        }
    },
    # 'filters': {
    #    'new_filter': {
    #        '()': NewFunctionFilter,
    #    }
    # },
    # 'root': {}   # '': {}
    # 'incremental': True
}
