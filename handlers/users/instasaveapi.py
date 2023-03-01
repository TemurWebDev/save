import requests




def instasave(shortcode):

    url = "https://instagram-scraper-2022.p.rapidapi.com/ig/post_info/"

    querystring = {"shortcode":shortcode}

    headers = {
        "X-RapidAPI-Key": "979fa7040amshd382fd8585d8c91p1b5ae9jsn7bb44fd0ece3",
        "X-RapidAPI-Host": "instagram-scraper-2022.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()['video_url']






