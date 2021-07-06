# flask-rest-companies-ner
Flask REST API micro-service with a single resource ` ScanText ` for extracting company names and confidence scores from a given piece of text.

### Requirements:
- torch (>=1.9.0)
- transformers (>=4.8.2)
- flask (>=1.1.2)
- flask-restful (>=0.3.9)

### Run API Server: 

```
python app.py
```

sample query: 
```
curl --location --request POST 'http://127.0.0.1:5000/' \
--form 'text="Contrary to what one might expect, most companies in this industry are small. This is because, although the product may be complicated, only a small investment is needed to fund the manufacture of many types of electronic components, especially in the software segment of this industry. However, these small companies are often bought by big revenue earners once they develop a hit product. Among computer hardware producers, the top names are Hitachi and Hewlett-Packard. Dell has been known for its direct-sale marketing strategy, yet in the rough times for PC’s of late has seen a considerable decline. The smaller companies that are not bought up must focus on differentiating their products and developing the brand name to compete with the diverse portfolios of the big companies.
    As for software companies, Microsoft Corp., IBM, Google and Oracle Corp. rule the roost. These companies should not sit too easily though since recently consumer electronics products have been merging with products from the computer industry, for example phones now have Internet capability, as do game consoles, PDAs, and many other items. This convergence means that companies can expect increased competition from industries who were not previously direct competitors. Companies, such as Apple, have grown to be giants in their own right by offering both hardware and software. This business model has led other companies that have traditionally focused exclusively on software to also enter the hardware production industry.
       As for software companies, Microsoft Corp., IBM, Google and Oracle Corp. rule the roost. These companies should not sit too easily though since recently consumer electronics products have been merging with products from the computer industry, for example phones now have Internet capability, as do game consoles, PDAs, and many other items. This convergence means that companies can expect increased competition from industries who were not previously direct competitors. Companies, such as Apple, have grown to be giants in their own right by offering both hardware and software. This business model has led other companies that have traditionally focused exclusively on software to also enter the hardware production industry.
   "'
```
sample output:
```
{
    "Apple": 0.9988998174667358,
    "Corp": 0.9990662932395935,
    "Dell": 0.9994696974754333,
    "Google": 0.9990136623382568,
    "Hewlett-Packard": 0.999359168112278,
    "Hitachi": 0.9991354942321777,
    "IBM": 0.9993434548377991,
    "Microsoft": 0.9996258616447449,
    "Oracle": 0.9993470907211304
}
```

### Run client Tests:

```
pytest
```

### Build a Docker Image for platform independence (could not be tested due to local docker environment issues, but it should work)
```
docker build .
```
