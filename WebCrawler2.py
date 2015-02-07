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
index=[]
print index
add_to_index(index,'udacity','http://udacity.com')
print index
add_to_index(index,'computing','http://acm.org')
print index
add_to_index(index,'udacity','http://npr.org')
print index 
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
print look_up(index,'udacity')            
print look_up(index,'computing')
'''
   

def add_page_to_index(index,url,content):
    content_splited=content.split()
    for word in content_splited:
        add_to_index(index, word, url)
    
'''
index=[]
add_page_to_index(index,'fake.test','this is a test')
print index
add_page_to_index(index,'real.test','this is not a test')
print index
'''
            
            
            
            
            