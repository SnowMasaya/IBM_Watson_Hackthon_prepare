
class ModelSearchList:
    def __init__(self):
        self.search_hash_list = [ 
                            "#社畜",
                            "#会長",
                            "#社長",
                            "#専務",
                            "#常務",
                            "#監査役",
                            "#事業部長",
                            "#部長",
                            "#次長",
                            "#課長",
                            "#係長",
                            "#主任",
                            "#リーダー",
                            "#メンター",
                            "#クリスマス",
                            "#クリスマスソング",
                            "#クリスマスプレゼント",
                            "#クリスマスケーキ",
                            "#クリスマスデート",
                            "#ディズニー",
                            "#クリスマスホテル",
                            "#クリスマスアニメ",
                            "#usj",
                            "#クリスマスインテリア",
                            "#クリスマス衣装",
                            "#お菓子",
                            "#アドヴェントカレンダー",
                            "#ケンタッキー",
                            "#エンジニア",
                            "#転職",
                            "#年収",
                            "#派遣",
                            "#資格",
                            "#採用",
                            "#インターン",
                            "#運用",
                            "#うつ",
                            "#web系",
                            "#オープン系",
                            "#キャリア",
                            "#キャリアプラン",
                            "#研修"
                          ] 
        self.search_list = [
                            "社畜",
                            "会長",
                            "社長",
                            "専務",
                            "常務",
                            "監査役",
                            "事業部長",
                            "部長",
                            "次長",
                            "課長",
                            "係長",
                            "主任",
                            "リーダー",
                            "メンター",
                            "クリスマス",
                            "クリスマスソング",
                            "クリスマスプレゼント",
                            "クリスマスケーキ",
                            "クリスマスデート",
                            "ディズニー",
                            "クリスマスホテル",
                            "クリスマスアニメ",
                            "usj",
                            "クリスマスインテリア",
                            "クリスマス衣装",
                            "お菓子",
                            "アドヴェントカレンダー",
                            "ケンタッキー",
                            "エンジニア",
                            "転職",
                            "年収",
                            "派遣",
                            "資格",
                            "採用",
                            "インターン",
                            "運用",
                            "うつ",
                            "web系",
                            "オープン系",
                            "キャリア",
                            "キャリアプラン",
                            "研修"
                          ] 
        self.search_list_test = [
                            "社長"
                            ]
        self.search_hash_dictionary = { 
                "#社畜":0,
                "#会長":1,
                "#社長":2,
                "#専務":3,
                "#常務":4,
                "#監査役":5,
                "#事業部長":6,
                "#部長":7,
                "#次長":8,
                "#課長":9,
                "#係長":10,
                "#主任":11,
                "#リーダー":12,
                "#メンター":13,
                "#クリスマス":14,
                "#クリスマスソング":15,
                "#クリスマスプレゼント":16,
                "#クリスマスケーキ":17,
                "#クリスマスデート":18,
                "#ディズニー":19,
                "#クリスマスホテル":20,
                "#クリスマスアニメ":21,
                "#usj":22,
                "#クリスマスインテリア":23,
                "#クリスマス衣装":24,
                "#お菓子":25,
                "#アドヴェントカレンダー":26,
                "#ケンタッキー":27,
                "#エンジニア":28,
                "#転職":29,
                "#年収":30,
                "#派遣":31,
                "#資格":32,
                "#採用":33,
                "#インターン":33,
                "#運用":34,
                "#うつ":35,
                "#web系":36,
                "#オープン系":37,
                "#キャリア":38,
                "#キャリアプラン":39,
                "#研修":40
                           } 
        self.search_dictionary = { 
                "社畜":0,
                "会長":1,
                "社長":2,
                "専務":3,
                "常務":4,
                "監査役":5,
                "事業部長":6,
                "部長":7,
                "次長":8,
                "課長":9,
                "係長":10,
                "主任":11,
                "リーダー":12,
                "メンター":13,
                "クリスマス":14,
                "クリスマスソング":15,
                "クリスマスプレゼント":16,
                "クリスマスケーキ":17,
                "クリスマスデート":18,
                "ディズニー":19,
                "クリスマスホテル":20,
                "クリスマスアニメ":21,
                "usj":22,
                "クリスマスインテリア":23,
                "クリスマス衣装":24,
                "お菓子":25,
                "アドヴェントカレンダー":26,
                "ケンタッキー":27,
                "エンジニア":28,
                "転職":29,
                "年収":30,
                "派遣":31,
                "資格":32,
                "採用":33,
                "インターン":33,
                "運用":34,
                "うつ":35,
                "web系":36,
                "オープン系":37,
                "キャリア":38,
                "キャリアプラン":39,
                "研修":40
                 } 
        self.search_char_dictionary = { 
                0: "社畜",
                1:"会長",
                2:"社長",
                3:"専務",
                4:"常務",
                5:"監査役",
                6:"事業部長",
                7:"部長",
                8:"次長",
                9:"課長",
                10:"係長",
                11:"主任",
                12:"リーダー",
                13:"メンター",
                14:"クリスマス",
                15:"クリスマスソング",
                16:"クリスマスプレゼント",
                17:"クリスマスケーキ",
                18:"クリスマスデート",
                19:"ディズニー",
                20:"クリスマスホテル",
                21:"クリスマスアニメ",
                22:"usj",
                23:"クリスマスインテリア",
                24:"クリスマス衣装",
                25:"お菓子",
                26:"アドヴェントカレンダー",
                27:"ケンタッキー",
                28:"エンジニア",
                29:"転職",
                30:"年収",
                31:"派遣",
                32:"資格",
                33:"採用",
                34:"インターン",
                35:"運用",
                36:"うつ",
                37:"web系",
                38:"オープン系",
                39:"キャリア",
                40:"キャリアプラン",
                41:"研修"
                 } 
        self.search_unblance_dictionary = { 
                1:"キャリアプラン",
                2:"オープン系",
                }
        self.search_priority_dictionary = { 
                "High":0,
                "Middle":1,
                "Low":2,
                }
        self.search_priority_char_dictionary = { 
                0:"High",
                1:"Middle",
                2:"Low",
                }
        self.search_category_dictionary = { 
                "NoSetting":0,
                "ライフライン":1,
                "交通機関":2,
                "住宅情報":3,
                "医療・福祉・健康相談":4,
                "安否確認":5,
                "救助":6,
                "物資要請":7,
                "生活支援・相談":8,
                }
        self.search_category_char_dictionary = { 
                0: "NoSetting",
                1: "ライフライン",
                2: "交通機関",
                3: "住宅情報",
                4: "医療・福祉・健康相談",
                5: "安否確認",
                6: "救助",
                7: "物資要請",
                8: "生活支援・相談"
                }
