NAME = 'TVO'
TITLE  = 'TVO'
PREFIX = '/video/tvo'
ART = 'art-default.jpg'
THUMB = 'icon-default.jpg'
RE_URL = Regex('((([A-Za-z]{3,9}:(?:\/\/)?)(?:[\-;:&=\+\$,\w]+@)?[A-Za-z0-9\.\-]+|(?:www\.|[\-;:&=\+\$,\w]+@)[A-Za-z0-9\.\-]+)((?:\/[\+~%\/\.\w\-_]*)?\??(?:[\-\+=&;%@\.\w_]*)#?(?:[\.\!\/\\\w]*))?)')
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

    oc.add(DirectoryObject(key=Callback(DocsSeriesMenu, title='Documentaries & Series'), title='Documentaries & Series'))
    oc.add(DirectoryObject(key=Callback(ShowTheAgenda, title='The Agenda', pass_url='http://theagenda.tvo.org/past-episodes', pass_thumb='https://pbs.twimg.com/profile_images/468804042336907265/K_RZ4BOp.jpeg'), title='The Agenda', thumb='https://pbs.twimg.com/profile_images/468804042336907265/K_RZ4BOp.jpeg'))
    oc.add(DirectoryObject(key=Callback(YTVids, title='TVO Parents', pass_url='https://www.youtube.com/user/tvoparents/videos', pass_thumb='https://pbs.twimg.com/profile_images/2028493104/TVO_Facebook_TVOParents_Profile.jpg'), title='TVO Parents', thumb='https://pbs.twimg.com/profile_images/2028493104/TVO_Facebook_TVOParents_Profile.jpg'))
    oc.add(DirectoryObject(key=Callback(YTVids, title='Big Ideas', pass_url='https://www.youtube.com/user/TVOBigIdeas/videos', pass_thumb='https://pbs.twimg.com/profile_images/372784543/big-ideas-logo_400x400.jpg'), title='Big Ideas', thumb='https://pbs.twimg.com/profile_images/372784543/big-ideas-logo_400x400.jpg'))
    oc.add(DirectoryObject(key=Callback(YTVids, title='Allan Gregg In Conversation', pass_url='https://www.youtube.com/user/AllanGregg/videos', pass_thumb='http://i.ytimg.com/i/XvuG5Dm12QKzvkA-3SR_LQ/mq1.jpg?v=520a776e'), title='Allan Gregg In Conversation', thumb='http://i.ytimg.com/i/XvuG5Dm12QKzvkA-3SR_LQ/mq1.jpg?v=520a776e'))
    oc.add(DirectoryObject(key=Callback(YTVids, title='Saturday Night at the Movies', pass_url='https://www.youtube.com/user/TVOsnam/videos', pass_thumb='http://i.ytimg.com/i/3V0davW9bG_M2ykgjHvPsA/mq1.jpg?v=520a77fa'), title='Saturday Night at the Movies', thumb='http://i.ytimg.com/i/3V0davW9bG_M2ykgjHvPsA/mq1.jpg?v=520a77fa'))

    return oc


