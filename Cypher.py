import codecs
abc = ("а б в г д е ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я").split()
ABC = ('А Б В Г Д Е Ж З И Й К Л М Н О П Р С Т У Ф Х Ц Ч Ш Щ Ъ Ы Ь Э Ю Я').split()
fileObj = codecs.open("text_origPart.txt", "r", "utf-8")
text = fileObj.read()  # или читайте по строке
fileObj2 = codecs.open("Text_encrypted.txt", "w", "utf-8")
text = text.lower()
for i in text:
    #k = i



    if i in abc or i in ABC:
        k = chr(ord(i) + 5)

        fileObj2.write(k)
        print(k, end='')
    else:
       fileObj2.write(i)
       print(i, end='')
fileObj.close()
fileObj2.close()
