import jieba.posseg as pseg

text = "我喜欢看书'不是"  # Przykładowe zdanie: "Lubię czytać książki"

words = pseg.cut(text)
for character, form_class in words:
    print(form_class)

for word, flag in words:
    print(f'{word}: {flag}')