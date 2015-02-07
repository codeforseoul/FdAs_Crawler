def get_page(page):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""

def union(a,b):
    i=0
    while i<len(b):
        if b[i] not in a:
            a.append(b[i])
        i=i+1
    return a


def get_next_link(content):
    '''This function takes a string that represents the HTML content of a webpage
    and return a url of a link it finds in it, and the the index of the last position
    it already parsed'''
    start_index_link = content.find('<a href=')
    if start_index_link == -1 : # if there is no link in a page (link not found)
        return None, 0
    start_index_quote = content.find('"', start_index_link)
    end_ind_quote = content.find('"', start_index_quote + 1)
    url = content[start_index_quote+1:end_ind_quote]
    return url, end_ind_quote


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
print crawl_web('http://www.udacity.com/cs101x/index.html')
'''

