# Custom Google-scrapper

## Dependencies
You must have following packages installed :
1. Gensim Module
2. nltk
3. scrapy
4. js2py
5. twisted


## How to run?

1. Run summarization:
    Make sure you are in gensim_summarization directory.
```
python search_query_extraction_using_gensim_summarization
```


2. Run goole-scrapper
```
scrapy crawl search -a keyword=<enter-keyword-for-search>
