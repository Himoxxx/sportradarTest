#the main application that allows to control the flow
import sqlite3 as sl


#connection string
con = sl.connect('scoreboard_db.db')

def startNewGame(homeTeam, awayTeam, startTime):
#function for starting new game with score 0 to 0, adding with custom timestamp
    sql = 'INSERT INTO SCOREBOARD ( homeTeam, homeScore, awayTeam, awayScore, addedTime) values( ?, ?, ?, ?, ?)'
    data = [
        (homeTeam, 0, awayTeam, 0, startTime),
    ]
    with con:
        con.executemany(sql, data)    



#startNewGame("A","B","2022-12-18 21:50")


# print ("---------------/n")
# with con:
#     data = con.execute("SELECT a.*, homeScore+awayScore as totalScore FROM SCOREBOARD a order by homeScore+awayScore desc, date(addedTime) desc")
#     for row in data:
#         print(row)