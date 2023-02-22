import requests




def instasave(shortcode):

    url = "https://instagram-scraper-2022.p.rapidapi.com/ig/post_info/"

    querystring = {"shortcode":shortcode}

    headers = {
        "X-RapidAPI-Key": "d8a9bb2408msh636654a651c6ac6p104989jsn500d73ab19a9",
        "X-RapidAPI-Host": "instagram-scraper-2022.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    return response.json()['video_url']






