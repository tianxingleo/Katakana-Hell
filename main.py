# -*- coding: utf-8 -*-
from pypinyin import pinyin, Style

# 拼音 → 片假名 映射规则（简化近似）
romaji_to_katakana = {
    'a': 'ア', 'ai': 'アイ', 'an': 'アン', 'ang': 'アン', 'ao': 'アオ',
    'ba': 'バ', 'bai': 'バイ', 'ban': 'バン', 'bang': 'バン', 'bao': 'バオ', 'bei': 'ベイ',
    'bi': 'ビ', 'bian': 'ビエン', 'biao': 'ビアオ', 'bo': 'ボ', 'bu': 'ブ',
    'ca': 'ツァ', 'cai': 'ツァイ', 'can': 'ツァン', 'ce': 'ツォ', 'ci': 'ツー',
    'cha': 'チャ', 'chai': 'チャイ', 'chan': 'チャン', 'chang': 'チャン', 'chao': 'チャオ', 'che': 'チェ',
    'chi': 'チー', 'chu': 'チュ', 'chun': 'チュン', 'chuo': 'チュオ',
    'da': 'ダ', 'dai': 'ダイ', 'dan': 'ダン', 'dang': 'ダン', 'dao': 'ダオ', 'de': 'デ', 'di': 'ディ',
    'dian': 'ディエン', 'dong': 'ドン', 'du': 'ドゥ', 'duo': 'ドゥオ',
    'e': 'エ', 'ei': 'エイ', 'en': 'エン', 'er': 'アル',
    'fa': 'ファ', 'fan': 'ファン', 'fang': 'ファン', 'fei': 'フェイ', 'fo': 'フォ', 'fu': 'フ',
    'ga': 'ガ', 'gai': 'ガイ', 'gan': 'ガン', 'gao': 'ガオ', 'ge': 'ゲ', 'gu': 'グ', 'guo': 'グオ',
    'ha': 'ハ', 'hai': 'ハイ', 'han': 'ハン', 'hao': 'ハオ', 'he': 'ヘ', 'hu': 'フ', 'huo': 'フオ',
    'ji': 'ジ', 'jia': 'ジア', 'jian': 'ジエン', 'jiao': 'ジアオ', 'jie': 'ジエ', 'jin': 'ジン', 'jing': 'ジン', 'jiong': 'ジョン',
    'ju': 'ジュ', 'juan': 'ジュアン',
    'ka': 'カ', 'kai': 'カイ', 'kan': 'カン', 'ke': 'ケ', 'ku': 'ク', 'kuai': 'クアイ',
    'la': 'ラ', 'lai': 'ライ', 'lan': 'ラン', 'lang': 'ラン', 'le': 'レ', 'li': 'リ', 'lia': 'リア', 'lian': 'リエン', 'liang': 'リアン',
    'lin': 'リン', 'liu': 'リウ', 'long': 'ロン', 'lu': 'ル', 'luo': 'ルオ',
    'ma': 'マ', 'mai': 'マイ', 'man': 'マン', 'mang': 'マン', 'mao': 'マオ', 'mei': 'メイ', 'men': 'メン',
    'mi': 'ミ', 'mian': 'ミエン', 'ming': 'ミン', 'mo': 'モ', 'mu': 'ム',
    'na': 'ナ', 'nai': 'ナイ', 'nan': 'ナン', 'nao': 'ナオ', 'nei': 'ネイ', 'ni': 'ニ', 'nian': 'ニエン', 'nin': 'ニン',
    'ning': 'ニン', 'niu': 'ニウ', 'nong': 'ノン', 'nu': 'ヌ', 'nuo': 'ヌオ',
    'ou': 'オウ',
    'pa': 'パ', 'pai': 'パイ', 'pan': 'パン', 'pang': 'パン', 'pao': 'パオ', 'pei': 'ペイ', 'pen': 'ペン', 'pi': 'ピ',
    'ping': 'ピン', 'po': 'ポ', 'pu': 'プ',
    'qi': 'チ', 'qia': 'チャ', 'qian': 'チェン', 'qiao': 'チャオ', 'qie': 'チェ', 'qin': 'チン', 'qing': 'チン', 'qiong': 'チョン',
    'qu': 'チュ', 'quan': 'チュアン',
    'ran': 'ラン', 'rang': 'ラン', 'rao': 'ラオ', 'ren': 'レン', 'reng': 'レン', 'ri': 'リ', 'rong': 'ロン', 'rou': 'ロウ', 'ru': 'ル',
    'sa': 'サ', 'sai': 'サイ', 'san': 'サン', 'sang': 'サン', 'se': 'セ', 'si': 'スー',
    'sha': 'シャ', 'shai': 'シャイ', 'shan': 'シャン', 'shang': 'シャン', 'shao': 'シャオ', 'she': 'シェ', 'shi': 'シー', 'shou': 'ショウ', 'shu': 'シュ',
    'shuang': 'シュアン', 'shuo': 'シュオ',
    'ta': 'タ', 'tai': 'タイ', 'tan': 'タン', 'tang': 'タン', 'tao': 'タオ', 'te': 'テ', 'ti': 'ティ', 'tian': 'ティエン',
    'ting': 'ティン', 'tong': 'トン', 'tu': 'トゥ', 'tuo': 'トゥオ',
    'wa': 'ワ', 'wai': 'ワイ', 'wan': 'ワン', 'wang': 'ワン', 'wei': 'ウェイ', 'wen': 'ウェン', 'wo': 'ヲ', 'wu': 'ウ',
    'xi': 'シ', 'xia': 'シャ', 'xian': 'シエン', 'xiang': 'シャン', 'xiao': 'シャオ', 'xie': 'シェ', 'xin': 'シン', 'xing': 'シン', 'xiong': 'ション',
    'xiu': 'シウ', 'xu': 'シュ', 'xuan': 'シュアン',
    'ya': 'ヤ', 'yan': 'イエン', 'yang': 'ヤン', 'yao': 'ヤオ', 'ye': 'イエ', 'yi': 'イ', 'yin': 'イン', 'ying': 'イン', 'yo': 'ヨ', 'yong': 'ヨン', 'yu': 'ユ', 'yuan': 'ユアン',
    'za': 'ザ', 'zai': 'ザイ', 'zan': 'ザン', 'zang': 'ザン', 'zao': 'ザオ', 'ze': 'ゼ', 'zhe': 'ジェ', 'zhi': 'ジー', 'zhong': 'ジョン', 'zhu': 'ジュ', 'zhuang': 'ジュアン',
    'zhuo': 'ジュオ', 'zi': 'ズー', 'zu': 'ズ', 'zuo': 'ズオ'
}

def pinyin_to_katakana(py):
    """将拼音（无声调）转为片假名"""
    py = py.lower()
    # 按长匹配
    for l in [5, 4, 3, 2, 1]:
        if py[:l] in romaji_to_katakana:
            return romaji_to_katakana[py[:l]]
    # 没找到近似匹配则逐字符拼假名
    result = ''
    for ch in py:
        result += romaji_to_katakana.get(ch, '・')
    return result

def chinese_to_katakana(text):
    """中文字符串 -> 拼音 -> 片假名"""
    pys = pinyin(text, style=Style.NORMAL)
    result = ''
    for p in pys:
        py = p[0]
        result += pinyin_to_katakana(py)
    return result

if __name__ == "__main__":
    text = input("请输入中文字符串：")
    print("对应的片假名为：")
    print(chinese_to_katakana(text))
