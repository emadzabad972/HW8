# **רשות/אתגר – מעבר לרמה שלמדנו בכיתה .... ראה הוזהרת
# הכן רשימה של מספרים בין 10-100 בדילוגים של ,10 כלומר: ,10 ,20 30 .. 100
# קלוט בלולאה מספרים מהמשתמש עד שנקלט מינוס 999
# כל מספר שנקלט יוכנס ברשימה באינד קס הנכון כדי לשמור על הרשימה ממויינת
# לדוגמא -
# אם נקלט 12 הוא יוכנס בין 10 ל - :20 ,10 ,12 ,20 30 .. 100
# אם נקלט מינוס 5 הוא יוכנס לפני :10 -5 , ,10 ,12 ,20 30 .. 100
# אם נקלט 200 הוא יוכנס אחרי :100 -5 , ,10 ,12 ,20 30 .. ,100 200

# start
list_1: list[int] = [i for i in range(10, 110, 10)]
while True:
    number: int = int(input('enter a number: '))
    if number == -999:
        break
    elif number >= list_1[-1]:
        list_1.append(number)
    else:
        for i in range(len(list_1)):
            if number < list_1[i]:
                list_1.insert(i,number)
                break
    print(list_1)
