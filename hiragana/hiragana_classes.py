hiragana_literals = [
    'あ', 'い', 'う', 'え', 'お',
    'か', 'が', 'き', 'ぎ', 'く',
    'ぐ', 'け', 'げ', 'こ', 'ご',
    'さ', 'ざ', 'し', 'じ', 'す',
    'ず', 'せ', 'ぜ', 'そ', 'ぞ',
    'た', 'だ', 'ち', 'ぢ', 'つ',
    'づ', 'て', 'で', 'と', 'ど',
    'な', 'に', 'ぬ', 'ね', 'の',
    'は', 'ば', 'ぱ', 'ひ', 'び',
    'ぴ', 'ふ', 'ぶ', 'ぷ', 'へ',
    'べ', 'ぺ', 'ほ', 'ぼ', 'ぽ',
    'ま', 'み', 'む', 'め', 'も',
    'や', 'ゆ', 'よ', 'ら', 'り',
    'る', 'れ', 'ろ', 'わ', 'を',
    'ん']

romanji = [
    "A", "I", "U", "E", "O",
    "Ka", "Ga", "Ki", "Gi", "Ku",
    "Gu", "Ke", "Ge", "Ko", "Go",
    "Sa", "Za", "Shi", "Ji", "Su",
    "Zu", "Se", "Ze", "So", "Zo",
    "Ta", "Da", "Chi", "Di", "Tsu",
    "Du", "Te", "De", "To", "Do",
    "Na", "Ni", "Nu", "Ne", "No",
    "Ha", "Ba", "Pa", "Hi", "Bi",
    "Pi", "Fu", "Bu", "Pu", "He",
    "Be", "Pe", "Ho", "Bo", "Po",
    "Ma", "Mi", "Mu", "Me", "Mo",
    "Ya", "Yu", "Yo", "Ra", "Ri",
    "Ru", "Re", "Ro", "Wa", "Wo",
    "N"]

# classification_indices = range(len(romanji))
romanji_to_class = dict(zip(romanji, range(len(romanji))))
romanji_to_class.setdefault("NA", -1)

class_map = {
    'あ': 'A',
    'い': "I",
    'う': "U",
    'え': "E",
    'お': "O",
    'か': "Ka",
    'が': "Ga",
    'き': "Ki",
    'ぎ': "Gi",
    'く': "Ku",
    'ぐ': "Gu",
    'け': "Ke",
    'げ': "Ge",
    'こ': "Ko",
    'ご': "Go",
    'さ': "Sa",
    'ざ': "Za",
    'し': "Shi",
    'じ': "Ji",
    'す': "Su",
    'ず': "Zu",
    'せ': "Se",
    'ぜ': "Ze",
    'そ': "So",
    'ぞ': "Zo",
    'た': "Ta",
    'だ': "Da",
    'ち': "Chi",
    'ぢ': "Di",
    'つ': "Tsu",
    'づ': "Du",
    'て': "Te",
    'で': "De",
    'と': "To",
    'ど': "Do",
    'な': "Na",
    'に': "Ni",
    'ぬ': "Nu",
    'ね': "Ne",
    'の': "No",
    'は': "Ha",
    'ば': "Ba",
    'ぱ': "Pa",
    'ひ': "Hi",
    'び': "Bi",
    'ぴ': "Pi",
    'ふ': "Fu",
    'ぶ': "Bu",
    'ぷ': "Pu",
    'へ': "He",
    'べ': "Be",
    'ぺ': "Pe",
    'ほ': "Ho",
    'ぼ': "Bo",
    'ぽ': "Po",
    'ま': "Ma",
    'み': "Mi",
    'む': "Mu",
    'め': "Me",
    'も': "Mo",
    'や': "Ya",
    'ゆ': "Yu",
    'よ': "Yo",
    'ら': "Ra",
    'り': "Ri",
    'る': "Ru",
    'れ': "Re",
    'ろ': "Ro",
    'わ': "Wa",
    'を': "Wo",
    'ん': "N"
}
