from jamo import h2j, j2hcj

# 종성 확인
def get_jongsung_TF(sentence):
    sentence = list(sentence)
    last_word = sentence[-1]
    last_word = list(j2hcj(h2j(last_word)))
    jongsung = "T"
    if last_word[-1] in (
    'ㅏ', 'ㅑ', 'ㅓ', 'ㅕ', 'ㅗ', 'ㅛ', 'ㅜ', 'ㅠ', 'ㅡ', 'ㅣ', 'ㅘ', 'ㅚ', 'ㅙ', 'ㅝ', 'ㅞ', 'ㅢ', 'ㅐ', 'ㅔ', 'ㅟ', 'ㅖ', 'ㅒ', '2', '4',
    '5', '9'):
        jongsung = "F"

    return jongsung