# boxoffice_scraper
1. Развернуть redis, postgres
2. Применить миграции:
alembic upgrade head
3. Запустить скрапинг (паралельно):
scrapy crawl kp_box_office_spider
scrapy crawl kp_weekends_spider
scrapy crawl kp_movies_spider