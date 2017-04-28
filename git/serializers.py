import requests
from rest_framework import serializers

from git.models import User


def get_query_params(**kwargs):
    query_params = ""
    for key, value in kwargs.items():
        if 'q' == key:
            query_params += "?q={0}".format(value[0])
        elif 'in' == key:
            query_params += "+in:{0}".format(value[0])
        elif 'respos' in key:
            if key == 'repos__gt':
                query_params += "+repos:>{0}".format(value[0])
            if key == 'repos__lt':
                query_params += "+repos:<{0}".format(value[0])
        elif key == 'location':
            query_params += "+location:{0}".format(value[0])
        elif key == 'language':
            query_params += "+language:{0}".format(value[0])
        elif 'followers' in key:
            if key == 'followers__gt':
                query_params += "+followers:>{0}".format(value[0])
            if key == 'followers__lt':
                query_params += "+followers:<{0}".format(value[0])
    return query_params


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

    def search(self, **kwargs):
        if 'q' not in kwargs:
            return {"errors": {"resource": "Search", "field": "q", "code": "missing"}}
        query_params = get_query_params(**kwargs)
        api_url = "https://api.github.com/search/users"+query_params+"&per_page=100"
        r = requests.get(api_url)
        if r.status_code == 200:
            data = r.json().get('items')
            count = 1
            while r.json().get('total_count') > count*100:
                page = "&per_page=100&page={0}".format(count+1)
                api_url = "https://api.github.com/search/users" + query_params+page
                r = requests.get(api_url)
                data += r.json().get('items')
                count += 1
            return data
        else:
            return r.json()
