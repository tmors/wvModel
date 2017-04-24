import gensim
from gensim.scripts import make_wiki

ans = make_wiki("enwiki-latest-stub-articles19.xml.gz")
print(ans)