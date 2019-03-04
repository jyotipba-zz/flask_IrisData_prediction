import requests


def search_image(search_item, image_file):
    subscription_key = "88c0b90804d14a95a7122c0d7d642b15"
    search_url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"
    search_term = search_item

    headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
    params  = {"q": search_term, "license": "public", "imageType": "photo"}


    response = requests.get(search_url, headers=headers, params=params)

    search_results = response.json()
    Image_url = search_results["value"][0]["thumbnailUrl"]

    image_data = requests.get(Image_url)
    #print((image_data.content))

    with open("static/pictures/"+image_file, "wb") as im:
        im.write(image_data.content)
