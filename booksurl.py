# 构造作品URL
for i in range(38):
    for j in range(1,1000):
        if j<1000:
            sj = str(j)
        if j<100 :
            sj = "0" + str(j)
        if j<10:
            sj = "00" + str(j)
        siteUrl = "http://www.xbiquge.la/"
        url = siteUrl + str(i) + "/" + str(i) + sj + "/"
        if i == 37 and j == 217:
            break
        print(url)
        #spider(url)
