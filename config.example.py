# Copy this file to china_bean_importer_config.py and place along side
# your import config

from china_bean_importers.common import BillDetailMapping as BDM

config = {
    "importers": {
        "alipay": {
            "account": "Assets:Alipay:Balance",
            "huabei_account": "Liabilities:Alipay:HuaBei",
            "yuebao_account": "Assets:Alipay:YueBao",
            "red_packet_income_account": "Income:RedPacket",
            "red_packet_expense_account": "Expenses:RedPacket",
            "category_mapping": {
                "交通出行": "Expenses:Transport:Others",
                "餐饮美食": "Expenses:Eating",
                "教育培训": "Expenses:Education:Others",
                "日用百货": "Expenses:Daily",
            },
        },
        "wechat": {
            "account": "Assets:WeChat:Balance",
            "lingqiantong_account": "Assets:WeChat:LingQianTong",
            "red_packet_income_account": "Income:RedPacket",
            "red_packet_expense_account": "Expenses:RedPacket",
            "family_card_expense_account": "Expenses:WeChat:FamilyCard",
            "group_payment_expense_account": "Expenses:Unknown",
            "group_payment_income_account": "Income:Unknown",
            "transfer_expense_account": "Expenses:Unknown",
            "transfer_income_account": "Income:Unknown",
        },
        "thu_ecard": {
            "account": "Assets:Card:THU",
        },
        "card_narration_whitelist": ["财付通(银联云闪付)"],
        "card_narration_blacklist": ["支付宝", "财付通", "美团支付"],
    },
    "card_accounts": {
        "Assets": {
            "BoC:Card": ["XXXX"],
            "CCB:Card": ["XXXX"],
        },
    },
    "pdf_passwords": ["123456"],
    # account matching
    "unknown_expense_account": "Expenses:Unknown",
    "unknown_income_account": "Income:Unknown",
    "detail_mappings": [
        BDM(
            ["Valve"],
            ["Steam Purchase"],
            "Expenses:Entertainment",
            [],
            {"platform": "Steam"},
        ),
        BDM(["京东"], [], "Expenses:JD", [], {"platform": "京东"}),
        BDM([], ["饿了么"], "Expenses:Eating", [], {"platform": "饿了么"}),
        BDM([], ["结息"], "Income:Interest", [], {}),
        BDM([], ["商铺健身房"], "Expenses:Entertainment", [], {}),
    ],
}
