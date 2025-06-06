# coding: utf-8
"""
A tool for parsing Scrapy log files periodically and incrementally, designed for ScrapydWeb.

GitHub: https://github.com/my8100/logparser
"""


###############################################################################
###############################################################################
## Make sure that [Scrapyd](https://github.com/scrapy/scrapyd) has been installed
## and started on the current host.
## ------------------------------ Chinese -------------------------------------
## 请先确保当前主机已经安装和启动 [Scrapyd](https://github.com/scrapy/scrapyd)。
###############################################################################
###############################################################################


############################## Basic Settings ##############################
# Enter the directory when you run Scrapyd, run the command below
# to find out where the Scrapy logs are stored:
# python -c "from os.path import abspath, isdir; from scrapyd.config import Config; path = abspath(Config().get('logs_dir')); print(path); print(isdir(path))"
# Check out https://scrapyd.readthedocs.io/en/stable/config.html#logs-dir for more info.
# e.g. 'C:/Users/username/logs' or '/home/username/logs'
SCRAPYD_LOGS_DIR = ''

# Sleep for N seconds before starting next round of parsing, the default is 10.
PARSE_ROUND_INTERVAL = 10


############################## Advanced Settings ##############################
# Only use for 'json_url' in the generated file 'stats.json' resides in SCRAPYD_LOGS_DIR.
# The default is '127.0.0.1:6800', so that the stats of Scrapyd jobs can be accessed at:
# http://127.0.0.1:6800/logs/stats.json
SCRAPYD_SERVER = '127.0.0.1:6800'

# Whether to collect Crawler.stats and Crawler.engine via telnet, the default is True.
# Check out https://doc.scrapy.org/en/latest/topics/telnetconsole.html for more info.
# Note that this feature only works for Scrapy<=1.5.1 if you are running Scrapyd on Windows or Fedora.
ENABLE_TELNET = True

# The default is '', set up this option only when you are using docker-compose.
# e.g. '127.0.0.1'
OVERRIDE_TELNET_CONSOLE_HOST = ''

# The encoding of the Scrapy logs, the default is 'utf-8'.
# https://doc.scrapy.org/en/latest/topics/settings.html#log-encoding
LOG_ENCODING = 'utf-8'

# LogParser would locate and parse the Scrapy log files with a specific extension.
# The default is ['.log', '.txt'].
LOG_EXTENSIONS = ['.log', '.txt']

# Extract the first N lines of the Scrapy log, the default is 100.
LOG_HEAD_LINES = 50

# Extract the last N lines of the Scrapy log, the default is 200.
LOG_TAIL_LINES = 50

# Keep only the last N logs of each item (e.g. critical_logs) in log_categories.
# The default is 10, set it to 0 to keep all.
LOG_CATEGORIES_LIMIT = 10

# Set up this option to limit the size of the generated file 'stats.json' resides in SCRAPYD_LOGS_DIR,
# by removing data of the deleted Scrapy logs, the default is 100.
JOBS_TO_KEEP = 200

# Limit the memory usage when parsing large log files.
# The default is 10 * 1000 * 1000, which equals to 10 MB.
CHUNK_SIZE = 10 * 1000 * 1000

# Whether to delete existing json files generated by LogParser at startup, the default is False.
DELETE_EXISTING_JSON_FILES_AT_STARTUP = True

# Whether to keep all parsed results in memory, the default is False.
# Set it to False to reduce the RAM usage of LogParser.
KEEP_DATA_IN_MEMORY = False

# The default is False, set it to True to set the logging level from INFO to DEBUG
VERBOSE = False
