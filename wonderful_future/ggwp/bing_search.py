import json
import urllib, urllib2
import sys
import httplib, urllib, base64
reload(sys)
sys.setdefaultencoding('utf8')

# Add your BING_API_KEY

BING_API_KEY = 'e8942d7635484dbcbe00eb21664c0df7'

def run_query(search_terms):
    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': 'e8942d7635484dbcbe00eb21664c0df7',
    }
    query = "'{0}'".format(search_terms)
    params = urllib.urlencode({
        # Request parameters
        'q': query,
        'count': '10',
        'offset': '0',
        'mkt': 'zh-CN',
        'safeSearch': 'Moderate',
    })
    results =[]
    try:
        conn = httplib.HTTPSConnection('api.cognitive.microsoft.com')
        conn.request("GET", "/bing/v5.0/search?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        json_response = json.loads(data)
        for result in json_response['webPages']['value']:
            results.append({
                'title': result['name'],
                'link': result['url'],
                'summary': result['snippet']})
        print(data)
        conn.close()
    except Exception as e:
        print  "Error when querying the Bing API: ", e
    return results

def main():
    # Query, get the results and create a variable to store rank.
    query = raw_input("Please enter a query: ")
    results = run_query(query)
    rank = 1

    # Loop through our results.
    for result in results:
        # Print details.
        print "Rank {0}".format(rank)
        print result['name']
        print result['']
        print

        # Increment our rank counter by 1.
        rank += 1


if __name__ == '__main__':
    main()