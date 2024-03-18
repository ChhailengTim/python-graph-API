import requests

def on_completed(response):
    if response.status_code == 200:
        print(response.json())
    else:
        print("Error:", response.json())

def make_graph_request(user_id='tma092444436'):
    url = "https://graph.facebook.com/v19.0/tma092444436"
    access_token = "EAABsbCS1iHgBO9ekqoxC6g5XPy7bZA1iHd4ccvIJc6VFEmBxuN6fKzZAnPWEF9TU6ATPPPQqkgZA4NB1DE0ffTfp2P0DSyy7ZCLsOhvIsYyuNyOlw9dPuhyqHs1xDfN9qiIjQoJUhhlJ7ZC9dtze1N99y3p8vaXMNkpFfc3ZBsuiwqo22Fi5WYWMp1iwZDZD"
    params = {'access_token': access_token}
    response = requests.get(url, params=params)
    on_completed(response)

make_graph_request()