###################################################################################################
@route(PREFIX + '/docsseriesmenu')
def DocsSeriesMenu(title):

    oc = ObjectContainer(title2=TITLE)
    oc.add(DirectoryObject(key=Callback(ShowPrograms, title='A', pass_url='http://tvo.org/programs-a-z/A'), title='A'))
    oc.add(DirectoryObject(key=Callback(ShowPrograms, title='B', pass_url='http://tvo.org/programs-a-z/B'), title='B'))
    oc.add(DirectoryObject(key=Callback(ShowPrograms, title='C', pass_url='http://tvo.org/programs-a-z/C'), title='C'))
    oc.add(DirectoryObject(key=Callback(ShowPrograms, title='D', pass_url='http://tvo.org/programs-a-z/D'), title='D'))
    oc.add(DirectoryObject(key=Callback(ShowPrograms, title='E', pass_url='http://tvo.org/programs-a-z/E'), title='E'))
    oc.add(DirectoryObject(key=Callback(ShowPrograms, title='F', pass_url='http://tvo.org/programs-a-z/F'), title='F'))
    oc.add(DirectoryObject(key=Callback(ShowPrograms, title='G', pass_url='http://tvo.org/programs-a-z/G'), title='G'))
    oc.add(DirectoryObject(key=Callback(ShowPrograms, title='H', pass_url='http://tvo.org/programs-a-z/H'), title='H'))
    oc.add(DirectoryObject(key=Callback(ShowPrograms, title='I', pass_url='http://tvo.org/programs-a-z/I'), title='I'))
    oc.add(DirectoryObject(key=Callback(ShowPrograms, title='J', pass_url='http://tvo.org/programs-a-z/J'), title='J'))
    oc.add(DirectoryObject(key=Callback(ShowPrograms, title='K', pass_url='http://tvo.org/programs-a-z/K'), title='K'))
    oc.add(DirectoryObject(key=Callback(ShowPrograms, title='L', pass_url='http://tvo.org/programs-a-z/L'), title='L'))
    oc.add(DirectoryObject(key=Callback(ShowPrograms, title='M', pass_url='http://tvo.org/programs-a-z/M'), title='M'))
    oc.add(DirectoryObject(key=Callback(ShowPrograms, title='N', pass_url='http://tvo.org/programs-a-z/N'), title='N'))
    oc.add(DirectoryObject(key=Callback(ShowPrograms, title='O', pass_url='http://tvo.org/programs-a-z/O'), title='O'))
    oc.add(DirectoryObject(key=Callback(ShowPrograms, title='P', pass_url='http://tvo.org/programs-a-z/P'), title='P'))
    oc.add(DirectoryObject(key=Callback(ShowPrograms, title='Q', pass_url='http://tvo.org/programs-a-z/Q'), title='Q'))
    oc.add(DirectoryObject(key=Callback(ShowPrograms, title='R', pass_url='http://tvo.org/programs-a-z/R'), title='R'))
    oc.add(DirectoryObject(key=Callback(ShowPrograms, title='S', pass_url='http://tvo.org/programs-a-z/S'), title='S'))
    oc.add(DirectoryObject(key=Callback(ShowPrograms, title='T', pass_url='http://tvo.org/programs-a-z/T'), title='T'))
    oc.add(DirectoryObject(key=Callback(ShowPrograms, title='U', pass_url='http://tvo.org/programs-a-z/U'), title='U'))
    oc.add(DirectoryObject(key=Callback(ShowPrograms, title='V', pass_url='http://tvo.org/programs-a-z/V'), title='V'))
    oc.add(DirectoryObject(key=Callback(ShowPrograms, title='W', pass_url='http://tvo.org/programs-a-z/W'), title='W'))
    oc.add(DirectoryObject(key=Callback(ShowPrograms, title='X', pass_url='http://tvo.org/programs-a-z/X'), title='X'))
    oc.add(DirectoryObject(key=Callback(ShowPrograms, title='Y', pass_url='http://tvo.org/programs-a-z/Y'), title='Y'))
    oc.add(DirectoryObject(key=Callback(ShowPrograms, title='Z', pass_url='http://tvo.org/programs-a-z/Z'), title='Z'))

    return oc


###################################################################################################
@route(PREFIX + '/showprograms')
def ShowPrograms(title, pass_url):
    oc = ObjectContainer(title2=title)
    pg_content = HTTP.Request(pass_url)
    pg_page = HTML.ElementFromString(pg_content)
    for item in pg_page.xpath('//div[contains(@class, "views-row views-row-")]'):
        showTitle = item.xpath('./a[@class="ms-heading"]')[0].text
        showThumb = item.xpath('.//img/@src')[0]
        showSummary = item.xpath('.//div[@class="views-field-field-description-value"]/p/text()')[0]
        showURL = item.xpath('.//span[@class="field-content ms-detail-links-program"]/a')[0].get('href')
        isSeries = 3 #not sure why this can't be set to 0
        nodeExists = item.xpath('boolean(.//span[@class="field-content ms-detail-links-video"]/a)');
        if nodeExists == 1:
            vidURL = item.xpath('.//span[@class="field-content ms-detail-links-video"]/a')[0].get('href')
            isSeries = 'video-landing' in vidURL

        if isSeries == 1:
            if not showTitle.startswith(' <Any>'):
                oc.add(DirectoryObject(key=Callback(ShowEpisodes, title=showTitle, pass_url=showURL, pass_thumb=showThumb), title=showTitle, summary=showSummary, thumb=showThumb))

        if isSeries == 0:
            if not showTitle.startswith(' <Any>'):
                if 'bcid' in vidURL:
                    oc.add(DirectoryObject(key=Callback(PlayEpisodes, title=showTitle, pass_url=vidURL), title=showTitle, summary=showSummary, thumb=showThumb))

        vidURL = ''

    return oc


