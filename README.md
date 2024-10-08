# Django MongoEngine Logger

A Django logger that logs to MongoDB using MongoEngine.

## Installation

```bash
pip install django-mongo-logger
pip install mongoengine
```

## Usage

To configure the logger, add the following to your settings.py file:

```settings.py

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s",
        },
        "simple": {
            "format": "%(levelname)s %(message)s",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "mongo": {
            "level": "DEBUG",
            "class": "django_mongoengine_logger.logging.MongoDBHandler",
            "log_document_path": "django_mongoengine_logger.documents.LogDocument", # path to you mongo engine log Document if not provided if not provided package will use default Document
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": True,
        },
        "mongo_log": {
            "handlers": ["mongo"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}
```

**log save in mongodb database with default name of django_logs**

## Example

```
import logging

logger = logging.getLogger('mongo_log')
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.error('This is an error message')

# you can pass json string to log message too

import json
logger = logging.getLogger(json.dumps({"message": 'mongo_log'}))
logger.debug(json.dumps({"message":'This is a debug message'}))
logger.info(json.dumps({"message":'This is an info message'}))
logger.error(json.dumps({"message":'This is an error message'}))
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## Acknowledgements

any contributors to this project will be appreciated.
