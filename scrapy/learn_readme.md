scrapy爬虫学习
scrapy win10安装失败解决办法
单独安装 twisted/win32/win64库
下载链接如下
https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted
1.进入链接https://www.lfd.uci.edu/~gohlke/pythonlibs/，直接CTRL+F进行页面查找Twisted
2.按照你对应的Python版本号下载所需的whl格式的安装包
3.打开cmd切换到下载目录，运行 pip3 install  Twisted‑19.2.0‑cp36‑cp36m‑win_amd64.whl  ,这里根据你自己的需求选择32或者64位版本；并且在这里建议大家用pip3安装python的插件。
4.这时候再次安装我们的爬虫scrapy框架就可以啦！


pip install Twisted-20.3.0-cp39-cp39-win_amd64.whl
pip install -i https://pypi.douban.com/simple/ scrapy

mkvirtualenv article_spider
workon article_spider

(article_spider) F:\PythonEnvs\article_spider>scrapy startproject ArticleSpider
New Scrapy project 'ArticleSpider', using template directory 'f:\pythonenvs\article_spider\lib\site-packages\scrapy\templates\project', created in:
    F:\PythonEnvs\article_spider\ArticleSpider

You can start your first spider with:
    cd ArticleSpider
    scrapy genspider example example.com


创建一个爬取的域名
(article_spider) F:\PythonEnvs\article_spider\ArticleSpider>scrapy genspider jobbole blog.jobbole.com
Created spider 'jobbole' using template 'basic' in module:
  ArticleSpider.spiders.jobbole
  
(article_spider) F:\PythonEnvs\article_spider\ArticleSpider>scrapy crawl jobbole  

新建 一个main.py 来处理pycharm里面来执行
 
在setting.py里找到这个
# Obey robots.txt rules
ROBOTSTXT_OBEY = False



  