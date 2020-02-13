import requests,bs4,re,datetime
#パース対象サイトをここに追加
targetSite =['AtCoder']

class GetHtml:
    """
    GetHtml as text
    """
    # 検索サイトのURL登録
    def __init__(self):
        self.headers = {"User-Agent": "Google Chrome/Version 80.0.3987.87 (Official Build) (64-bit)",}
        self.urls = {
            targetSite[0]:'https://atcoder.jp/contests/'
        }

    # 対象ページのHtml全文を取得
    def getText(self):
        textList = {}
        for url in self.urls:
            res = requests.get(self.urls[url], headers=self.headers)
            text = bs4.BeautifulSoup(res.text, "html.parser")
            textList.setdefault(url, text)
        return textList

class ParseHtml:
    """
    ParseHtmlHtml to get required values
    """
    # 企業名と評価ポイントの取得
    def parseNamePoint(self, textList):
        #パース用のタグ登録
        # contest_table = 'contest-table-upcoming > div > table'

        table = {
            targetSite[0]:["div", "contest-table-upcoming"]
        }
        # dateTag =  {
        #     targetSite[0]:["h3", "fs-18 lh-1o3 p-r"] #[tag, class]
        #     # targetSite[1]:["h2", "companyName"],
        # }
        # nameTag = {
        #     targetSite[0]:["p", "totalEvaluation_item fs-15 fw-b"]
        #     # targetSite[1]:["span", "point"],
        # }

        contest_name = []
        time = []
        str_time = []
        contest_name_time = ''

        for site in targetSite[:1]:
            try:
                # 会社評価ポイントの取得
                # parseDate = textList[site].find(dateTag[site][0], class_=dateTag[site][1])
                # cpoint = parseDate.getText().replace('\n', '').replace(' ', '')
                # #会社名の取得
                # parseCname =  textList[site].find(nameTag[site][0], class_=nameTag[site][1])
                # cname = parseCname.getText().replace('\n','').replace(' ', '')
                parseTable = textList[site].find(table[site][0], id=table[site][1])
                time = re.findall('\d{4}-\d{2}-\d{2} \d+:\d+:\d+',str(parseTable))
                # time = parseTable.findAll('time')
                # a_tag = parseTable.findAll('a')
                # link_element = a_tag['href']
                # for i in range(len(time)):
                #     href = 	link_element['href']
                # contest_name = parseTable.findAll('a')
                contest_name = re.findall('contests[\w\d/%#$&?()~_.=+-]+',str(parseTable))
                # contest_name_str = contest_name.string

                cTable = parseTable.getText().replace('\n','').split()
                # parse_contest = textList[site].find(contest_table)
                # cContest = parse_contest.getText().split('\n')


                print(parseTable,'\n')
                print(time)
                print(contest_name)

            # 検索結果が無かった場合の処理
            except AttributeError:
                contest_name_time = None,None


            # 検索結果が有った場合の処理
        for i in range(len(time)):
            str_time.append(datetime.datetime.strptime(time[i], '%Y-%m-%d %H:%M:%S'))
            print(str_time)
            contest_name_time += contest_name[i] + ':\n' + time[i] +'(JPtime +0900)\n\n'

        return contest_name_time

# print(GetHtml().getText())
print(ParseHtml().parseNamePoint(GetHtml().getText()))
