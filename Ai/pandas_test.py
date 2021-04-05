import pandas as pd

word_dict = {
    'Apple': '사과',
    'Banana': '바나나',
    'Carrot': '당근'
}

frequency_dict = {
    'Apple': 3,
    'Banana': 5,
    'Carrot': 7
}

word = pd.Series(word_dict)
frequency = pd.Series(frequency_dict)

summary = pd.DataFrame({
    'word': word,
    'frequency': frequency
})

summary.to_csv("summary.csv", encoding="utf-8-sig")
saved = pd.read_csv("summary.csv", index_col=0)
print(saved)
