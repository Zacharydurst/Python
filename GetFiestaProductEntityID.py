import json
import requests

def grab_token():
    url = "https://uat-xprtbackend.xenial.com/integrator/token"
    payload = {"key_id": "dea35e18-7373-4861-bbca-61da409c5fa8",
               "secret_key": "61d2e136-38af-4319-88b1-6bdb35f20146"}

    payload = json.dumps(payload)
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "30640197-710b-458c-bbf6-30841d335a34"
    }
    response = requests.request("POST", url, data=payload, headers=headers, verify=False)
    return response.text


def grab_products(token):
    url = 'https://uat-dmbackend.xenial.com/product/current?effective_date=2019-07-25T17:25:52.470Z&$skip=0&$top=10000&include_audit=true' 

    #querystring = {"effective_date":"2019-07-25T17:25:52.470Z","$skip":"0","$top":"10000","include_audit":"true"}

    headers = {
    'Content-Type': "application/json",
    'Authorization': "Bearer " + str(token),
    'X-Company-Id': "5c3e4162d313660019f9b5cb",
    'X-Site-Ids': "5c409f408df06b001d3a1a63",
    'User-Agent': "PostmanRuntime/7.15.2",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "e020816f-48d6-43de-8e26-118267a6c18e,242ba347-8488-4ded-8a7b-e744ce85761e",
    'Host': "uat-dmbackend.xenial.com",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

    r = requests.get(url=url, headers=headers, verify=False)
    if r.status_code != 200:
        print(f"error: {r.json()}")

    return r.json()

if __name__ == "__main__":
    token = grab_token()
    products = grab_products(token)
    print(len(products["items"]))
    count = 0
    for product in products["items"]:
        try:
            bc = product["bundle_components"]
        except:
            continue
        
        for b in bc:
            try:
                choices = b["product_choices_entity_ids"]
            except:
                continue

            count += len(choices)

    print(count)
