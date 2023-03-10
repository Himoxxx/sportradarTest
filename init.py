import sqlite3 as sl
con = sl.connect('scoreboard_db.db')


# with con:
#     con.execute("""
#         CREATE TABLE SCOREBOARD (
#             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#             homeTeam  NOT NULL TEXT UNIQUE,
#             homeScore  NOT NULL INTEGER,
#             awayTeam  NOT NULL TEXT UNIQUE,
#             awayScore  NOT NULLINTEGER,
#             addedTime TEXT
#         );
#     """)

# with con:
#     con.execute("""
#         CREATE TABLE ARCHIVE (
#             id INTEGER NOT NULL PRIMARY KEY,
#             homeTeam  NOT NULL TEXT,
#             homeScore  NOT NULL INTEGER,
#             awayTeam  NOT NULL TEXT,
#             awayScore  NOT NULL INTEGER,
#             addedTime TEXT
#         );
#     """)

# sql = 'INSERT INTO SCOREBOARD ( homeTeam, homeScore, awayTeam, awayScore, addedTime) values( ?, ?, ?, ?, ?)'
# data = [
#     ('Team A', 0, 'Team B', 0, '2022-12-16 13:57:01'),
#     ('Team C', 0, 'Team D', 0, '2022-12-16 14:23:12'),
# ]
# with con:
#     con.executemany(sql, data)

print ("---------------/n")
with con:
    data = con.execute("SELECT a.*, homeScore+awayScore as totalScore FROM SCOREBOARD a order by homeScore+awayScore desc, date(addedTime) desc")
    for row in data:
        print(row)