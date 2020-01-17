from collections import Counter  # импортируем класс для вызова метода подсчета вхождения символов в текст

abc = ("а б в г д е ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я").split()  # создание алвавита строчных букв
ABC = ('А Б В Г Д Е Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я').split()  # создание алфавита заглавных букв

f = open("text_encrypted.txt", "r", encoding="utf-8")  # открытие файла с зашифрованной главой
c = dict(Counter(f.read().strip()))  # подсчет вхождения всех символов встреченых в файлу
f2 = open("text_orig.txt", "r", encoding="utf-8")  # открытие файла оригинальной книги "Война и Мир"
line = f2.read()  # считывание оригинальной книги в переменную
forig = open("text_orig.txt", "r",
             encoding="utf-8")  # зачем-то еще раз открываем книгу(оригинал) и записываем ее в переменную
c2 = dict(Counter(forig.read().strip()))  # подсчет вхождения всех символов встреченых в файле(оригинальной книге)
print('Original: ', c2)  # вывод количества вхождения всех символов в оригинальной книге
print('Encrypted:', c)  # вывод количества вхождения всех символов в зашифрованной главе
sortedC2 = dict(sorted(c2.items(), reverse=True,
                       key=lambda x: (x[1], x[0])))  # сортировка словарей с подстчетом символов по кол-ву вхождений
sortedC = dict(sorted(c.items(), reverse=True,
                      key=lambda x: (x[1], x[0])))  # сортировка словарей с подстчетом символов по кол-ву вхождений
print("Original part sorted by value: ", sortedC2)  # вывод отсортированных словарей вхождений
print("Encrypted part sorted by value: ", sortedC)  # вывод отсортированных словарей вхождений
dictionary = {}  # создание хеш-мапа замены(пока пустой наполняем позже)
cz = {}  # словарь частоты русских в шифре#
cz2 = {}  # словарь частоты русских в оригинале#
for key, value in c.items():  # цикл для заполнения словарей частоты русских символов в оригинале
    if key in abc or key in ABC:  # если ключ русский символ тогда...
        cz.update({key: value})  # ...записываем {ключ: значение} в новый словарь
for key2, value2 in c2.items():  # цикл для заполнения словарей частоты русских символов в оригинале
    if key2 in abc or key2 in ABC:  # если ключ русский символ тогда...
        cz2.update({key2: value2})  # ...записываем {ключ: значение} в новый словарь
cz = dict(sorted(cz.items(), reverse=True, key=lambda x: (x[1], x[0])))  # сортируем новые словари
cz2 = dict(sorted(cz2.items(), reverse=True, key=lambda x: (x[1], x[0])))  # сортируем новые словари
print(cz)  # вывод новых словарей
print(cz2)  # вывод новых словарей
for key in cz:  # создание хешмапа замены символов
    for key2 in cz2:
        dictionary.update({key: key2})  # составляем хеш-мап из ключей двух предыдущих словарей
        cz2.pop(key2)  # удаляем использованный ключ во втором словаре
        break  # ну и прерываем чтобы было хорошо
print("needed dict:", dictionary)  # выводим хеш-мап

fileEncr = open("text_encrypted.txt", "r", encoding="utf-8")  # открываем файл шифрованной главы для считывания
text = fileEncr.read()  # считываем шифрованную главу в переменную(в виде строки)
fileDecr = open("text_encoded.txt", "w", encoding="utf-8")  # открытие файла для записи уже расшифрованной главы
for key in dictionary:  # расшифровываем главу
    text = text.replace(key, dictionary.get(key))  # заменяем символы в главе

fileDecr.write(text)  # записываем главу
print(text, end='')  # выводим главу
print('\n')
fileEncr.close()  # закрываем файл для записи главы

# Биграммы
bigramHashsetEnc = {}
bigramHashsetOrig = {}
pairEnc = ''
pairOrig = ''
fileOrig = open("text_orig.txt", "r", encoding="utf-8")
text2 = fileOrig.read()
for i in range(0, len(text2) - 1):
    if (text2[i] in abc or text2[i] in ABC) and (text2[i + 1] in abc or text2[i + 1] in ABC):
        pairOrig = text2[i] + text2[i + 1]
    if pairOrig in bigramHashsetOrig.keys():
        bigramHashsetOrig.update({pairOrig: bigramHashsetOrig.get(pairOrig) + 1})
    else:
        bigramHashsetOrig.update({pairOrig: 1})
for i in range(0, len(text) - 1):
    if (text[i] in abc or text[i] in ABC) and (text[i + 1] in abc or text[i + 1] in ABC):
        pairEnc = text[i] + text[i + 1]
    if pairEnc in bigramHashsetEnc.keys():
        bigramHashsetEnc.update({pairEnc: bigramHashsetEnc.get(pairEnc) + 1})
    else:
        bigramHashsetEnc.update({pairEnc: 1})
print("Bigrams Hash-Map of original text:", dict(bigramHashsetOrig))
print("Bigrams Hash-Map:", dict(bigramHashsetEnc))
boHM = sorted(bigramHashsetOrig.items(), reverse=True, key=lambda x: (x[1], x[0]))
bHM = sorted(bigramHashsetEnc.items(), reverse=True, key=lambda x: (x[1], x[0]))
print(bHM)
print(boHM)

bHM = dict(bHM[:5])
boHM = dict(boHM[:5])

print(bHM)
print(boHM)
resultDic = {}
for key in boHM:  # создание хешмапа замены символов
    for key2 in bHM:
        resultDic.update({key: key2})  # составляем хеш-мап из ключей двух предыдущих словарей
        bHM.pop(key2)
        break
print(resultDic)
resultDictionary = {}
swapKey = ''
swapValue = ()
for i in resultDic:
    swapKey = str(i)
    swapValue = str(resultDic.get(i))
    print(swapKey + ":" + swapValue)

    for j in range(0, 1):
        resultDictionary.update({swapKey[0]: swapValue[0]})
        resultDictionary.update({swapKey[1]: swapValue[1]})
# print(resultDictionary)
# print(dictionary)

for keys in resultDictionary:
    if keys in dictionary.keys():
        dictionary.pop(keys)
        dictionary.update({keys: resultDictionary.get(keys)})
# print(dictionary)

fileEncr = open("text_encrypted.txt", "r", encoding="utf-8")  # открываем файл шифрованной главы для считывания
textEncodered = fileEncr.read()  # считываем шифрованную главу в переменную(в виде строки)
fileDecr = open("text_encodedbigrammas.txt", "w", encoding="utf-8")  # открытие файла для записи уже расшифрованной главы
for key in dictionary:  # расшифровываем главу
    textEncodered = textEncodered.replace(key, dictionary.get(key))  # заменяем символы в главе

fileDecr.write(textEncodered)  # записываем главу
print(textEncodered, end='')  # выводим главу
print('\n')
fileEncr.close()    # закрываем файл для записи главы