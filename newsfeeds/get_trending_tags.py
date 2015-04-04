import twitter
import json


def get_tags(woe_id):
    """
    takes woe id of the country and uses twitter api to get top #tags
    and news of that country
    :param woe_id: unique WOE ID of the country
    :return: list of trending #tags and top news from twitter
    """
    consumer_key = 'NNWRNbrJAAovWOkvlNuPh6WOL'
    consumer_secret = 'rTtPwwRNP2Pfs84jycp2It0SsVzGa9oRcmqtYmoJDGCUbdE8Ml'
    oauth_token = '2638839127-niBkABwiXSo4HwNJPc0n0eMVp7AB4cJPIwh3nfN'
    oauth_token_secret = 'PSfT6Pgx3smsRVjRIEkVbnDkH6ngkgQX6iv4luuMRM4nc'

    auth = twitter.oauth.OAuth(oauth_token, oauth_token_secret,
                               consumer_key, consumer_secret)

    # instantiating twitter api to get top #tags and news
    twitter_api = twitter.Twitter(auth=auth)

    # WORLD_WOE_ID = 1
    # IN_WOE_ID = 23424848
    in_woe_id = woe_id
    # Prefix ID with the underscore for query string parameterization.
    # Without the underscore, the twitter package appends the ID value
    # to the URL itself as a special case keyword argument.

    #world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
    country_trends = twitter_api.trends.place(_id=in_woe_id)
    return country_trends

if __name__ == '__main__':
    india_trends = get_tags(23424848)
    #print json.dumps(world_trends, indent=1)
    print json.dumps(india_trends, indent=1)

    for trend in india_trends:
        for key in trend["trends"]:
            print key["name"]