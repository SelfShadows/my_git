import logging
import time
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
#                     datefmt='%a, %d %b %Y %H:%M:%S',
#                     filename='test.log',
#                     filemode='w')


logger=logging.getLogger()
fh=logging.FileHandler('log.log',encoding='utf-8')
sh=logging.StreamHandler()   #创建一个屏幕控制对象
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s [line:%(lineno)d] : %(message)s')
formatter2=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s [line:%(lineno)d] : %(message)s')
#文件操作符 和 格式关联
fh.setFormatter(formatter)
sh.setFormatter(formatter2)
#logger对象 和 文件操作符关联
logger.addHandler(fh)
logger.addHandler(sh)


logger.debug('debug message')    #低级别的排错信息
logger.info('info message')      #正常信息
logging.warning('警告信息')        #警告信息
logging.error('error message')      #错误信息
logger.critical('critical message')#高级别的 严重错误信息