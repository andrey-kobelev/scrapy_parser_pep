from pathlib import Path

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

BASE_DIR = Path(__file__).parent
RESULTS_DIR_NAME = 'results'
CSV_PEP_FILE_NAME = 'pep_%(time)s.csv'
RESULTS_DIR = BASE_DIR.parent / RESULTS_DIR_NAME

FEEDS = {
    f'{RESULTS_DIR_NAME}/{CSV_PEP_FILE_NAME}': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    }
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
