import sqlite3

db = sqlite3.connect("rss.db")
cur = db.cursor()

post = []
temp = dict()

post_retrive = cur.execute(f"select id,title,link,summary,pub_date,pub_month,pub_year,site,author,image from rss_data order by time asc, pub_day asc,pub_month asc,pub_year asc;")
post_retrive_fetch = post_retrive.fetchall()
for j in range(len(post_retrive_fetch)):
    # print(post_retrive_fetch[j])
    temp["id"] = post_retrive_fetch[j][0]
    temp["title"] = post_retrive_fetch[j][1]
    temp["link"] = post_retrive_fetch[j][2]
    temp["summary"] = post_retrive_fetch[j][3]
    temp["date_posted"] = post_retrive_fetch[j][4] + post_retrive_fetch[j][5]+ post_retrive_fetch[j][6]
    temp["site"] = post_retrive_fetch[j][7][0].upper() + post_retrive_fetch[j][7][1:]
    temp["author"] = post_retrive_fetch[j][8]
    temp["image"] = post_retrive_fetch[j][9]
    post.append(temp)
    temp = dict()

# print(post)