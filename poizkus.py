

vzorec_deli=r'<!--title, author, fandom-->(.*?)</dl>' #shit works

naslov=r'<h4 class="heading">.*?>(.*?)</a>'
avtor=r'<a rel="author" .*?>(.*?)</a>'

jezik=r'<dd class="language" .*?>(.*?)</dd>'
besede=r'<dd class="words">(.*?)</dd>'
chapters1=r'<dd class="chapters"><.*?>(.*?)</a>/(.*?)</dd>'
chapters2=r'<dd class="chapters">(.*?)/(.*?)</dd>'

kolekcije=r'<dd class="collections"><a .*?>(.*?)</a>'
komentarji=r'<dd class="comments"><a href=".*?">(.*?)</a>'
kudos=r'<dd class="kudos"><a .*?>(.*?)</a>'
bookmarks=r'<dd class="bookmarks"><a .*?>(.*?)</a>'
hits=r'<dd class="hits">(.*?)</dd>'

datum=r'<p class="datetime">(.*?)</p>'

###################################################

link= "https://archiveofourown.org/works?commit=Sort+and+Filter&work_search%5Bsort_column%5D=kudos_count&work_search%5Bother_tag_names%5D=&work_search%5Bexcluded_tag_names%5D=&work_search%5Bcrossover%5D=&work_search%5Bcomplete%5D=&work_search%5Bwords_from%5D=&work_search%5Bwords_to%5D=&work_search%5Bdate_from%5D=&work_search%5Bdate_to%5D=&work_search%5Bquery%5D=&work_search%5Blanguage_id%5D=&tag_id=Harry+Potter+-+J*d*+K*d*+Rowling"

vzorci=[naslov,avtor,jezik,besede,kolekcije,komentarji,kudos,bookmarks, hits, datum]
imena_vzorci=['naslov', 'avtor', 'jezik','število besed','kolekcije', 'komentarji', 'kudos', 'bookmarks', 'hits', 'datum']





