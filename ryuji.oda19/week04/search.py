import requests,bs4,re,datetime
#パース対象サイトをここに追加
targetSite =['AtCoder']

class GetHtml:
    """
    GetHtml as text
    """
    # 検索サイトのURL登録 #searching target
    def __init__(self):
        self.headers = {"User-Agent": "Google Chrome/Version 80.0.3987.87 (Official Build) (64-bit)",}
        self.urls = {
            targetSite[0]:'https://atcoder.jp/contests/'
        }

    # 対象ページのHtml全文を取得 #get whole html
    def getText(self):
        textList = {}
        for url in self.urls:
            res = requests.get(self.urls[url], headers=self.headers)
            text = bs4.BeautifulSoup(res.text, "html.parser") #enable to select html tag and attribute by beautifulsoup
            textList.setdefault(url, text) #store whole html in variable
        return textList

class ParseHtml:
    """
    ParseHtmlHtml to get required values
    """
    # 企業名と評価ポイントの取得
    def parseName_Date(self, textList):
        #パース用のタグ登録
        table = {
            targetSite[0]:["div", "contest-table-upcoming"]
        }

        contest_name = []
        time = []
        str_time = []
        modified_2H = []
        contest_name_time = []

        for site in targetSite[:1]:
            try:
                # parse name and time
                parseTable = textList[site].find(table[site][0], id=table[site][1])
                time = re.findall('\d{4}-\d{2}-\d{2} \d+:\d+:\d+',str(parseTable))#from <time>
                contest_name = re.findall('contests[\w\d/%#$&?()~_.=+-]+',str(parseTable))#from <a href=...>

            # 検索結果が無かった場合の処理 #if nothing find in table
            except AttributeError:
                contest_name_time = None,None


            # if find elements
        for i in range(len(time)):
            str_time.append(datetime.datetime.strptime(time[i], '%Y-%m-%d %H:%M:%S'))
            # print(str_time)
            modified_2H.append(str_time[i] - datetime.timedelta(hours=2))
            # contest_name_time += contest_name[i] + ':\n' + str(modified_2H[i]) +'(KHtime +0700)\n\n'
            contest_name_time.append(contest_name[i] + ' ' + str(modified_2H[i]) + '(KHtime +0700)')

        # print(modified_2H)
        return contest_name_time

# print(GetHtml().getText())
print(ParseHtml().parseName_Date(GetHtml().getText()))
