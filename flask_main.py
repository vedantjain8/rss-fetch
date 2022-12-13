from flask import Flask,render_template, url_for,request
import sqlite3

app = Flask(__name__)

@app.route("/")
@app.route("/home")
@app.route("/sortlatest/page/<int:page>")
def sortLatest(page=1):
    db = sqlite3.connect("rss.db")
    cur = db.cursor()

    temp = dict()
    post = []

    # Get the total number of rows in the table
    total_rows = cur.execute('SELECT COUNT(*) FROM rss_data').fetchone()[0]

    # Calculate the total number of pages
    total_pages = total_rows // 10 + (total_rows % 10 > 0)

    # Validate the page number
    if page < 1 or page > total_pages:
        return 'Invalid page number'

    # Calculate the offset for the query
    offset = (page - 1) * 10

    # Query the database for the results for the current page
    results = cur.execute(f'select id,title,link,summary,pub_date,pub_month,pub_year,site,author,image from rss_data order by time asc, pub_day asc,pub_month asc,pub_year asc LIMIT 10 OFFSET {offset}').fetchall()
    
    for j in range(len(results)):
        temp["id"] = results[j][0]
        temp["title"] = results[j][1]
        temp["link"] = results[j][2]
        temp["summary"] = results[j][3]
        temp["date_posted"] = results[j][4] + results[j][5]+ results[j][6]
        temp["site"] = results[j][7][0].upper() + results[j][7][1:]
        temp["author"] = results[j][8]
        temp["image"] = results[j][9]
        post.append(temp)
        temp = dict()

    # Check if there is a next page
    next_page = page + 1 if page < total_pages else None
    previous_page = page - 1 if page-1 > 0 else None
    cur.close()
    db.close()

    # Render the template with the results and the page count
    return render_template('home.html', title = "Home", posts = post, latestActive="active", oldestActive="", page=page, total_pages=total_pages, next_page=next_page, previous_page= previous_page)

@app.route("/sortoldest/page/<int:page>")
def SortOldest(page=1):
    db = sqlite3.connect("rss.db")
    cur = db.cursor()

    temp = dict()
    post = []

    # Get the total number of rows in the table
    total_rows = cur.execute('SELECT COUNT(*) FROM rss_data').fetchone()[0]

    # Calculate the total number of pages
    total_pages = total_rows // 10 + (total_rows % 10 > 0)

    # Validate the page number
    if page < 1 or page > total_pages:
        return 'Invalid page number'

    # Calculate the offset for the query
    offset = (page - 1) * 10

    # Query the database for the results for the current page
    results = cur.execute(f'select id,title,link,summary,pub_date,pub_month,pub_year,site,author,image from rss_data order by time desc, pub_day desc,pub_month desc,pub_year desc LIMIT 10 OFFSET {offset}').fetchall()

    for j in range(len(results)):
        temp["id"] = results[j][0]
        temp["title"] = results[j][1]
        temp["link"] = results[j][2]
        temp["summary"] = results[j][3]
        temp["date_posted"] = results[j][4] + results[j][5]+ results[j][6]
        temp["site"] = results[j][7][0].upper() + results[j][7][1:]
        temp["author"] = results[j][8]
        temp["image"] = results[j][9]
        post.append(temp)
        temp = dict()

    # Check if there is a next page
    next_page = page + 1 if page < total_pages else None
    previous_page = page - 1 if page-1 > 0 else None

    cur.close()
    db.close()

    # Render the template with the results and the page count
    return render_template('home.html', title = "Home", posts = post, latestActive="", oldestActive="active", page=page, total_pages=total_pages, next_page=next_page, previous_page= previous_page)


@app.route("/about")
def about():
    return render_template('about.html',title = "About")

@app.errorhandler(404)
def not_found(e):
  return render_template("404.html"),404

if __name__ == '__main__':
    app.run(debug=True)