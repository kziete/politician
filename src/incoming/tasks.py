from multiprocessing import Process
from celery import shared_task
# from scrapy.crawler import CrawlerProcess
# from scrapy.conf import settings

from .spider import BlogSpider

def in_process():
    crawler = CrawlerProcess(settings)
    crawler.install()
    crawler.configure()
    crawler.crawl(BlogSpider())
    crawler.start()
    crawler.stop()


@shared_task
def test_task():
    print('iniciando scrapy')

    p = Process(target=in_process)
    p.start()
    p.join()

    print('termino scrapy')
