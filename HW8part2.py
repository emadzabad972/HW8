# ערוך מדגם ממוצע גבהים של שחקני ה- NBA
# צור רשימה ריקה
# רוץ בלולאה וקלוט גבהי שחקנים ) float )בלולאה. אם הגובה שנקלט נמוך מ- 1.60 או
# גבוה מ - 3.0 התעלם, רמז: continue. כל גובה תקין הוסף לרשימה באמצעות append
# כאשר המשתמש יכניס גובה מינוס 999 צא מהלולאה
# בתום הלולאה הדפס-
# .1 כמה שחקנים נקלטו במדגם?
# .2 מהו הגובה של השחק ן הכי גבוה?
# .3 מהו הגובה של השחקן הכי נמוך?
# .4 מהו ממוצע הגבהים של כל השחקנים?
# .5 כמה שחקנים יותר גבוהים מ - 2.0 מטר?
# .6 כמה שחקנים יותר גבוהים מהממוצע? )רמז: רוץ בלולאה על כל רשימת השחקנים ובדו ק
# עבור כל גובה אם הוא גדול מהממוצע שחישבת קודם. אם כן הגדל את מונה הגבהים ב - 1(

# start
players: list[float] = []
counter: int = 0
higher: float = 0
higher_counter: float = 0
SENTINEL = -999

while True:
    height: float = float(input('enter the height: '))
    if height == -999:
        break
    if not 1.60 <= height <= 3.0:
        continue
    if height:
        counter += 1
        players.append(height)
    if height > 2.0:
        higher = height
        higher_counter += 1
avg: float = sum(players) / counter
higher_than: float = 0
for i in players:
    if i > avg:
        higher_than += 1

print(f'the number of the players is {counter}')
print(f'the highest is : {max(players)}')
print(f'the lowest player was: {min(players)}')
import statistics
print(f'the average height is: {statistics.mean(players)}')
print(f'players higher than 2.0: {higher_counter}')
print(f'the number of players who are higher than average is: {higher_than}')
