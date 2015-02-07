'''
Created on 2014. 12. 29.

@author: Will.Kwon
'''

# Get the contents of the page
def get_page(page):
    import urllib2
    source = urllib2.urlopen(page)
    return source.read()

# Get the next contents of the page after the first url
def get_next_target(page):
    start_link=page.find('<a href=')
    if start_link==-1:
        return None,0 
    else:
        start_quote=page.find('"',start_link)
        end_quote=page.find('"',start_quote+1)
        url=page[start_quote+1:end_quote]
        return url, end_quote

# Use above to print the url gotten
def print_all_links(page):
    while True:
        url, endpos=get_next_target(page)
        if url:
            print url
            page=page[endpos:]
        else:
            break

# Similar to above but save url instead
def get_all_links(page):
    urllist=[]
    while True:
        url, endpos=get_next_target(page)
        if url:
            urllist.append(url)
            page=page[endpos:]
        else:
            break
    return urllist
