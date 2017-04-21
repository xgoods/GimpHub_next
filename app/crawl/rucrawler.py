import requests
from bs4 import BeautifulSoup

def getMemes():
    memep1URL="http://www.quickmeme.com/page/1/"
    memep2URL="http://www.quickmeme.com/page/2/"
    memep3URL="http://www.quickmeme.com/page/3/"
    memep4URL="http://www.quickmeme.com/page/4/"
    memep5URL="http://www.quickmeme.com/page/5/"
    memep6URL="http://www.quickmeme.com/page/6/"
    memep7URL="http://www.quickmeme.com/page/7/"
    memep8URL="http://www.quickmeme.com/page/8/"
    memep9URL="http://www.quickmeme.com/page/9/"
    memep10URL="http://www.quickmeme.com/page/10/"
    
    r_memep1=requests.get(memep1URL)
    r_memep2=requests.get(memep2URL)
    r_memep3=requests.get(memep3URL)
    r_memep4=requests.get(memep4URL)
    r_memep5=requests.get(memep5URL)
    r_memep6=requests.get(memep6URL)
    r_memep7=requests.get(memep7URL)
    r_memep8=requests.get(memep8URL)
    r_memep9=requests.get(memep9URL)
    r_memep10=requests.get(memep10URL)
    
    memep1Soup=BeautifulSoup(r_memep1.content, "lxml")
    memep2Soup=BeautifulSoup(r_memep2.content, "lxml")
    memep3Soup=BeautifulSoup(r_memep3.content, "lxml")
    memep4Soup=BeautifulSoup(r_memep4.content, "lxml")
    memep5Soup=BeautifulSoup(r_memep5.content, "lxml")
    memep6Soup=BeautifulSoup(r_memep6.content, "lxml")
    memep7Soup=BeautifulSoup(r_memep7.content, "lxml")
    memep8Soup=BeautifulSoup(r_memep8.content, "lxml")
    memep9Soup=BeautifulSoup(r_memep9.content, "lxml")
    memep10Soup=BeautifulSoup(r_memep10.content, "lxml")
    
    memep1Links=memep1Soup.find_all("a")
    memep2Links=memep2Soup.find_all("a")
    memep3Links=memep3Soup.find_all("a")
    memep4Links=memep4Soup.find_all("a")
    memep5Links=memep5Soup.find_all("a")
    memep6Links=memep6Soup.find_all("a")
    memep7Links=memep7Soup.find_all("a")
    memep8Links=memep8Soup.find_all("a")
    memep9Links=memep9Soup.find_all("a")
    memep10Links=memep10Soup.find_all("a")
    
    linkList=[memep1Links,memep2Links,memep3Links,memep4Links,memep5Links,memep6Links,memep7Links,
              memep8Links,memep9Links,memep10Links]
    
    memeLinks=[]
    
    pointer=0
    
    listLength=len(linkList)
    
    
    for i in range(listLength):
        for link in linkList[pointer]:
            tempURL=link.get("href")
            if tempURL is None:
                continue
            if tempURL.startswith("/p/"):
                memeFix='http://www.quickmeme.com'
                memeResolved=memeFix+tempURL
                dictionary={}
                dictionary['category']='Memes'
                dictionary['url']=memeResolved
                dictionary['title']=link.get_text().replace('\n','')
                dictionary['title']=link.get_text().replace('\t','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    memeLinks.append(dictionary)
            
                
        pointer+=1

    return memeLinks
    

def getPolitics():
    
    nytimesURL="http://www.nytimes.com/pages/politics"
    cnnURL="http://www.cnn.com/specials/politics/national-politics"
    foxnewsURL="http://www.foxnews.com/politics"
    #cbsnewsURL="http://www.cbsnews.com/politics"
    abcnewsURL="http://www.abcnews.go.com/Politics/Election"
    reutersnewsURL="http://www.reuters.com/politics"
    bbcnewsURL="http://www.bbc.com/news/election/us2016"
    #yahoonewsURL="https://www.yahoo.com/news/politics"
    nbcnewsURL="http://www.nbcnews.com/politics/2016-election"
    usatodaynewsURL="http://www.usatoday.com/section/global/elections-2016/"
    #huffingtonpostnewsURL="http://www.huffingtonpost.com/section/politics"
    timenewsURL="http://www.time.com/politics"
    washingtonpostnewsURL="http://www.washingtonpost.com/politics/"
    guardiannewsURL="https://www.theguardian.com/us-news/us-elections-2016"
    #wsjnewsURL="http://www.wsj.com/news/politics"
    #latimesnewsURL="http://www.latimes.com/politics"
    nydailynewsURL="http://www.nydailynews.com/news/politics"
    #chicagotribunenewsURL="http://www.chicagotribune.com/news/nationworld/politics/"
   
    r_nytimes=requests.get(nytimesURL)
    r_CNN=requests.get(cnnURL)
    r_foxnews=requests.get(foxnewsURL)
    #r_cbsnews=requests.get(cbsnewsURL)
    r_abcnews=requests.get(abcnewsURL)
    r_reutersnews=requests.get(reutersnewsURL)
    r_bbcnews=requests.get(bbcnewsURL)
    #r_yahoonews=requests.get(yahoonewsURL)
    r_nbcnews=requests.get(nbcnewsURL)
    r_usatodaynews=requests.get(usatodaynewsURL)
    #r_huffingtonpostnews=requests.get(huffingtonpostnewsURL)
    r_timenews=requests.get(timenewsURL)
    r_washingtonpostnews=requests.get(washingtonpostnewsURL)
    r_guardiannews=requests.get(guardiannewsURL)
    #r_wsjnews=requests.get(wsjnewsURL)
    #r_latimesnews=requests.get(latimesnewsURL)
    r_nydailynews=requests.get(nydailynewsURL)
    #r_chicagotribunenews=requests.get(chicagotribunenewsURL)
    
    nytimesSoup=BeautifulSoup(r_nytimes.content, "lxml")
    cnnSoup=BeautifulSoup(r_CNN.content, "lxml")
    foxnewsSoup=BeautifulSoup(r_foxnews.content, "lxml")
    #cbsnewsSoup=BeautifulSoup(r_cbsnews.content, "lxml")
    abcnewsSoup=BeautifulSoup(r_abcnews.content, "lxml")
    reutersnewsSoup=BeautifulSoup(r_reutersnews.content, "lxml")
    bbcnewsSoup=BeautifulSoup(r_bbcnews.content, "lxml")
    #yahoonewsSoup=BeautifulSoup(r_yahoonews.content, "lxml")
    nbcnewsSoup=BeautifulSoup(r_nbcnews.content, "lxml")
    usatodaynewsSoup=BeautifulSoup(r_usatodaynews.content, "lxml")
    #huffingtonpostnewsSoup=BeautifulSoup(r_huffingtonpostnews.content, "lxml")
    timenewsSoup=BeautifulSoup(r_timenews.content, "lxml")
    washingtonpostnewsSoup=BeautifulSoup(r_washingtonpostnews.content, "lxml")
    guardiannewsSoup=BeautifulSoup(r_guardiannews.content, "lxml")
    #wsjnewsSoup=BeautifulSoup(r_wsjnews.content, "lxml")
    #latimesnewsSoup=BeautifulSoup(r_latimesnews.content, "lxml")
    nydailynewsSoup=BeautifulSoup(r_nydailynews.content, "lxml")
    #chicagotribunenewsSoup=BeautifulSoup(r_chicagotribunenews.content, "lxml")
    
    nytimesLinks=nytimesSoup.find_all("a")
    cnnLinks=cnnSoup.find_all("a")
    foxnewsLinks=foxnewsSoup.find_all("a")
    #cbsnewsLinks=cbsnewsSoup.find_all("a")
    abcnewsLinks=abcnewsSoup.find_all("a")
    reutersnewsLinks=reutersnewsSoup.find_all("a")
    bbcnewsLinks=bbcnewsSoup.find_all("a")
    #yahoonewsLinks=yahoonewsSoup.find_all("a")
    nbcnewsLinks=nbcnewsSoup.find_all("a")
    usatodaynewsLinks=usatodaynewsSoup.find_all("a")
    #huffingtonpostnewsLinks=huffingtonpostnewsSoup.find_all("a")
    timenewsLinks=timenewsSoup.find_all("a")
    washingtonpostnewsLinks=washingtonpostnewsSoup.find_all("a")
    guardiannewsLinks=guardiannewsSoup.find_all("a")
    #wsjnewsLinks=wsjnewsSoup.find_all("a")
    #latimesnewsLinks=latimesnewsSoup.find_all("a")
    nydailynewsLinks=nydailynewsSoup.find_all("a")
    #chicagotribunenewsLinks=chicagotribunenewsSoup.find_all("a")
    
    linkList=[nytimesLinks,cnnLinks,foxnewsLinks,abcnewsLinks,reutersnewsLinks,
            bbcnewsLinks,nbcnewsLinks,usatodaynewsLinks,timenewsLinks,
            washingtonpostnewsLinks,guardiannewsLinks,nydailynewsLinks]

    politicsLinks=[]
    politicsLinksFinal=[]
    politicsLinksTitle=[]
    politicsLinksTitleFinal=[]
    pointer=0
    
    listLength=len(linkList)
    
    
    for i in range(listLength):
        for link in linkList[pointer]:
            tempURL=link.get("href")
            if tempURL is None:
                continue
            if tempURL.startswith("http://www.nytimes.com/2016/"):
                dictionary={}
                dictionary['category']='Politics'
                dictionary['url']=tempURL
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    politicsLinks.append(dictionary)
            if tempURL.startswith("http://www.foxnews.com/politics/2016/10/"):
                dictionary={}
                dictionary['category']='Politics'
                dictionary['url']=tempURL
                dictionary['title']=link.get_text().replace('\n','')
                
                if dictionary['title'] and not dictionary['title'].isspace():
                    politicsLinks.append(dictionary)
            if tempURL.startswith("/2016/10/") or tempURL.startswith("/politics/2016/10/"):
                cnnFix='http://www.cnn.com'
                cnnResolved=cnnFix+tempURL
                dictionary={}
                dictionary['category']='Politics'
                dictionary['url']=cnnResolved
                dictionary['title']=link.get_text().replace('\n','')
                dictionary['title']=link.get_text().replace('\t','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    politicsLinks.append(dictionary)
            if tempURL.startswith('http://abcnews.go.com/Politics/'):
                dictionary={}
                dictionary['url']=tempURL
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    politicsLinks.append(dictionary)
            if tempURL.startswith("/article/us-usa-election"):
                reutersFix='http://www.reuters.com'
                reutersResolved=reutersFix+tempURL
                dictionary={}
                dictionary['category']='Politics'
                dictionary['url']=reutersResolved
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    politicsLinks.append(dictionary)
            if tempURL.startswith("http://time.com/453") or tempURL.startswith("http://time.com/454"):
                dictionary={}
                dictionary['category']='Politics'
                dictionary['url']=tempURL
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    politicsLinks.append(dictionary)
            if tempURL.startswith("https://www.washingtonpost.com/news/post-politics/wp/2016/") or tempURL.startswith("https://www.washingtonpost.com/news/the-fix/wp/2016/"):
                dictionary={}
                dictionary['category']='Politics'
                dictionary['url']=tempURL
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    politicsLinks.append(dictionary)
            if tempURL.startswith("https://www.theguardian.com/us-news/2016/"):
                dictionary={}
                dictionary['category']='Politics'
                dictionary['url']=tempURL
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    politicsLinks.append(dictionary)
            if tempURL.startswith("http://www.nydailynews.com/news/politics"):
                dictionary={}
                dictionary['category']='Politics'
                dictionary['url']=tempURL
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    politicsLinks.append(dictionary)
                
        pointer+=1

    return politicsLinks

 
def getBusiness():
    
    nytimesURL="http://www.nytimes.com/pages/business"
    cnnURL="http://www.money.cnn.com"
    foxnewsURL="http://www.foxbusiness.com"
    #cbsnewsURL="http://www.cbsnews.com/politics"
    abcnewsURL="http://www.abcnews.go.com/Business"
    reutersnewsURL="http://www.reuters.com/finance"
    bbcnewsURL="http://www.bbc.com/news/business"
    #yahoonewsURL="https://www.yahoo.com/news/politics"
    nbcnewsURL="http://www.nbcnews.com/business"
    usatodaynewsURL="http://www.usatoday.com/money/"
    #huffingtonpostnewsURL="http://www.huffingtonpost.com/section/business"
    timenewsURL="http://www.time.com/business"
    washingtonpostnewsURL="https://www.washingtonpost.com/business/"
    guardiannewsURL="https://www.theguardian.com/us/business"
    #wsjnewsURL="http://www.wsj.com/news/business"
    #latimesnewsURL="http://www.latimes.com/politics"
    #nydailynewsURL="http://www.nydailynews.com/news/politics"
    #chicagotribunenewsURL="http://www.chicagotribune.com/business"
   
    r_nytimes=requests.get(nytimesURL)
    r_CNN=requests.get(cnnURL)
    r_foxnews=requests.get(foxnewsURL)
    #r_cbsnews=requests.get(cbsnewsURL)
    r_abcnews=requests.get(abcnewsURL)
    r_reutersnews=requests.get(reutersnewsURL)
    r_bbcnews=requests.get(bbcnewsURL)
    #r_yahoonews=requests.get(yahoonewsURL)
    r_nbcnews=requests.get(nbcnewsURL)
    r_usatodaynews=requests.get(usatodaynewsURL)
    #r_huffingtonpostnews=requests.get(huffingtonpostnewsURL)
    r_timenews=requests.get(timenewsURL)
    r_washingtonpostnews=requests.get(washingtonpostnewsURL)
    r_guardiannews=requests.get(guardiannewsURL)
    #r_wsjnews=requests.get(wsjnewsURL)
    #r_latimesnews=requests.get(latimesnewsURL)
    #r_nydailynews=requests.get(nydailynewsURL)
    #r_chicagotribunenews=requests.get(chicagotribunenewsURL)
    
    nytimesSoup=BeautifulSoup(r_nytimes.content, "lxml")
    cnnSoup=BeautifulSoup(r_CNN.content, "lxml")
    foxnewsSoup=BeautifulSoup(r_foxnews.content, "lxml")
    #cbsnewsSoup=BeautifulSoup(r_cbsnews.content, "lxml")
    abcnewsSoup=BeautifulSoup(r_abcnews.content, "lxml")
    reutersnewsSoup=BeautifulSoup(r_reutersnews.content, "lxml")
    bbcnewsSoup=BeautifulSoup(r_bbcnews.content, "lxml")
    #yahoonewsSoup=BeautifulSoup(r_yahoonews.content, "lxml")
    nbcnewsSoup=BeautifulSoup(r_nbcnews.content, "lxml")
    usatodaynewsSoup=BeautifulSoup(r_usatodaynews.content, "lxml")
    #huffingtonpostnewsSoup=BeautifulSoup(r_huffingtonpostnews.content, "lxml")
    timenewsSoup=BeautifulSoup(r_timenews.content, "lxml")
    washingtonpostnewsSoup=BeautifulSoup(r_washingtonpostnews.content, "lxml")
    guardiannewsSoup=BeautifulSoup(r_guardiannews.content, "lxml")
    #wsjnewsSoup=BeautifulSoup(r_wsjnews.content, "lxml")
    #latimesnewsSoup=BeautifulSoup(r_latimesnews.content, "lxml")
    #nydailynewsSoup=BeautifulSoup(r_nydailynews.content, "lxml")
    #chicagotribunenewsSoup=BeautifulSoup(r_chicagotribunenews.content, "lxml")
    
    nytimesLinks=nytimesSoup.find_all("a")
    cnnLinks=cnnSoup.find_all("a")
    foxnewsLinks=foxnewsSoup.find_all("a")
    #cbsnewsLinks=cbsnewsSoup.find_all("a")
    abcnewsLinks=abcnewsSoup.find_all("a")
    reutersnewsLinks=reutersnewsSoup.find_all("a")
    bbcnewsLinks=bbcnewsSoup.find_all("a")
    #yahoonewsLinks=yahoonewsSoup.find_all("a")
    nbcnewsLinks=nbcnewsSoup.find_all("a")
    usatodaynewsLinks=usatodaynewsSoup.find_all("a")
    #huffingtonpostnewsLinks=huffingtonpostnewsSoup.find_all("a")
    timenewsLinks=timenewsSoup.find_all("a")
    washingtonpostnewsLinks=washingtonpostnewsSoup.find_all("a")
    guardiannewsLinks=guardiannewsSoup.find_all("a")
    #wsjnewsLinks=wsjnewsSoup.find_all("a")
    #latimesnewsLinks=latimesnewsSoup.find_all("a")
    #nydailynewsLinks=nydailynewsSoup.find_all("a")
    #chicagotribunenewsLinks=chicagotribunenewsSoup.find_all("a")
    
    linkList=[nytimesLinks,cnnLinks,foxnewsLinks,abcnewsLinks,reutersnewsLinks,
            bbcnewsLinks,nbcnewsLinks,usatodaynewsLinks,timenewsLinks,
            washingtonpostnewsLinks,guardiannewsLinks]

    businessLinks=[]
    pointer=0
    
    listLength=len(linkList)
    
    
    for i in range(listLength):
        for link in linkList[pointer]:
            tempURL=link.get("href")
            
            if tempURL is None:
                continue
            if tempURL.startswith("http://www.nytimes.com/2016/"):
                dictionary={}
                dictionary['category']='Business'
                dictionary['url']=tempURL
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    businessLinks.append(dictionary)
            if tempURL.startswith("/markets/2016") or tempURL.startswith("/politics/2016") or tempURL.startswith("/features/2016") or tempURL.startswith("/investing/2016"):
                foxFix='http://www.foxbusiness.com'
                foxResolve=foxFix+tempURL
                dictionary={}
                dictionary['category']='Business'
                dictionary['url']=foxResolve
                dictionary['title']=link.get_text().replace('\n','')
                
                if dictionary['title'] and not dictionary['title'].isspace():
                    businessLinks.append(dictionary)
            if tempURL.startswith("/2016/10/"):
                cnnFix='http://www.money.cnn.com'
                cnnResolved=cnnFix+tempURL
                dictionary={}
                dictionary['category']='Business'
                dictionary['url']=cnnResolved
                dictionary['title']=link.get_text().replace('\n','')
                dictionary['title']=link.get_text().replace('\t','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    businessLinks.append(dictionary)
            if tempURL.startswith('http://abcnews.go.com/Business/'):
                dictionary={}
                dictionary['category']='Business'
                dictionary['url']=tempURL
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    businessLinks.append(dictionary)
            if tempURL.startswith("/article/"):
                reutersFix='http://www.reuters.com'
                reutersResolved=reutersFix+tempURL
                dictionary={}
                dictionary['category']='Business'
                dictionary['url']=reutersResolved
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    businessLinks.append(dictionary)
            if tempURL.startswith("/news/business-1") or tempURL.startswith("/news/business-2") or tempURL.startswith("/news/business-3"):
                bbcFix='http://www.bbc.com'
                bbcResolved=bbcFix+tempURL
                dictionary={}
                dictionary['category']='Business'
                dictionary['url']=bbcResolved
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    businessLinks.append(dictionary)
            if tempURL.startswith("/business/consumer/") or tempURL.startswith("/business/personal-finance/") or tempURL.startswith("/business/economy/") or tempURL.startswith("/business/markets/"):
                nbcFix='http://www.nbcnews.com'
                nbcResolved=nbcFix+tempURL
                dictionary={}
                dictionary['category']='Business'
                dictionary['url']=nbcResolved
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    businessLinks.append(dictionary)
            if tempURL.startswith("/story/money/"):
                usatodayFix='http://www.usatoday.com'
                usatodayResolved=usatodayFix+tempURL
                dictionary={}
                dictionary['category']='Business'
                dictionary['url']=usatodayResolved
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    businessLinks.append(dictionary)
            if tempURL.startswith("http://time.com/453") or tempURL.startswith("http://time.com/454"):
                dictionary={}
                dictionary['category']='Business'
                dictionary['url']=tempURL
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    businessLinks.append(dictionary)
            if tempURL.startswith("https://www.washingtonpost.com/news/business/economy/") or  tempURL.startswith("https://www.washingtonpost.com/news/on-small-business/wp/2016/")or tempURL.startswith("https://www.washingtonpost.com/news/wonk/wp/2016/") or tempURL.startswith("https://www.washingtonpost.com/news/on-leadership/wp/2016/") or tempURL.startswith("https://www.washingtonpost.com/news/get-there/wp/2016/") or  tempURL.startswith("https://www.washingtonpost.com/news/the-swtich/wp/2016/") or tempURL.startswith("https://www.washingtonpost.com/news/capital-business/wp/2016/"):
                dictionary={}
                dictionary['category']='Business'
                dictionary['url']=tempURL
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    businessLinks.append(dictionary)
            if tempURL.startswith("https://www.theguardian.com/business/2016/") or  tempURL.startswith("https://www.theguardian.com/us-news/2016/") or tempURL.startswith("https://www.theguardian.com/technology/2016/") or tempURL.startswith("https://www.theguardian.com/environment/2016/") or tempURL.startswith("https://www.theguardian.com/world/2016/") or tempURL.startswith("https://www.theguardian.com/sustainable-business/2016/"):
                dictionary={}
                dictionary['category']='Business'
                dictionary['url']=tempURL
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    businessLinks.append(dictionary)
                    
        pointer+=1
            
    return businessLinks


def getWorldNews():
    
    nytimesURL="http://www.nytimes.com/pages/world"
    cnnURL="http://www.cnn.com/world"
    foxnewsURL="http://www.foxnews.com/world"
    #cbsnewsURL="http://www.cbsnews.com/politics"
    abcnewsURL="http://www.abcnews.go.com/International"
    reutersnewsURL="http://www.reuters.com/news/world"
    bbcnewsURL="http://www.bbc.com/news/world"
    #yahoonewsURL="https://www.yahoo.com/news/politics"
    nbcnewsURL="http://www.nbcnews.com/news/world"
    usatodaynewsURL="http://www.usatoday.com/news/world"
    #huffingtonpostnewsURL="http://www.huffingtonpost.com/section/business"
    timenewsURL="http://www.time.com/world"
    #washingtonpostnewsURL="https://www.washingtonpost.com/world/"
    guardiannewsURL="https://www.theguardian.com/world"
    #wsjnewsURL="http://www.wsj.com/news/business"
    #latimesnewsURL="http://www.latimes.com/politics"
    #nydailynewsURL="http://www.nydailynews.com/news/politics"
    #chicagotribunenewsURL="http://www.chicagotribune.com/business"
   
    r_nytimes=requests.get(nytimesURL)
    r_CNN=requests.get(cnnURL)
    r_foxnews=requests.get(foxnewsURL)
    #r_cbsnews=requests.get(cbsnewsURL)
    r_abcnews=requests.get(abcnewsURL)
    r_reutersnews=requests.get(reutersnewsURL)
    r_bbcnews=requests.get(bbcnewsURL)
    #r_yahoonews=requests.get(yahoonewsURL)
    r_nbcnews=requests.get(nbcnewsURL)
    r_usatodaynews=requests.get(usatodaynewsURL)
    #r_huffingtonpostnews=requests.get(huffingtonpostnewsURL)
    r_timenews=requests.get(timenewsURL)
    #r_washingtonpostnews=requests.get(washingtonpostnewsURL)
    r_guardiannews=requests.get(guardiannewsURL)
    #r_wsjnews=requests.get(wsjnewsURL)
    #r_latimesnews=requests.get(latimesnewsURL)
    #r_nydailynews=requests.get(nydailynewsURL)
    #r_chicagotribunenews=requests.get(chicagotribunenewsURL)
    
    nytimesSoup=BeautifulSoup(r_nytimes.content, "lxml")
    cnnSoup=BeautifulSoup(r_CNN.content, "lxml")
    foxnewsSoup=BeautifulSoup(r_foxnews.content, "lxml")
    #cbsnewsSoup=BeautifulSoup(r_cbsnews.content, "lxml")
    abcnewsSoup=BeautifulSoup(r_abcnews.content, "lxml")
    reutersnewsSoup=BeautifulSoup(r_reutersnews.content, "lxml")
    bbcnewsSoup=BeautifulSoup(r_bbcnews.content, "lxml")
    #yahoonewsSoup=BeautifulSoup(r_yahoonews.content, "lxml")
    nbcnewsSoup=BeautifulSoup(r_nbcnews.content, "lxml")
    usatodaynewsSoup=BeautifulSoup(r_usatodaynews.content, "lxml")
    #huffingtonpostnewsSoup=BeautifulSoup(r_huffingtonpostnews.content, "lxml")
    timenewsSoup=BeautifulSoup(r_timenews.content, "lxml")
    #washingtonpostnewsSoup=BeautifulSoup(r_washingtonpostnews.content, "lxml")
    guardiannewsSoup=BeautifulSoup(r_guardiannews.content, "lxml")
    #wsjnewsSoup=BeautifulSoup(r_wsjnews.content, "lxml")
    #latimesnewsSoup=BeautifulSoup(r_latimesnews.content, "lxml")
    #nydailynewsSoup=BeautifulSoup(r_nydailynews.content, "lxml")
    #chicagotribunenewsSoup=BeautifulSoup(r_chicagotribunenews.content, "lxml")
    
    nytimesLinks=nytimesSoup.find_all("a")
    cnnLinks=cnnSoup.find_all("a")
    foxnewsLinks=foxnewsSoup.find_all("a")
    #cbsnewsLinks=cbsnewsSoup.find_all("a")
    abcnewsLinks=abcnewsSoup.find_all("a")
    reutersnewsLinks=reutersnewsSoup.find_all("a")
    bbcnewsLinks=bbcnewsSoup.find_all("a")
    #yahoonewsLinks=yahoonewsSoup.find_all("a")
    nbcnewsLinks=nbcnewsSoup.find_all("a")
    usatodaynewsLinks=usatodaynewsSoup.find_all("a")
    #huffingtonpostnewsLinks=huffingtonpostnewsSoup.find_all("a")
    timenewsLinks=timenewsSoup.find_all("a")
    #washingtonpostnewsLinks=washingtonpostnewsSoup.find_all("a")
    guardiannewsLinks=guardiannewsSoup.find_all("a")
    #wsjnewsLinks=wsjnewsSoup.find_all("a")
    #latimesnewsLinks=latimesnewsSoup.find_all("a")
    #nydailynewsLinks=nydailynewsSoup.find_all("a")
    #chicagotribunenewsLinks=chicagotribunenewsSoup.find_all("a")
    
    linkList=[nytimesLinks,cnnLinks,foxnewsLinks,abcnewsLinks,reutersnewsLinks,
            bbcnewsLinks,nbcnewsLinks,usatodaynewsLinks,timenewsLinks,guardiannewsLinks]

    worldNewsLinks=[]
    pointer=0
    
    listLength=len(linkList)
    
    
    for i in range(listLength):
        for link in linkList[pointer]:
            tempURL=link.get("href")
            
            if tempURL is None:
                continue
            if tempURL.startswith("http://www.nytimes.com/2016/"):
                dictionary={}
                dictionary['category']='World_News'
                dictionary['url']=tempURL
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    worldNewsLinks.append(dictionary)
            if tempURL.startswith("/world/2016/10/"):
                foxFix='http://www.foxnews.com'
                foxResolve=foxFix+tempURL
                dictionary={}
                dictionary['category']='World_News'
                dictionary['url']=foxResolve
                dictionary['title']=link.get_text().replace('\n','')
                
                if dictionary['title'] and not dictionary['title'].isspace():
                    worldNewsLinks.append(dictionary)
            if tempURL.startswith("/2016/10/"):
                cnnFix='http://www.cnn.com'
                cnnResolved=cnnFix+tempURL
                dictionary={}
                dictionary['category']='World_News'
                dictionary['url']=cnnResolved
                dictionary['title']=link.get_text().replace('\n','')
                dictionary['title']=link.get_text().replace('\t','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    worldNewsLinks.append(dictionary)
            if tempURL.startswith("/International/wireStory"):
                abcFix='http://www.abcnews.go.com'
                abcResolved=abcFix+tempURL
                dictionary={}
                dictionary['category']='World_News'
                dictionary['url']=abcResolved
                dictionary['title']=link.get_text().replace('\n','')
                dictionary['title']=link.get_text().replace('\t','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    worldNewsLinks.append(dictionary)
            if tempURL.startswith("/article/") or tempURL.startswith("/video/2016/10/"):
                reutersFix='http://www.reuters.com'
                reutersResolved=reutersFix+tempURL
                dictionary={}
                dictionary['category']='World_News'
                dictionary['url']=reutersResolved
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    worldNewsLinks.append(dictionary)
            if tempURL.startswith("/news/world-africa") or tempURL.startswith("/news/world-europe") or tempURL.startswith("/news/world-us"):
                bbcFix='http://www.bbc.com'
                bbcResolved=bbcFix+tempURL
                dictionary={}
                dictionary['category']='World_News'
                dictionary['url']=bbcResolved
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    worldNewsLinks.append(dictionary)
            if tempURL.startswith("/news/world/"):
                nbcFix='http://www.nbcnews.com'
                nbcResolved=nbcFix+tempURL
                dictionary={}
                dictionary['category']='World_News'
                dictionary['url']=nbcResolved
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    worldNewsLinks.append(dictionary)
            if tempURL.startswith("/story/news/world/2016/10/"):
                usatodayFix='http://www.usatoday.com'
                usatodayResolved=usatodayFix+tempURL
                dictionary={}
                dictionary['category']='World_News'
                dictionary['url']=usatodayResolved
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    worldNewsLinks.append(dictionary)
            if tempURL.startswith("http://time.com/453") or tempURL.startswith("http://time.com/454"):
                dictionary={}
                dictionary['category']='World_News'
                dictionary['url']=tempURL
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    worldNewsLinks.append(dictionary)
            
            if tempURL.startswith("https://www.theguardian.com/world/2016/oct/"):
                dictionary={}
                dictionary['category']='World_News'
                dictionary['url']=tempURL
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    worldNewsLinks.append(dictionary)
                    
        pointer+=1
            
    return worldNewsLinks


def getUSNews():
    
    nytimesURL="http://www.nytimes.com/section/us"
    cnnURL="http://www.cnn.com/us"
    foxnewsURL="http://www.foxnews.com/us"
    #cbsnewsURL="http://www.cbsnews.com/politics"
    abcnewsURL="http://www.abcnews.go.com/US"
    reutersnewsURL="http://www.reuters.com/news/us"
    bbcnewsURL="http://www.bbc.com/news/world/us_and_canada"
    #yahoonewsURL="https://www.yahoo.com/news/politics"
    nbcnewsURL="http://www.nbcnews.com/news/us-news"
    usatodaynewsURL="http://www.usatoday.com/news/nation"
    #huffingtonpostnewsURL="http://www.huffingtonpost.com/section/business"
    timenewsURL="http://www.time.com/us"
    #washingtonpostnewsURL="https://www.washingtonpost.com/world/"
    guardiannewsURL="https://www.theguardian.com/us"
    #wsjnewsURL="http://www.wsj.com/news/business"
    #latimesnewsURL="http://www.latimes.com/politics"
    #nydailynewsURL="http://www.nydailynews.com/news/politics"
    #chicagotribunenewsURL="http://www.chicagotribune.com/business"
   
    r_nytimes=requests.get(nytimesURL)
    r_CNN=requests.get(cnnURL)
    r_foxnews=requests.get(foxnewsURL)
    #r_cbsnews=requests.get(cbsnewsURL)
    r_abcnews=requests.get(abcnewsURL)
    r_reutersnews=requests.get(reutersnewsURL)
    r_bbcnews=requests.get(bbcnewsURL)
    #r_yahoonews=requests.get(yahoonewsURL)
    r_nbcnews=requests.get(nbcnewsURL)
    r_usatodaynews=requests.get(usatodaynewsURL)
    #r_huffingtonpostnews=requests.get(huffingtonpostnewsURL)
    r_timenews=requests.get(timenewsURL)
    #r_washingtonpostnews=requests.get(washingtonpostnewsURL)
    r_guardiannews=requests.get(guardiannewsURL)
    #r_wsjnews=requests.get(wsjnewsURL)
    #r_latimesnews=requests.get(latimesnewsURL)
    #r_nydailynews=requests.get(nydailynewsURL)
    #r_chicagotribunenews=requests.get(chicagotribunenewsURL)
    
    nytimesSoup=BeautifulSoup(r_nytimes.content, "lxml")
    cnnSoup=BeautifulSoup(r_CNN.content, "lxml")
    foxnewsSoup=BeautifulSoup(r_foxnews.content, "lxml")
    #cbsnewsSoup=BeautifulSoup(r_cbsnews.content, "lxml")
    abcnewsSoup=BeautifulSoup(r_abcnews.content, "lxml")
    reutersnewsSoup=BeautifulSoup(r_reutersnews.content, "lxml")
    bbcnewsSoup=BeautifulSoup(r_bbcnews.content, "lxml")
    #yahoonewsSoup=BeautifulSoup(r_yahoonews.content, "lxml")
    nbcnewsSoup=BeautifulSoup(r_nbcnews.content, "lxml")
    usatodaynewsSoup=BeautifulSoup(r_usatodaynews.content, "lxml")
    #huffingtonpostnewsSoup=BeautifulSoup(r_huffingtonpostnews.content, "lxml")
    timenewsSoup=BeautifulSoup(r_timenews.content, "lxml")
    #washingtonpostnewsSoup=BeautifulSoup(r_washingtonpostnews.content, "lxml")
    guardiannewsSoup=BeautifulSoup(r_guardiannews.content, "lxml")
    #wsjnewsSoup=BeautifulSoup(r_wsjnews.content, "lxml")
    #latimesnewsSoup=BeautifulSoup(r_latimesnews.content, "lxml")
    #nydailynewsSoup=BeautifulSoup(r_nydailynews.content, "lxml")
    #chicagotribunenewsSoup=BeautifulSoup(r_chicagotribunenews.content, "lxml")
    
    nytimesLinks=nytimesSoup.find_all("a")
    cnnLinks=cnnSoup.find_all("a")
    foxnewsLinks=foxnewsSoup.find_all("a")
    #cbsnewsLinks=cbsnewsSoup.find_all("a")
    abcnewsLinks=abcnewsSoup.find_all("a")
    reutersnewsLinks=reutersnewsSoup.find_all("a")
    bbcnewsLinks=bbcnewsSoup.find_all("a")
    #yahoonewsLinks=yahoonewsSoup.find_all("a")
    nbcnewsLinks=nbcnewsSoup.find_all("a")
    usatodaynewsLinks=usatodaynewsSoup.find_all("a")
    #huffingtonpostnewsLinks=huffingtonpostnewsSoup.find_all("a")
    timenewsLinks=timenewsSoup.find_all("a")
    #washingtonpostnewsLinks=washingtonpostnewsSoup.find_all("a")
    guardiannewsLinks=guardiannewsSoup.find_all("a")
    #wsjnewsLinks=wsjnewsSoup.find_all("a")
    #latimesnewsLinks=latimesnewsSoup.find_all("a")
    #nydailynewsLinks=nydailynewsSoup.find_all("a")
    #chicagotribunenewsLinks=chicagotribunenewsSoup.find_all("a")
    
    linkList=[nytimesLinks,cnnLinks,foxnewsLinks,abcnewsLinks,reutersnewsLinks,
            bbcnewsLinks,nbcnewsLinks,usatodaynewsLinks,timenewsLinks,guardiannewsLinks]

    USNewsLinks=[]
    pointer=0
    
    listLength=len(linkList)
    outf=open("USNewsLinks.txt",'w')
    
    for i in range(listLength):
        for link in linkList[pointer]:
            tempURL=link.get("href")
            
            if tempURL is None:
                continue
            if tempURL.startswith("http://www.nytimes.com/2016/"):
                dictionary={}
                dictionary['category']='US_News'
                dictionary['url']=tempURL
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    USNewsLinks.append(dictionary)
            if tempURL.startswith("/us/2016/10/"):
                foxFix='http://www.foxnews.com'
                foxResolve=foxFix+tempURL
                dictionary={}
                dictionary['category']='US_News'
                dictionary['url']=foxResolve
                dictionary['title']=link.get_text().replace('\n','')
                
                if dictionary['title'] and not dictionary['title'].isspace():
                    USNewsLinks.append(dictionary)
            if tempURL.startswith("/2016/10/"):
                cnnFix='http://www.cnn.com'
                cnnResolved=cnnFix+tempURL
                dictionary={}
                dictionary['category']='US_News'
                dictionary['url']=cnnResolved
                dictionary['title']=link.get_text().replace('\n','')
                dictionary['title']=link.get_text().replace('\t','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    USNewsLinks.append(dictionary)
            if tempURL.startswith("/US/wireStory/"):
                abcFix='http://www.abcnews.go.com'
                abcResolved=abcFix+tempURL
                dictionary={}
                dictionary['category']='US_News'
                dictionary['url']=abcResolved
                dictionary['title']=link.get_text().replace('\n','')
                dictionary['title']=link.get_text().replace('\t','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    USNewsLinks.append(dictionary)
            if tempURL.startswith("/article/") or tempURL.startswith("/video/2016/10/"):
                reutersFix='http://www.reuters.com'
                reutersResolved=reutersFix+tempURL
                dictionary={}
                dictionary['category']='US_News'
                dictionary['url']=reutersResolved
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    USNewsLinks.append(dictionary)
            if tempURL.startswith("/news/election-us") or tempURL.startswith("/news/world-us"):
                bbcFix='http://www.bbc.com'
                bbcResolved=bbcFix+tempURL
                dictionary={}
                dictionary['category']='US_News'
                dictionary['url']=bbcResolved
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    USNewsLinks.append(dictionary)
            if tempURL.startswith("/news/us-news/"):
                nbcFix='http://www.nbcnews.com'
                nbcResolved=nbcFix+tempURL
                dictionary={}
                dictionary['category']='US_News'
                dictionary['url']=nbcResolved
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    USNewsLinks.append(dictionary)
            if tempURL.startswith("/story/news/nation-now/2016/10/"):
                usatodayFix='http://www.usatoday.com'
                usatodayResolved=usatodayFix+tempURL
                dictionary={}
                dictionary['category']='US_News'
                dictionary['url']=usatodayResolved
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    USNewsLinks.append(dictionary)
            if tempURL.startswith("http://time.com/453") or tempURL.startswith("http://time.com/454"):
                dictionary={}
                dictionary['category']='US_News'
                dictionary['url']=tempURL
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    USNewsLinks.append(dictionary)
            
            if tempURL.startswith("https://www.theguardian.com/us-news/2016/oct/"):
                dictionary={}
                dictionary['category']='US_News'
                dictionary['url']=tempURL
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    USNewsLinks.append(dictionary)
                    
        pointer+=1
            
    return USNewsLinks

def getEntertainment():
    
    nytimesURL="http://www.nytimes.com/section/arts"
    cnnURL="http://www.cnn.com/entertainment"
    foxnewsURL="http://www.foxnews.com/entertainment"
    #cbsnewsURL="http://www.cbsnews.com/politics"
    abcnewsURL="http://www.abcnews.go.com/Entertainment"
    reutersnewsURL="http://www.reuters.com/news/entertainment"
    bbcnewsURL="http://www.bbc.com/news/entertainment_and_arts"
    #yahoonewsURL="https://www.yahoo.com/news/politics"
    #nbcnewsURL="http://www.nbcnews.com/pop-culture"
    usatodaynewsURL="http://www.usatoday.com/life"
    #huffingtonpostnewsURL="http://www.huffingtonpost.com/section/business"
    timenewsURL="http://www.time.com/entertainment"
    #washingtonpostnewsURL="https://www.washingtonpost.com/world/"
    guardiannewsURL="https://www.theguardian.com/us/culture"
    #wsjnewsURL="http://www.wsj.com/news/business"
    #latimesnewsURL="http://www.latimes.com/politics"
    #nydailynewsURL="http://www.nydailynews.com/news/politics"
    #chicagotribunenewsURL="http://www.chicagotribune.com/business"
   
    r_nytimes=requests.get(nytimesURL)
    r_CNN=requests.get(cnnURL)
    r_foxnews=requests.get(foxnewsURL)
    #r_cbsnews=requests.get(cbsnewsURL)
    r_abcnews=requests.get(abcnewsURL)
    r_reutersnews=requests.get(reutersnewsURL)
    r_bbcnews=requests.get(bbcnewsURL)
    #r_yahoonews=requests.get(yahoonewsURL)
    #r_nbcnews=requests.get(nbcnewsURL)
    r_usatodaynews=requests.get(usatodaynewsURL)
    #r_huffingtonpostnews=requests.get(huffingtonpostnewsURL)
    r_timenews=requests.get(timenewsURL)
    #r_washingtonpostnews=requests.get(washingtonpostnewsURL)
    r_guardiannews=requests.get(guardiannewsURL)
    #r_wsjnews=requests.get(wsjnewsURL)
    #r_latimesnews=requests.get(latimesnewsURL)
    #r_nydailynews=requests.get(nydailynewsURL)
    #r_chicagotribunenews=requests.get(chicagotribunenewsURL)
    
    nytimesSoup=BeautifulSoup(r_nytimes.content, "lxml")
    cnnSoup=BeautifulSoup(r_CNN.content, "lxml")
    foxnewsSoup=BeautifulSoup(r_foxnews.content, "lxml")
    #cbsnewsSoup=BeautifulSoup(r_cbsnews.content, "lxml")
    abcnewsSoup=BeautifulSoup(r_abcnews.content, "lxml")
    reutersnewsSoup=BeautifulSoup(r_reutersnews.content, "lxml")
    bbcnewsSoup=BeautifulSoup(r_bbcnews.content, "lxml")
    #yahoonewsSoup=BeautifulSoup(r_yahoonews.content, "lxml")
    #nbcnewsSoup=BeautifulSoup(r_nbcnews.content, "lxml")
    usatodaynewsSoup=BeautifulSoup(r_usatodaynews.content, "lxml")
    #huffingtonpostnewsSoup=BeautifulSoup(r_huffingtonpostnews.content, "lxml")
    timenewsSoup=BeautifulSoup(r_timenews.content, "lxml")
    #washingtonpostnewsSoup=BeautifulSoup(r_washingtonpostnews.content, "lxml")
    guardiannewsSoup=BeautifulSoup(r_guardiannews.content, "lxml")
    #wsjnewsSoup=BeautifulSoup(r_wsjnews.content, "lxml")
    #latimesnewsSoup=BeautifulSoup(r_latimesnews.content, "lxml")
    #nydailynewsSoup=BeautifulSoup(r_nydailynews.content, "lxml")
    #chicagotribunenewsSoup=BeautifulSoup(r_chicagotribunenews.content, "lxml")
    
    nytimesLinks=nytimesSoup.find_all("a")
    cnnLinks=cnnSoup.find_all("a")
    foxnewsLinks=foxnewsSoup.find_all("a")
    #cbsnewsLinks=cbsnewsSoup.find_all("a")
    abcnewsLinks=abcnewsSoup.find_all("a")
    reutersnewsLinks=reutersnewsSoup.find_all("a")
    bbcnewsLinks=bbcnewsSoup.find_all("a")
    #yahoonewsLinks=yahoonewsSoup.find_all("a")
    #nbcnewsLinks=nbcnewsSoup.find_all("a")
    usatodaynewsLinks=usatodaynewsSoup.find_all("a")
    #huffingtonpostnewsLinks=huffingtonpostnewsSoup.find_all("a")
    timenewsLinks=timenewsSoup.find_all("a")
    #washingtonpostnewsLinks=washingtonpostnewsSoup.find_all("a")
    guardiannewsLinks=guardiannewsSoup.find_all("a")
    #wsjnewsLinks=wsjnewsSoup.find_all("a")
    #latimesnewsLinks=latimesnewsSoup.find_all("a")
    #nydailynewsLinks=nydailynewsSoup.find_all("a")
    #chicagotribunenewsLinks=chicagotribunenewsSoup.find_all("a")
    
    linkList=[nytimesLinks,cnnLinks,foxnewsLinks,abcnewsLinks,reutersnewsLinks,
            bbcnewsLinks,usatodaynewsLinks,timenewsLinks,guardiannewsLinks]

    entertainmentLinks=[]
    pointer=0
    
    listLength=len(linkList)
    
    
    for i in range(listLength):
        for link in linkList[pointer]:
            tempURL=link.get("href")
            
            if tempURL is None:
                continue
            if tempURL.startswith("http://www.nytimes.com/2016/"):
                dictionary={}
                dictionary['category']='Entertainment'
                dictionary['url']=tempURL
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    entertainmentLinks.append(dictionary)
            if tempURL.startswith("/entertainment/2016/10/"):
                foxFix='http://www.foxnews.com'
                foxResolve=foxFix+tempURL
                dictionary={}
                dictionary['category']='Entertainment'
                dictionary['url']=foxResolve
                dictionary['title']=link.get_text().replace('\n','')
                
                if dictionary['title'] and not dictionary['title'].isspace():
                    entertainmentLinks.append(dictionary)
            if tempURL.startswith("/2016/10/"):
                cnnFix='http://www.cnn.com'
                cnnResolved=cnnFix+tempURL
                dictionary={}
                dictionary['category']='Entertainment'
                dictionary['url']=cnnResolved
                dictionary['title']=link.get_text().replace('\n','')
                dictionary['title']=link.get_text().replace('\t','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    entertainmentLinks.append(dictionary)
            if tempURL.startswith("/Entertainment/"):
                abcFix='http://www.abcnews.go.com'
                abcResolved=abcFix+tempURL
                dictionary={}
                dictionary['category']='Entertainment'
                dictionary['url']=abcResolved
                dictionary['title']=link.get_text().replace('\n','')
                dictionary['title']=link.get_text().replace('\t','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    entertainmentLinks.append(dictionary)
            if tempURL.startswith("/article/") or tempURL.startswith("/video/2016/10/"):
                reutersFix='http://www.reuters.com'
                reutersResolved=reutersFix+tempURL
                dictionary={}
                dictionary['category']='Entertainment'
                dictionary['url']=reutersResolved
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    entertainmentLinks.append(dictionary)
            if tempURL.startswith("/news/entertainment-arts"):
                bbcFix='http://www.bbc.com'
                bbcResolved=bbcFix+tempURL
                dictionary={}
                dictionary['category']='Entertainment'
                dictionary['url']=bbcResolved
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    entertainmentLinks.append(dictionary)
            if tempURL.startswith("/pop-culture/"):
                nbcFix='http://www.nbcnews.com'
                nbcResolved=nbcFix+tempURL
                dictionary={}
                dictionary['category']='Entertainment'
                dictionary['url']=nbcResolved
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    entertainmentLinks.append(dictionary)
            if tempURL.startswith("/story/life/2016/10/"):
                usatodayFix='http://www.usatoday.com'
                usatodayResolved=usatodayFix+tempURL
                dictionary={}
                dictionary['category']='Entertainment'
                dictionary['url']=usatodayResolved
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    entertainmentLinks.append(dictionary)
            if tempURL.startswith("http://time.com/453") or tempURL.startswith("http://time.com/454"):
                dictionary={}
                dictionary['category']='Entertainment'
                dictionary['url']=tempURL
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    entertainmentLinks.append(dictionary)
            
            if tempURL.startswith("https://www.theguardian.com/tv-and-radio/2016/oct/") or tempURL.startswith("https://www.theguardian.com/music/2016/oct/") or tempURL.startswith("https://www.theguardian.com/books/2016/oct/") or tempURL.startswith("https://www.theguardian.com/culture/2016/oct/"):
                dictionary={}
                dictionary['category']='Entertainment'
                dictionary['url']=tempURL
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    entertainmentLinks.append(dictionary)
                    
        pointer+=1
            
    return entertainmentLinks

def getSports():
    
    nytimesURL="http://www.nytimes.com/section/sports"
    cnnURL="http://www.bleacherrepot.com"
    #foxnewsURL="http://www.foxnews.com/entertainment"
    #cbsnewsURL="http://www.cbsnews.com/politics"
    abcnewsURL="http://www.abcnews.go.com/Sports"
    reutersnewsURL="http://www.reuters.com/news/sports"
    #bbcnewsURL="http://www.bbc.com/sport"
    yahoonewsURL="https://www.yahoo.com/news/politics"
    nbcnewsURL="http://www.nbcsports.com/"
    usatodaynewsURL="http://www.usatoday.com/sports"
    #huffingtonpostnewsURL="http://www.huffingtonpost.com/section/business"
    timenewsURL="http://www.time.com/sports"
    #washingtonpostnewsURL="https://www.washingtonpost.com/world/"
    guardiannewsURL="https://www.theguardian.com/us/sport"
    #wsjnewsURL="http://www.wsj.com/news/business"
    #latimesnewsURL="http://www.latimes.com/politics"
    #nydailynewsURL="http://www.nydailynews.com/news/politics"
    #chicagotribunenewsURL="http://www.chicagotribune.com/business"
   
    r_nytimes=requests.get(nytimesURL)
    r_CNN=requests.get(cnnURL)
    #r_foxnews=requests.get(foxnewsURL)
    #r_cbsnews=requests.get(cbsnewsURL)
    r_abcnews=requests.get(abcnewsURL)
    r_reutersnews=requests.get(reutersnewsURL)
    #r_bbcnews=requests.get(bbcnewsURL)
    #r_yahoonews=requests.get(yahoonewsURL)
    r_nbcnews=requests.get(nbcnewsURL)
    r_usatodaynews=requests.get(usatodaynewsURL)
    #r_huffingtonpostnews=requests.get(huffingtonpostnewsURL)
    r_timenews=requests.get(timenewsURL)
    #r_washingtonpostnews=requests.get(washingtonpostnewsURL)
    r_guardiannews=requests.get(guardiannewsURL)
    #r_wsjnews=requests.get(wsjnewsURL)
    #r_latimesnews=requests.get(latimesnewsURL)
    #r_nydailynews=requests.get(nydailynewsURL)
    #r_chicagotribunenews=requests.get(chicagotribunenewsURL)
    
    nytimesSoup=BeautifulSoup(r_nytimes.content, "lxml")
    cnnSoup=BeautifulSoup(r_CNN.content, "lxml")
    #foxnewsSoup=BeautifulSoup(r_foxnews.content, "lxml")
    #cbsnewsSoup=BeautifulSoup(r_cbsnews.content, "lxml")
    abcnewsSoup=BeautifulSoup(r_abcnews.content, "lxml")
    reutersnewsSoup=BeautifulSoup(r_reutersnews.content, "lxml")
    #bbcnewsSoup=BeautifulSoup(r_bbcnews.content, "lxml")
    #yahoonewsSoup=BeautifulSoup(r_yahoonews.content, "lxml")
    nbcnewsSoup=BeautifulSoup(r_nbcnews.content, "lxml")
    usatodaynewsSoup=BeautifulSoup(r_usatodaynews.content, "lxml")
    #huffingtonpostnewsSoup=BeautifulSoup(r_huffingtonpostnews.content, "lxml")
    timenewsSoup=BeautifulSoup(r_timenews.content, "lxml")
    #washingtonpostnewsSoup=BeautifulSoup(r_washingtonpostnews.content, "lxml")
    guardiannewsSoup=BeautifulSoup(r_guardiannews.content, "lxml")
    #wsjnewsSoup=BeautifulSoup(r_wsjnews.content, "lxml")
    #latimesnewsSoup=BeautifulSoup(r_latimesnews.content, "lxml")
    #nydailynewsSoup=BeautifulSoup(r_nydailynews.content, "lxml")
    #chicagotribunenewsSoup=BeautifulSoup(r_chicagotribunenews.content, "lxml")
    
    nytimesLinks=nytimesSoup.find_all("a")
    cnnLinks=cnnSoup.find_all("a")
    #foxnewsLinks=foxnewsSoup.find_all("a")
    #cbsnewsLinks=cbsnewsSoup.find_all("a")
    abcnewsLinks=abcnewsSoup.find_all("a")
    reutersnewsLinks=reutersnewsSoup.find_all("a")
    #bbcnewsLinks=bbcnewsSoup.find_all("a")
    #yahoonewsLinks=yahoonewsSoup.find_all("a")
    nbcnewsLinks=nbcnewsSoup.find_all("a")
    usatodaynewsLinks=usatodaynewsSoup.find_all("a")
    #huffingtonpostnewsLinks=huffingtonpostnewsSoup.find_all("a")
    timenewsLinks=timenewsSoup.find_all("a")
    #washingtonpostnewsLinks=washingtonpostnewsSoup.find_all("a")
    guardiannewsLinks=guardiannewsSoup.find_all("a")
    #wsjnewsLinks=wsjnewsSoup.find_all("a")
    #latimesnewsLinks=latimesnewsSoup.find_all("a")
    #nydailynewsLinks=nydailynewsSoup.find_all("a")
    #chicagotribunenewsLinks=chicagotribunenewsSoup.find_all("a")
    
    linkList=[nytimesLinks,cnnLinks,abcnewsLinks,reutersnewsLinks,
            nbcnewsLinks,usatodaynewsLinks,timenewsLinks,guardiannewsLinks]

    sportsLinks=[]
    pointer=0
    
    listLength=len(linkList)
    
    
     
    for i in range(listLength):
        for link in linkList[pointer]:
            tempURL=link.get("href")
            
            if tempURL is None:
                continue
            if tempURL.startswith("http://www.nytimes.com/2016/"):
                dictionary={}
                dictionary['category']='Sports'
                dictionary['url']=tempURL
                dictionary['title']=link.get_text().replace('\n','')
                
                if dictionary['title'] and not dictionary['title'].isspace():
                    sportsLinks.append(dictionary)
            if tempURL.startswith("/articles/267"):
                cnnFix='http://www.bleacherreport.com'
                cnnResolved=cnnFix+tempURL
                dictionary={}
                dictionary['category']='Sports'
                dictionary['url']=cnnResolved
                dictionary['title']=link.get_text().replace('\n','')
                dictionary['title']=link.get_text().replace('\t','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    sportsLinks.append(dictionary)
            if tempURL.startswith("/Sports/wireStory/"):
                abcFix='http://www.abcnews.go.com'
                abcResolved=abcFix+tempURL
                dictionary={}
                dictionary['category']='Sports'
                dictionary['url']=abcResolved
                dictionary['title']=link.get_text().replace('\n','')
                dictionary['title']=link.get_text().replace('\t','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    sportsLinks.append(dictionary)
            if tempURL.startswith("/article/"):
                reutersFix='http://www.reuters.com'
                reutersResolved=reutersFix+tempURL
                dictionary={}
                dictionary['category']='Sports'
                dictionary['url']=reutersResolved
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    sportsLinks.append(dictionary)
            if tempURL.startswith("/news/entertainment-arts"):
                bbcFix='http://www.bbc.com'
                bbcResolved=bbcFix+tempURL
                dictionary={}
                dictionary['category']='Sports'
                dictionary['url']=bbcResolved
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    sportsLinks.append(dictionary)
            if tempURL.startswith("http://nhl.nbcsports.com/2016/10/") or tempURL.startswith("http://mlb.nbcsports.com/2016/10/") or tempURL.startswith("http://nascar.nbcsports.com/2016/10/") or tempURL.startswith("http://nhl.nbcsports.com/2016/10/") or tempURL.startswith("http://soccer.nbcsports.com/2016/10/") or tempURL.startswith("http://nba.nbcsports.com/2016/10/"):
                nbcFix='http://www.nbcsports.com'
                nbcResolved=nbcFix+tempURL
                dictionary={}
                dictionary['category']='Sports'
                dictionary['url']=nbcResolved
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    sportsLinks.append(dictionary)
            if tempURL.startswith("/story/sports/mlb/2016/10/") or tempURL.startswith("/story/sports/ncaaf/2016/10/") or tempURL.startswith("/story/sports/nfl/2016/10/") or tempURL.startswith("/story/sports/nba/2016/10/") or tempURL.startswith("/story/sports/nascar/2016/10/"):
                usatodayFix='http://www.usatoday.com'
                usatodayResolved=usatodayFix+tempURL
                dictionary={}
                dictionary['category']='Sports'
                dictionary['url']=usatodayResolved
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    sportsLinks.append(dictionary)
            if tempURL.startswith("http://time.com/453") or tempURL.startswith("http://time.com/454"):
                dictionary={}
                dictionary['category']='Sports'
                dictionary['url']=tempURL
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    sportsLinks.append(dictionary)
            
            if tempURL.startswith("https://www.theguardian.com/sport/2016/oct/"):
                dictionary={}
                dictionary['category']='Sports'
                dictionary['url']=tempURL
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    sportsLinks.append(dictionary)
                    
        pointer+=1
            
    return sportsLinks
   
def getTech():
    
    nytimesURL="http://www.nytimes.com/pages/technology"
    cnnURL="http://www.money.cnn.com/technology"
    foxnewsURL="http://www.foxnews.com/tech"
    #cbsnewsURL="http://www.cbsnews.com/politics"
    abcnewsURL="http://www.abcnews.go.com/Technology"
    reutersnewsURL="http://www.reuters.com/news/technology"
    bbcnewsURL="http://www.bbc.com/news/technology"
    #yahoonewsURL="https://www.yahoo.com/news/politics"
    #nbcnewsURL="http://www.nbcnews.com/tech"
    usatodaynewsURL="http://www.usatoday.com/tech"
    #huffingtonpostnewsURL="http://www.huffingtonpost.com/section/business"
    timenewsURL="http://www.time.com/tech"
    #washingtonpostnewsURL="https://www.washingtonpost.com/world/"
    guardiannewsURL="https://www.theguardian.com/us/technology"
    #wsjnewsURL="http://www.wsj.com/news/business"
    #latimesnewsURL="http://www.latimes.com/politics"
    #nydailynewsURL="http://www.nydailynews.com/news/politics"
    #chicagotribunenewsURL="http://www.chicagotribune.com/business"
   
    r_nytimes=requests.get(nytimesURL)
    r_CNN=requests.get(cnnURL)
    r_foxnews=requests.get(foxnewsURL)
    #r_cbsnews=requests.get(cbsnewsURL)
    r_abcnews=requests.get(abcnewsURL)
    r_reutersnews=requests.get(reutersnewsURL)
    r_bbcnews=requests.get(bbcnewsURL)
    #r_yahoonews=requests.get(yahoonewsURL)
    #r_nbcnews=requests.get(nbcnewsURL)
    r_usatodaynews=requests.get(usatodaynewsURL)
    #r_huffingtonpostnews=requests.get(huffingtonpostnewsURL)
    r_timenews=requests.get(timenewsURL)
    #r_washingtonpostnews=requests.get(washingtonpostnewsURL)
    r_guardiannews=requests.get(guardiannewsURL)
    #r_wsjnews=requests.get(wsjnewsURL)
    #r_latimesnews=requests.get(latimesnewsURL)
    #r_nydailynews=requests.get(nydailynewsURL)
    #r_chicagotribunenews=requests.get(chicagotribunenewsURL)
    
    nytimesSoup=BeautifulSoup(r_nytimes.content, "lxml")
    cnnSoup=BeautifulSoup(r_CNN.content, "lxml")
    foxnewsSoup=BeautifulSoup(r_foxnews.content, "lxml")
    #cbsnewsSoup=BeautifulSoup(r_cbsnews.content, "lxml")
    abcnewsSoup=BeautifulSoup(r_abcnews.content, "lxml")
    reutersnewsSoup=BeautifulSoup(r_reutersnews.content, "lxml")
    bbcnewsSoup=BeautifulSoup(r_bbcnews.content, "lxml")
    #yahoonewsSoup=BeautifulSoup(r_yahoonews.content, "lxml")
    #nbcnewsSoup=BeautifulSoup(r_nbcnews.content, "lxml")
    usatodaynewsSoup=BeautifulSoup(r_usatodaynews.content, "lxml")
    #huffingtonpostnewsSoup=BeautifulSoup(r_huffingtonpostnews.content, "lxml")
    timenewsSoup=BeautifulSoup(r_timenews.content, "lxml")
    #washingtonpostnewsSoup=BeautifulSoup(r_washingtonpostnews.content, "lxml")
    guardiannewsSoup=BeautifulSoup(r_guardiannews.content, "lxml")
    #wsjnewsSoup=BeautifulSoup(r_wsjnews.content, "lxml")
    #latimesnewsSoup=BeautifulSoup(r_latimesnews.content, "lxml")
    #nydailynewsSoup=BeautifulSoup(r_nydailynews.content, "lxml")
    #chicagotribunenewsSoup=BeautifulSoup(r_chicagotribunenews.content, "lxml")
    
    nytimesLinks=nytimesSoup.find_all("a")
    cnnLinks=cnnSoup.find_all("a")
    foxnewsLinks=foxnewsSoup.find_all("a")
    #cbsnewsLinks=cbsnewsSoup.find_all("a")
    abcnewsLinks=abcnewsSoup.find_all("a")
    reutersnewsLinks=reutersnewsSoup.find_all("a")
    bbcnewsLinks=bbcnewsSoup.find_all("a")
    #yahoonewsLinks=yahoonewsSoup.find_all("a")
    #nbcnewsLinks=nbcnewsSoup.find_all("a")
    usatodaynewsLinks=usatodaynewsSoup.find_all("a")
    #huffingtonpostnewsLinks=huffingtonpostnewsSoup.find_all("a")
    timenewsLinks=timenewsSoup.find_all("a")
    #washingtonpostnewsLinks=washingtonpostnewsSoup.find_all("a")
    guardiannewsLinks=guardiannewsSoup.find_all("a")
    #wsjnewsLinks=wsjnewsSoup.find_all("a")
    #latimesnewsLinks=latimesnewsSoup.find_all("a")
    #nydailynewsLinks=nydailynewsSoup.find_all("a")
    #chicagotribunenewsLinks=chicagotribunenewsSoup.find_all("a")
    
    linkList=[nytimesLinks,cnnLinks,foxnewsLinks,abcnewsLinks,reutersnewsLinks,
            bbcnewsLinks,usatodaynewsLinks,timenewsLinks,guardiannewsLinks]

    techLinks=[]
    pointer=0
    
    listLength=len(linkList)
    
    
    for i in range(listLength):
        for link in linkList[pointer]:
            tempURL=link.get("href")
            
            if tempURL is None:
                continue
            if tempURL.startswith("http://www.nytimes.com/2016/"):
                dictionary={}
                dictionary['category']='Technology'
                dictionary['url']=tempURL
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    techLinks.append(dictionary)
            if tempURL.startswith("http://www.foxnews.com/tech/2016/10/"):
                foxFix='http://www.foxnews.com'
                foxResolve=foxFix+tempURL
                dictionary={}
                dictionary['category']='Technology'
                dictionary['url']=foxResolve
                dictionary['title']=link.get_text().replace('\n','')
                
                if dictionary['title'] and not dictionary['title'].isspace():
                    techLinks.append(dictionary)
            if tempURL.startswith("/2016/10/"):
                cnnFix='http://www.money.cnn.com'
                cnnResolved=cnnFix+tempURL
                dictionary={}
                dictionary['category']='Technology'
                dictionary['url']=cnnResolved
                dictionary['title']=link.get_text().replace('\n','')
                dictionary['title']=link.get_text().replace('\t','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    techLinks.append(dictionary)
            if tempURL.startswith("/Technology/wireStory/"):
                abcFix='http://www.abcnews.go.com'
                abcResolved=abcFix+tempURL
                dictionary={}
                dictionary['category']='Technology'
                dictionary['url']=abcResolved
                dictionary['title']=link.get_text().replace('\n','')
                dictionary['title']=link.get_text().replace('\t','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    techLinks.append(dictionary)
            if tempURL.startswith("/article/") or tempURL.startswith("/video/2016/10/"):
                reutersFix='http://www.reuters.com'
                reutersResolved=reutersFix+tempURL
                dictionary={}
                dictionary['category']='Technology'
                dictionary['url']=reutersResolved
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    techLinks.append(dictionary)
            if tempURL.startswith("/news/technology-"):
                bbcFix='http://www.bbc.com'
                bbcResolved=bbcFix+tempURL
                dictionary={}
                dictionary['category']='Technology'
                dictionary['url']=bbcResolved
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    techLinks.append(dictionary)
            if tempURL.startswith("/story/tech/2016/10/") or tempURL.startswith("/story/tech/news/2016/10/"):
            
                usatodayFix='http://www.usatoday.com'
                usatodayResolved=usatodayFix+tempURL
                dictionary={}
                dictionary['category']='Technology'
                dictionary['url']=usatodayResolved
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    techLinks.append(dictionary)
            if tempURL.startswith("http://time.com/453") or tempURL.startswith("http://time.com/454"):
                dictionary={}
                dictionary['category']='Technology'
                dictionary['url']=tempURL
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    techLinks.append(dictionary)
            
            if tempURL.startswith("https://www.theguardian.com/technology/2016/oct/"):
                dictionary={}
                dictionary['category']='Technology'
                dictionary['url']=tempURL
                dictionary['title']=link.get_text().replace('\n','')
                if dictionary['title'] and not dictionary['title'].isspace():
                    techLinks.append(dictionary)
                    
        pointer+=1
            
    return techLinks

getPolitics()
getBusiness()
getMemes()
getWorldNews()
getUSNews()
getEntertainment()
getSports()
getTech()

