#!/usr/bin/env python
#

## MAde by Louis Volant
## 2010-04-27

"""All the settings of the application."""


import os

##### General Properties #####
APPLICATION_NAME = "PyPNG"
INPUT_PNG_FILENAME = "coucou.png"
OUTPUT_HTML_FILENAME = "index.html"
OUTPUT_CSS_FILENAME = "coucou.ss"

##### Log Properties #####
LOG_FILENAME = "logs" + os.sep + "repport-pypng.log"
LOG_FILESIZE = 1048576
LOG_NBLOGFILES = 10
LOG_FORMATTER = "%(asctime)s - [%(levelname)s] %(name)s : %(message)s"
LOG_LEVEL = "DEBUG"