###################################################################################################
@route(PREFIX + '/showepisodes')
def ShowEpisodes(title, pass_url, pass_thumb):

    oc = ObjectContainer(title2=title)
    pageElement = HTML.ElementFromURL(pass_url)

    for item in pageElement.xpath('//li[contains(@class, "views-row views-row")]'):
        try:
            epURL = item.xpath('.//a[contains(@class, "watch-video")]')[0].get('href')
            epTitle = item.xpath('./span[contains(@class, "ep-title")]')[0].text
            epSummary = item.xpath('.//p[contains(@class, "ep-desc")]')[0].text
            oc.add(DirectoryObject(key=Callback(PlayEpisodes, title=epTitle, pass_url=epURL),title=epTitle, summary=epSummary, thumb=pass_thumb))
            Log(epTitle)
            Log(epURL)
        except:
            continue

    return oc


###################################################################################################
@route(PREFIX + '/playepisodes')
def PlayEpisodes(title, pass_url):

    oc = ObjectContainer(title2=title)
    epElement = HTML.ElementFromURL(pass_url)

    epTitle = epElement.xpath('//h1[@class="title"]')[0].text
    epSummary = epElement.xpath('//head//meta[@property="og:description"]')[0].get('content')
    epThumb = epElement.xpath('//head//meta[@property="og:image"]')[0].get('content')
    PlayerID = epElement.xpath('//param[contains(@name, "playerID")]')[0].get('value')
    PlayerKey = epElement.xpath('//param[contains(@name, "playerKey")]')[0].get('value')
    VideoID = pass_url.replace('http://tvo.org/bcid/','')
    VideoID = VideoID.replace('http://theagenda.tvo.org/bcid/','')
    vidURL = 'http://c.brightcove.com/services/viewer/federated_f9?isVid=true&isUI=true&videoId='+VideoID+'&playerID='+PlayerID+'&playerKey='+PlayerKey+'&domain=embed&dynamicStreaming=true'

    oc.add(VideoClipObject(title = epTitle, url = vidURL, summary = epSummary, thumb = epThumb))

    return oc


###################################################################################################
#                      The Agenda
###################################################################################################

###################################################################################################
@route(PREFIX + '/showtheagenda')
def ShowTheAgenda(title, pass_url, pass_thumb):
    oc = ObjectContainer(title2=title)
    pg_content = HTTP.Request(pass_url)
    pg_page = HTML.ElementFromString(pg_content)
    for item in pg_page.xpath('//div[contains(@class, "views-row views-row-")]'):
        showTitle = item.xpath('.//span[@class="date-display-single"]')[0].text
        showSummary = item.xpath('.//div[@class="past-episode-desc"]/p')[0].text
        showURL = item.xpath('.//div[@class="past-episode-link"]/a')[0].get('href')
        oc.add(DirectoryObject(key=Callback(ShowAgendaSegments, title=showTitle, pass_url=showURL, pass_thumb=pass_thumb), title=showTitle, summary=showSummary, thumb=pass_thumb))

    return oc


###################################################################################################
@route(PREFIX + '/showagendasegments')
def ShowAgendaSegments(title, pass_url, pass_thumb):

    oc = ObjectContainer(title2=title)
    pageElement = HTML.ElementFromURL(pass_url)

    for item in pageElement.xpath('//div[@class="episode-detail-segment"]'):
        epURL = item.xpath('.//div[@class="episode-detail-segment-watch-video"]/a')[0].get('href')
        epTitle = item.xpath('.//h4')[0].text
        epSummary = item.xpath('.//div[contains(@class, "episode-detail-segment-info")]/p')[0].text
        if 'bcid' in epURL:
            oc.add(DirectoryObject(key=Callback(PlayEpisodes, title=epTitle, pass_url=epURL),title=epTitle, summary=epSummary, thumb=pass_thumb))

    return oc


###################################################################################################
#                      YouTube Shows
###################################################################################################

###################################################################################################
@route(PREFIX + '/ytvids')
def YTVids(title, pass_url, pass_thumb):
    oc = ObjectContainer(title2=title)
    pgElement = HTML.ElementFromURL(pass_url)
    for item in pgElement.xpath('//li[@class="channels-content-item yt-shelf-grid-item"]'):
        ytID = item.xpath('.//div/@data-context-item-id')[0]
        vidTitle = item.xpath('.//h3/a')[0].text
        vidThumb = 'http://i.ytimg.com/vi/'+ytID+'/mqdefault.jpg'
        vidSummary = vidTitle
        vidURL = 'https://www.youtube.com/watch?v='+ytID
        oc.add(VideoClipObject(title = vidTitle, url = vidURL, thumb = vidThumb))

    return oc
