NAME = 'TVO'
TITLE  = 'TVO'
PREFIX = '/video/tvo'
ART   = "art-default.jpg"
THUMB = 'icon-default.png'
HTTP_USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/536.26.17 (KHTML, like Gecko) Version/6.0.2 Safari/536.26.17"

###################################################################################################
def Start():
    ObjectContainer.title1 = TITLE
    ObjectContainer.art   = R(ART)

    DirectoryObject.thumb = R(THUMB)
    DirectoryObject.art   = R(ART)
    VideoClipObject.thumb = R(ICON)
    VideoClipObject.art   = R(ART)

    HTTP.Headers['User-agent'] = HTTP_USER_AGENT

###################################################################################################
@handler(PREFIX, TITLE, thumb = THUMB, art = ART)
def MainMenu():

    oc = ObjectContainer(title1=TITLE)

    oc.add(DirectoryObject(key=Callback(ShowPrograms, title='Current Programs', pass_url='http://ww3.tvo.org/video?quicktabs_3=0'), title='Current Programs'))
    oc.add(DirectoryObject(key=Callback(ShowPrograms, title='Drams', pass_url='http://ww3.tvo.org/video?quicktabs_3=3'), title='Dramas'))
    oc.add(DirectoryObject(key=Callback(ShowPrograms, title='Archives', pass_url='http://ww3.tvo.org/video?quicktabs_3=4'), title='Archives'))
    oc.add(DirectoryObject(key=Callback(ShowDocs, title='Documentaries', pass_url='http://ww3.tvo.org/video?quicktabs_3=1', pgnum = 0), title='Documentaries'))
    oc.add(DirectoryObject(key=Callback(ShowPrograms, title='Documentary Series', pass_url='http://ww3.tvo.org/video?quicktabs_3=2'), title='Documentary Series'))
    oc.add(DirectoryObject(key=Callback(ShowDocs, title='Coming Soon', pass_url='http://ww3.tvo.org/video?quicktabs_3=6', pgnum = 0), title='Coming Soon'))

    return oc


###################################################################################################
@route(PREFIX + '/showprograms')
def ShowPrograms(title, pass_url):

    oc = ObjectContainer(title2=title)
    pageElement = HTML.ElementFromURL(pass_url)
    for item in pageElement.xpath('//div[contains(@id, "edit-field-web-master-series-nid")]'):
        showIDFull = item.xpath('./input[@type="radio"]')[0].get('value')
        showID = showIDFull.replace('<span></span>','')
        showTitle = item.xpath('./label[@class="option"]')[0].text
        showURL = 'http://ww3.tvo.org/program/'+showID+'/'
        if not showTitle.startswith(' <Any>'):
            oc.add(DirectoryObject(key=Callback(PlayPrograms, title=showTitle, pass_url=showURL, showpg=0), title=showTitle, summary='Add summary'))

    return oc


###################################################################################################
@route(PREFIX + '/playprograms')
def PlayPrograms(title, pass_url, showpg):

    oc = ObjectContainer(title2=title)
    pageElement = HTML.ElementFromURL(pass_url)

    for epies in pageElement.xpath('//a[contains(@class, "watch-video")]'):
        epURL = epies.xpath('./@href')[0]

        epElement = HTML.ElementFromURL(epURL)
        epTitle = epElement.xpath('//h1[@class="title"]')[0].text
        epSummary = epElement.xpath('//head//meta[@property="og:description"]')[0].get('content')
        epThumb = epElement.xpath('//head//meta[@property="og:image"]')[0].get('content')
        PlayerID = epElement.xpath('//param[contains(@name, "playerID")]')[0].get('value')
        PlayerKey = epElement.xpath('//param[contains(@name, "playerKey")]')[0].get('value')
        VideoID = epURL.replace('http://ww3.tvo.org/bcid/','')
        vidURL = 'http://c.brightcove.com/services/viewer/federated_f9?isVid=1&isUI=1&videoId='+VideoID+'&playerID='+PlayerID+'&playerKey='+PlayerKey+'&domain=embed&dynamicStreaming=true'

        oc.add(VideoClipObject(title = epTitle, url = vidURL, summary = epSummary, thumb = epThumb))

    return oc

###################################################################################################
@route(PREFIX + '/showdocs')
def ShowDocs(title, pass_url, pgnum):

    oc = ObjectContainer(title2=title)
    pageElement = HTML.ElementFromURL(pass_url)
    
    for item in pageElement.xpath('//div[contains(@class, "video-landing-this-means-war")]'):
        docTitle = 'testing'
        docURL = item.xpath('./a[contains(@class, "video-landing-item-anchor")]')[0].get('href')
        docElement = HTML.ElementFromURL(docURL)
        docTitle = docElement.xpath('//h1[@class="title"]')[0].text
        docSummary = docElement.xpath('//head//meta[@property="og:description"]')[0].get('content')
        docThumb = docElement.xpath('//head//meta[@property="og:image"]')[0].get('content')
        VideoID = docURL.replace('http://ww3.tvo.org/bcid/','')
        PlayerID = docElement.xpath('//param[contains(@name, "playerID")]')[0].get('value')
        PlayerKey = docElement.xpath('//param[contains(@name, "playerKey")]')[0].get('value')
        vidURL = 'http://c.brightcove.com/services/viewer/federated_f9?isVid=1&isUI=1&videoId='+VideoID+'&playerID='+PlayerID+'&playerKey='+PlayerKey+'&domain=embed&dynamicStreaming=true'

        oc.add(VideoClipObject(title = docTitle, url = vidURL, summary = docSummary, thumb = docThumb))

    return oc
