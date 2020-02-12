import requests,bs4
#パース対象サイトをここに追加
targetSite =['AtCoder']

class GetHtml:
    """
    GetHtml as text
    """
    # 検索サイトのURL登録
    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0",}
        self.urls = {
            targetSite[0]:'https://atcoder.jp/home?lang=en'
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

        contestnamePoint = {}
        for site in targetSite[:1]:
            try:
                # 会社評価ポイントの取得
                # parseDate = textList[site].find(dateTag[site][0], class_=dateTag[site][1])
                # cpoint = parseDate.getText().replace('\n', '').replace(' ', '')
                # #会社名の取得
                # parseCname =  textList[site].find(nameTag[site][0], class_=nameTag[site][1])
                # cname = parseCname.getText().replace('\n','').replace(' ', '')
                parseTable = textList[site].find(table[site][0], id=table[site][1])
                cTable = parseTable.getText().replace('\n', '').replace(' ', '')

            # 検索結果が無かった場合の処理
            except AttributeError:
                contestnamePoint.setdefault(site, ['None','None'])

            # 検索結果が有った場合の処理
            else:
                contestnamePoint.setdefault(site, [cTable]) #,cname, cpoint

        return contestnamePoint

# print(GetHtml().getText())
print(ParseHtml().parseNamePoint(GetHtml().getText()))
