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


# startNewGame("E","F","2022-12-18 21:59")

def updateScore(matchID, homeScoreUpdate, awayScoreUpdate):
    #function to update the score of match, basing on matchID (primary key) it updates the home score and away score
    sql2 = 'UPDATE SCOREBOARD SET homeScore = ?, awayScore=? where id = ?;'
    data2 = [homeScoreUpdate,awayScoreUpdate,matchID]
    with con:
        con.execute(sql2, data2)            


#updateScore(1,1,5)


print ("--------------- \n")
with con:
    data = con.execute("SELECT a.*, homeScore+awayScore as totalScore FROM SCOREBOARD a order by homeScore+awayScore desc, date(addedTime) desc")
    for row in data:
        print(row)