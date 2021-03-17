# zslib-book-downloader

> 广东省立中山图书馆电子书批量下载工具

只需安装 `requests` 库，使用 Python 3。

使用方法：`python3 downloader.py`

---

前两天在 Hostloc 看到了有人发了广东省立中山图书馆目前公开了 6133 本免费电子书（其实是 6113 本）可供下载。

我看了一下发现下载源是超星，呐，都是大家的老朋友了，直接爬吧。

于是就花了五分钟写了个“爬虫”，一个晚上可算是下好了，100M 宽带真不给力啊（落泪）。

> 广东省立中山图书馆
来源：http://gdslzstsg.superlib.libsou.com/node/409.jspx
日期：2020-04-10
数量：6133（实际有效 6113）
大小：224.16 GB

看代码吧，只需要一个 `requests` 库。当然，都 0202 年了，必须得上 Python 3 咯。另外，这个下载是单线程的，也没有任何异常处理，毕竟五分钟写的要啥自行车（狗头保命）。

👉 [GitHub 传送门](https://github.com/imByteCat/zslib-book-downloader)

至于这个 `books.json` 文件是怎么来的，用 Chrome 抓一下就知道了。

这里直接给出此文件的链接：[传送门](http://unitvb.featurelib.libsou.com/book/list_jsonp?schoolid=72&cpage=1&pageSize=10000)

~~至于伸手党们想直接转存这 224GB 的电子书，你们就自己找办法联系我问我要吧。~~

2020年05月04日更新：百度网盘暂时不分享了，因为之前嫌占地方就删掉了，可以找其他已经保存的人转存下，这里再给一个 GD 链接好了：https://drive.google.com/drive/folders/1Ab2_JSxuZvPYbypY3eQQWr0Zhmd0f0QV?usp=sharing
