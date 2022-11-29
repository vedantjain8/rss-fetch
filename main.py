import rss_site,rss_fetch,sqlite3,os,datetime,time,re,logging,tool,argparse

def dumpp():
    def cleanString(s):
        r = re.sub(r'[^\w]', ' ', s)
        s = re.sub(' +', ' ', r)
        return str(s)

    start = time.time()
    
    try:
        os.mkdir("logs")
    except:
        pass

    logging.basicConfig(filename=r"logs/logs.log",
                        format='%(asctime)s %(message)s',
                        filemode='a')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    db = sqlite3.connect("rss.db")
    cur = db.cursor()
    tool.dropAllSQLtableTrigger()
    
    # Initialize parser
    parser = argparse.ArgumentParser()
    
    # Adding optional argument
    parser.add_argument("-k", "--Key", help = "Key from rss_site", default=None)
        
    # Read arguments from command line
    args = parser.parse_args()
    
    if args.Key:
        site_name = str(rss_site.siteDict.get(str(args.Key))[1].title())  
        site_url = str(rss_site.siteDict.get(str(args.Key))[0])
        cur.execute(f"create table if not exists {site_name} (id text primary key, title text not null, link text not null,summary text, time text not null, pub_day text not null, pub_date text not null, pub_month text not null, pub_year text not null, pub_time text not null);")
        cur.execute(f"create trigger if not exists oldPost_delete_{site_name} before insert on {site_name} when (select count(id) from {site_name}) > {int(rss_site.min_articles_to_retain_per_website)} begin delete from {site_name} where id in (select id from {site_name} order by time asc limit 1); end;")
        posts_details, post_count = rss_fetch.get_posts_details(rss=site_url)
        for post in posts_details:
            try:
                postTitle = cleanString(str(post["title"]))
                insert_qry = f'insert into {site_name} values ("{post["id"]}", "{postTitle}","{post["link"]}","{post["summary"]}",datetime("now"),"{post["pub_day"]}" ,"{post["pub_date"]}" ,"{post["pub_month"]}","{post["pub_year"]}","{post["pub_time"]}");'
                cur.execute(insert_qry)
                #notification
                db.commit()
                logger.info(f">> ADDED: {site_name} [+] {postTitle}")
                
            except Exception as error:
                if str(error).split(" ")[0:3] == ['UNIQUE', 'constraint', 'failed:']:
                    pass
                else:
                    logger.error(f">> ERROR: {site_name} [!] {postTitle} -> {error}")

        end = time.time()
        logger.info(f"Last ran on {datetime.datetime.now()} for {site_name}")
        logger.info(f"Completed in: {round((end-start)*10**3/1000, 5)} Seconds")
    else:
        for i in rss_site.siteDict:
            site_name = str(rss_site.siteDict.get(i)[1].title())  
            site_url = str(rss_site.siteDict.get(i)[0])

            cur.execute(f"create table if not exists {site_name} (id text primary key, title text not null, link text not null,summary text, time text not null, pub_day text not null, pub_date text not null, pub_month text not null, pub_year text not null, pub_time text not null);")
            cur.execute(f"create trigger if not exists oldPost_delete_{site_name} before insert on {site_name} when (select count(id) from {site_name}) > {int(rss_site.min_articles_to_retain_per_website)} begin delete from {site_name} where id in (select id from {site_name} order by time asc limit 1); end;")
            posts_details, post_count = rss_fetch.get_posts_details(rss=site_url)
            for post in posts_details:
                
                try:
                    postTitle = cleanString(str(post["title"]))
                    insert_qry = f'insert into {site_name} values ("{post["id"]}", "{postTitle}","{post["link"]}","{post["summary"]}",datetime("now"),"{post["pub_day"]}" ,"{post["pub_date"]}" ,"{post["pub_month"]}","{post["pub_year"]}","{post["pub_time"]}");'
                    cur.execute(insert_qry)
                    #notification
                    db.commit()
                    logger.info(f">> ADDED: {site_name} [+] {postTitle}")
                
                except Exception as error:
                    if str(error).split(" ")[0:3] == ['UNIQUE', 'constraint', 'failed:']:
                        pass
                    else:
                        logger.error(f">> ERROR: {site_name} [!] {postTitle} -> {error}")
        
        end = time.time()
        logger.info(f"Last ran on {datetime.datetime.now()}")
        logger.info(f"Completed in: {round((end-start)*10**3/1000, 5)} Seconds")

    db.close()
    

if __name__=="__main__":
    dumpp()