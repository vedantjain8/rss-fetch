def get_posts_details(rss=None):
    """
    Take link of rss feed as argument
    """
    if rss is not None:

        # import the library only when url for feed is passed
        try:
            import feedparser
            import os
            from link_preview import link_preview
            from bs4 import BeautifulSoup as BSHTML
            from modules import listToString
        except:
            os.system("pip install -r requirements.txt")
        import re

        # parsing blog feed
        blog_feed = blog_feed = feedparser.parse(rss)
        postCount = 0

        # getting lists of blog entries via .entries
        posts = blog_feed.entries

        # dictionary for holding posts details
        post_list = []

        # iterating over individual posts
        for post in posts:
            temp = dict()

            # if any post doesn't have information then throw error.
            try:
                if post.id == "" or post.id == " " or post.id == None:
                    pass
                else:
                    temp["author"]= temp["summary"] = temp["pub_day"] =temp["pub_date"]=temp["pub_month"]=temp["pub_year"]=temp["pub_time"]= temp["image"]=" " 
                    
                    temp["id"] = post.id 
                    
                    temp["title"] = post.title #post title
                    
                    try:
                        temp["link"] = post.link.split("/?utm_source")[0]
                    except:
                        temp["link"] = post.link
                    
                    dict_elem = link_preview.generate_dict(temp["link"])

                    temp["author"] = post.author
                    
                    temp["pub_day"] = post.published.replace(",","").split(" ")[0]
                    
                    temp["pub_date"] = post.published.split(" ")[1]
                    
                    temp["pub_month"] = post.published.split(" ")[2]
                    
                    temp["pub_year"] = post.published.split(" ")[3]
                    
                    temp["pub_time"] = post.published.split(" ")[4:-1]
                    
                    
                    try: #image
                        try:
                            soup = BSHTML(post.summary, "lxml")
                            images = soup.findAll('img')
                            for image in images:
                                temp["image"] = image['src']
                            
                        except:
                            if str(dict_elem["image"]).endswith(".jpg") or str(dict_elem["image"]).endswith(".png") or str(dict_elem["image"]).endswith(".jpeg"):
                                temp["image"] = dict_elem['image']      
                    except:
                        try:
                            if 'media_content' in post:
                                # Loop through all the 'media_content' elements
                                mediaCount = 0
                                for media in post.media_content:
                                    # Check if the 'medium' attribute of the element is 'image'
                                    if media.get('medium') == 'image':
                                        # Print the URL of the preview image
                                        temp["image"] = media.get('url')
                                        # print(media.get('url'))
                                        mediaCount +=1
                                    
                                    if mediaCount ==1:
                                        break
                        except:
                            temp["image"] = " "

                    # temp["tags"] = [tag.term for tag in post.tags] #output in list
                    # temp["tags"] = ' '.join([str(elem+"↑") for elem in [tag.term for tag in post.tags]]) #output in string #working
                    # temp["image"] = (post.media_content[0]).get('url')
                    
                    try: #summary
                    # temp["summary"] = re.sub("\n", "", re.sub('<[^<]+?>', '', post.summary).replace("&#8230;", "... ")) # full summary
                        try:
                            soup = BSHTML(post.summary, "lxml")
                            temp["summary"] = (str(re.sub("\n", "", re.sub('<[^<]+?>', '', " ".join(str(listToString(str(soup.findAll('p'))).strip().replace("[","")).split(" ",15)[0:15])).replace(",", "").replace('"', '').replace("'", "")) + "..."))  #summary upto 15 words
                        except:
                            temp["summary"] = str(re.sub("\n", "", re.sub('<[^<]+?>', '', " ".join(str(t) for t in post.summary.split(" ",15)[0:15])).replace(",", "").replace('"', '').replace("'", "")) + "...")  #summary upto 15 words
                    except:
                        temp["summary"] = post.summary
            except:
                pass

            post_list.append(temp)
            postCount += 1

        # storing lists of posts in the dictionary
        posts_details = post_list

        return posts_details,postCount  # returning the details which is dictionary
    else:
        return None       