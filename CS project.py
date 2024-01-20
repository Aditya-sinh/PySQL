#functions
def viewall(tab):
    if tab=="Standings":
        c1.execute("select * from standings order by position")
    if tab=="Gboot" or tab=="Gglove":
        c1.execute("select * from {} order by rnk".format(tab))
    elif tab=="Transfers" or tab=="Profits":
         c1.execute("select * from {}".format(tab))
    data=c1.fetchall()
    for r in data:
        print(r)

def viewvar(tab,rowcount):
    if tab=="Standings":
        c1.execute("select * from standings order by position")
    if tab=="Gboot" or tab=="Gglove":
        c1.execute("select * from {} order by rnk".format(tab))
    elif tab=="Transfers" or tab=="Profits":
         c1.execute("select * from {}".format(tab))
    data=c1.fetchmany(rowcount)
    for r in data:
        print(r)

def add(tab, dat):
    c1.execute("insert into {} values {}".format(tab, dat))

def update1(tab, r, nval, crtr):
    c1.execute("update {} set {}={} where {}='{}'".format(tab, r, nval, 'team_name', crtr))
def update2(tab, r, nval, crtr):
    c1.execute("update {} set {}={} where {}='{}'".format(tab, r, nval, 'player_name', crtr))
#main
print("tables are as follows:")
print("Standings")
print("Transfers")
print("Profits")
print("Gboot")
print("Gglove")
import mysql.connector as sqltor
mycon=sqltor.connect(host="localhost", user="root", passwd="adi123user", database="football")
if mycon.is_connected()==False:
    print("Error connecting to MySql")
else:
    c1=mycon.cursor()
    while True:
        print("choose among the following:")
        print("1.View")
        print("2.Add")
        print("3.Update")
        print("4.Simulate a Match")
        print("5.Close")
        n=int(input("enter corrosponding code:"))
        if n==1:
            tab=input("enter Table name that you wish to view:")
            if tab=="Standings" or tab=="Transfers" or tab=="Profits" or tab=="Gboot" or tab=="Gglove":
                print("1.All")
                print("2.Variable")
                row=int(input("How many rows do you wish to view?"))
                if row==1:
                    viewall(tab)
                if row==2:
                    rowcnt=int(input("enter number of rows you wish to you:"))
                    viewvar(tab,rowcnt)
            else:
                print("wrong entry")
        elif n==2:
            tab=input("enter Table name within which you wish to add:")
            if tab=="Standings":
                pos=int(input("enter position:"))
                teamn=input("enter team name")
                mp=int(input("enter mathches played"))
                points=int(input("enter points of the team"))
                gs=int(input("enter goals scored by the team"))
                gc=int(input("enter goals conceded by the team"))
                gt=gs-gc
                dat=(pos, teamn, mp, points, gs, gc, gt)
                add(tab, dat)
            elif tab=="Transfers":
                playern=input("enter player name:")
                formerteam=input("enter former team name:")
                transferredteam=input("enter the transferred team name:")
                val=int(input("enter value"))
                dat=(playern,formerteam,transferredteam,value)
                add(tab, dat)
            elif tab=="Profits":
                teamn=input("enter team name:")
                netpro=int(input("enter net profit:"))
                tickets=float(input("enter profit percent from tickets:"))
                stream=float(input("enter profit percent from streaming:"))
                sponsor=float(input("enter sponsor investment percent:"))
                dat=(teamn,netpro,tickets,stream,sponsor)
                add(tab,dat)
            elif tab=="Gboot":
                rnk=int(input("enter rank:"))
                playern=input("enter player name:")
                teamn=input("enter teamn name:")
                mp=int(input("enter no of mnatches played:"))
                gs=int(input("enter number of goals scored:"))
                dat=(rnk, playern, teamn, mp, gs)
                add(tab,dat)
            elif tab=="Gglove":
                rnk=int(input("enter rank:"))
                playern=input("enter player name:")
                teamn=input("enter teamn name:")
                mp=int(input("enter no of mnatches played:"))
                gs=int(input("enter number of goals saved:"))
                dat=(rnk, playern, teamn, mp, gs)
                add(tab,dat)
            else:
                print("wrong entry")
        elif n==3:
            tab=input("which table do you want to update:")
            if tab=="Standings" or tab=="Profits":
                crtr=input("enter name of team which needs to be updated:")
                r=input("enter column name which needs to be updated:")
                if r=="team_name":
                    nval=eval(input("enter new value for the column:"))
                    update(tab, r, nval, crtr)
                elif r=="position" or r=="matches_played" or r=="points" or r=="goals_scored" or r=="goals_conceded" or r=="goals_tally":
                    nval=int(input("enter new value for the column:"))
                    update1(tab, r, nval, crtr)
                else:
                    print("wrong entry")
            elif tab=="Transfers" or tab=="Gboot" or tab=="Gglove":
                crtr=input("enter name of player which needs to be updated:")
                r=input("enter column name which needs to be updated:")
                if r=="player_name" or r=="former_team" or r=="transferred_team" or r=="team_name":
                    nval=eval(input("enter new value for the column:"))
                    update(tab, r, nval, crtr)
                elif r=="value" or r=="rnk" or r=="matches_played" or r=="goals_scored" or r=="saves":
                    nval=int(input("enter new value for the column:"))
                    update2(tab, r, nval, crtr)
            else:
                print("wrong entry")
        elif n==4:
            t1=input("enter name of first team")
            t2=input("enter name of second team")
            g1=int(input("enter goals scored by first team:"))
            g2=int(input("enter goals scored by second team:"))
            if g1>g2:
                print(t1, "wins")
                c1.execute("update standings set points={}+{} where team_name='{}'".format('points', 3, t1))
                c1.execute("update standings set goals_scored={}+{} where team_name='{}'".format('goals_scored', g1, t1))
                c1.execute("update standings set goals_conceded={}+{} where team_name='{}'".format('goals_conceded', g2, t1))
                c1.execute("update standings set goals_tally={}-{} where team_name='{}'".format('goals_scored', 'goals_conceded', t1))
            elif g1<g2:
                print(t2, "wins")
                c1.execute("update standings set points={}+{} where team_name='{}'".format('points', 3, t2))
                c1.execute("update standings set goals_scored={}+{} where team_name='{}'".format('goals_scored', g2, t2))
                c1.execute("update standings set goals_conceded={}+{} where team_name='{}'".format('goals_conceded', g1, t2))
                c1.execute("update standings set goals_tally={}-{} where team_name='{}'".format('goals_scored', 'goals_conceded', t2))
            elif g1==g2:
                print("draw")
                c1.execute("update standings set points={}+{} where team_name='{}'".format('points', 1, t1))
                c1.execute("update standings set points={}+{} where team_name='{}'".format('points', 1, t2))
                c1.execute("update standings set goals_scored={}+{} where team_name='{}'".format('goals_scored', g1, t1))
                c1.execute("update standings set goals_conceded={}+{} where team_name='{}'".format('goals_conceded', g2, t1))
                c1.execute("update standings set goals_tally={}-{} where team_name='{}'".format('goals_scored', 'goals_conceded', t1))
                c1.execute("update standings set goals_scored={}+{} where team_name='{}'".format('goals_scored', g2, t2))
                c1.execute("update standings set goals_conceded={}+{} where team_name='{}'".format('goals_conceded', g1, t2))
                c1.execute("update standings set goals_tally={}-{} where team_name='{}'".format('goals_scored', 'goals_conceded', t2))
            else:
                print("wrong entry")
        elif n==5:
            print("Thank you!")
            break
































            
                
