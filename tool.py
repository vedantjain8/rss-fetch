import rss_site
import sqlite3
import os


db = sqlite3.connect("rss.db")
curr = db.cursor()

def dropAllSQLtable():
    for i in rss_site.siteDict:
        site_name = str(rss_site.siteDict.get(i)[1].title())  # site name
        curr.execute(f"drop table {site_name};")
    db.commit()

def dropAllSQLtableTrigger():
    try:
        for i in rss_site.siteDict:
            site_name = str(rss_site.siteDict.get(i)[1].title())  # site name
            curr.execute(f"drop trigger oldPost_delete_{site_name};")
        db.commit()
    except:
        pass

def dropSpecificSQLtableTrigger(site_name):
    curr.execute(f"drop trigger oldPost_delete_{site_name};")
    db.commit()

def dropSpecificSQLtable(site_name):
    curr.execute(f"drop table {site_name};")
    db.commit()


def listAllSQLtable():
    print("\n\n")
    for i in rss_site.siteDict:
        site_name = str(rss_site.siteDict.get(i)[1].title())  # site name
        print(site_name)
    db.commit()

def countTable():
    print("\n\n")
    siteCount =0
    for i in rss_site.siteDict:
        siteCount +=1
    print(siteCount)

def nuke():
    db.close()
    os.system("del rss.db")

if __name__=="__main__":
    while True:
        choice = int(input(
            """\n\nSQLite command aliases
            1. List all tables 
            2. Drop specific table 
            3. Drop all table 
            4. Drop specific trigger 
            5. Drop oldPost_delete trigger for all tables 
            6. Count all tables 
            7. Nuke - Delete rss.db
            99. Exit \n\nEnter your choice: """))

        if choice == 1:
            listAllSQLtable()
        elif choice == 2:
            dropSpecificSQLtable(str(input("\n\nEnter table name: ")))
        elif choice == 3:
            dropAllSQLtable()
        elif choice == 4:
            dropSpecificSQLtableTrigger(str(input("\n\nEnter trigger name: ")))
        elif choice == 5:
            dropAllSQLtableTrigger()
        elif choice == 6:
            countTable()
        elif choice == 7:
            nuke()
            print("""
                _.-^^---....,,--       
            _--                  --_  
            <                        >)
            |                         | 
            \._                   _./  
                ```--. . , ; .--'''       
                    | |   |             
                .-=||  | |=-.   
                `-=#$%&%$#=-'   
                    | ;  :|     
            _____.,-#%&$@%#&#~,._____
            """)
        elif choice == 99:
            break
        else:
            print("Enter a valid option!")
