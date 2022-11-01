

def count_vowels(txt):
  return sum([1 for x in txt.lower() if x in 'aeiou'])


text = input("Введите текст: ")
parts = text.split(", ")
words = []
for part in parts:
    words.extend(part.split(" "))
print(words)

words.sort(key=lambda x: count_vowels(x)/len(x))
print(words)