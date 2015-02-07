'''
Grabs the contents of a webpage
'''
def get_page(page):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""

'''
Get the union set, discard repetitions
'''
def union(a,b):
    i=0
    while i<len(b):
        if b[i] not in a:
            a.append(b[i])
        i=i+1
    return a

'''
Return the first link found and its end position 
'''
def get_next_link(content):
    start_index_link = content.find('<a href=')
    if start_index_link == -1 : # if there is no link in a page (link not found)
        return None, 0
    start_index_quote = content.find('"', start_index_link)
    end_ind_quote = content.find('"', start_index_quote + 1)
    url = content[start_index_quote+1:end_ind_quote]
    return url, end_ind_quote

'''
Update contents and keep grabbing the links
'''
def get_all_links(page):
    url_list=[]
    while True :
        url, end_pos = get_next_link(page)
        # check if the url is anything but the empty string or None
        if url:
            url_list.append(url)
            page = page[end_pos:]
        else:
            break
    return url_list

'''
Input a seed page, visit all the links and collect links in thier contents
'''
def crawl_web(seed):
    to_crawl=[seed]
    crawled=[]
    while to_crawl:
        page=to_crawl.pop()    # assigns to page the last element of to_crawl and eliminates that element
        if page not in crawled:
            union(to_crawl, get_all_links(get_page(page)))
            crawled.append(page)    # Only add pages not already crawled   
        
    return crawled

'''
For each keyword, add links that are found
'''
def add_to_index(index,keyword,url):
    bFound = False
    for i in index:
        if i[0] == keyword:
            if url not in i[1]:
                i[1].append(url)
            bFound = True
    if not bFound:
        index.append([keyword,[url]])   
      
'''
Input keyword return associated links
'''
def lookup(index,keyword):
    bFound=False
    for entry in index:
        if entry[0]==keyword:
            return index[index.index(entry)] [1]
        bFound=True
    if not bFound:
        return []

'''
split content input, add associated links, append links as new one appears for each existing keyword
'''   
def add_page_to_index(index,url,content):
    content_splited=content.split()
    for word in content_splited:
        add_to_index(index, word, url)
        
'''
Modify pre-defined crawl_web to now do much better job
'''        
def crawl_web(seed):
    to_crawl=[seed]
    crawled=[]
    index=[]
       
    while to_crawl:
        page=to_crawl.pop()    # assigns to page the last element of to_crawl and eliminates that element
        if page not in crawled:
            content=get_page(page)
            add_page_to_index(index,page,content)
            union(to_crawl, get_all_links(content))
            crawled.append(page)    # Only add pages not already crawled   
        
    return index


print crawl_web('http://www.udacity.com/cs101x/index.html')


    
                        