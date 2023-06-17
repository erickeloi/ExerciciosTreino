from logging import basicConfig
from logging import DEBUG, INFO, WARNING, CRITICAL
from logging import debug, info, error
from logging import FileHandler, StreamHandler 

basicConfig(
    level=INFO,
    encoding='utf-8',
    format='[%(levelname)s] - %(message)s - [%(asctime)s]',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[StreamHandler()]
    #handlers=[FileHandler("meus_logs.txt", "w"),StreamHandler()]
)

debug('Mensagem de debug')
info('Mensagem informativa')
error('Mensagem de erro')
