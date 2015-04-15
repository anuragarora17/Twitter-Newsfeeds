from newsfeeds.models import Country, News
from get_trending_tags import get_articles, get_urls, get_tags

all_countries = Country.objects.all()
list_1 = all_countries[:5]
list_2 = all_countries[5:10]
list_3 = all_countries[10:15]
list_4 = all_countries[15:]


def update(country_list):
    for country in country_list:
        keywords = get_tags(country.code)
        for k_word in keywords:
            urls = get_urls(k_word[1])
            for url in urls:
                article = get_articles(url)
                if not article.get('errorCode'):
                    if article.get('image_url'):
                        news = News(
                            tag=k_word[0], heading=article.get('title'),
                            body=article.get('text'),
                            link=url,
                            country=country,
                            image_url=article.get('image_url'),
                            )
                    else:
                        news = News(
                            tag=k_word[0],
                            heading=article.get('title'),
                            body=article.get('text'),
                            link=url,
                            country=country,
                            image_url='',
                            )
                    news.save()
        print 'Updated tweets of ' + country.name