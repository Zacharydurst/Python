import requests
import json
import argparse

parser = argparse.ArgumentParser()
# parser.add_argument("--num", "number", required=True)

def grab_token():
    url = "https://qa-xprtbackend.xenial.com/integrator/token"
    payload = {"key_id": "480e6b03-b728-4d84-94c6-b3c0c70f88a8",
               "secret_key": "e1a479de-fc37-4e45-be25-3322169d7749"}

    payload = json.dumps(payload)
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "30640197-710b-458c-bbf6-30841d335a34"
    }
    response = requests.request("POST", url, data=payload, headers=headers, verify=False)
    return response.text

def order_full(token):
    url = "https://qa-xooapi.xenial.com/order"

    payload = "{\n  \"store_number\": \"999966\",\n  \"terminal\": {\n    \"id\": \"9\"\n  },\n  \"items\":[{\n    \"product_id\":\"22100\",\n    \"quantity\":1\n    }],\n  \"customer\": {\n    \"id\": \"30562060\",\n    \"first_name\": \"Zack\",\n    \"last_name\": \"Durst\",\n    \"phone_cell\": \"9999999999\",\n    \"loyalty_customer\": false,\n    \"email\": \"zachary.durst@xenial.com\"\n  },\n  \"destination\": {\n    \"id\": \"128\",\n    \"name\": \"Carry Out\"\n  },\n  \"reference_id\": \"dba260af-16d0-41ad-b901-08ce06816b35\",\n  \"comment\": \"Hello!\"\n}"
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer " + str(token),
        'X-Company-Id': "59d114d6261fd0200024e047",
        'X-Site-Ids': "59d11594261fd0200024e050",
        'cache-control': "no-cache",
        'Postman-Token': "75312f67-85da-4ab4-abf6-6afebbeac085"
        }

    response = requests.request("POST", url, data=payload, headers=headers, verify=False)
    response_data = json.loads(response.text)
    order_id = response_data["order"]["_id"]
    

    return order_id

def order_single(token, order_id):
    url = "https://qa-xooapi.xenial.com/order/" + order_id + "/item"

    payload = "{\n  \"items\": [{\n    \"product_id\": \"22100\",\n    \"quantity\": 1\n  }]\n}"
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer " + str(token),
        'X-Company-Id': "59d114d6261fd0200024e047",
        'X-Site-Ids': "59d11594261fd0200024e050",
        }

    response = requests.request("PUT", url, data=payload, headers=headers, verify=False)

    print(response.text)


def send_product(token, order_id):
    url = "https://qa-xooapi.xenial.com/order/" + order_id + "/commit"

    payload = "{\n}"
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer " + str(token),
        'X-Company-Id': "59d114d6261fd0200024e047",
        'X-Site-Ids': "59d11594261fd0200024e050",
        'cache-control': "no-cache",
        'Postman-Token': "d79ae5c8-0691-494f-81aa-34abd57cb99f"
        }

    response = requests.request("PUT", url, data=payload, headers=headers, verify=False)

    print (response.text)

def main():
    quantity = int(input("Enter an order quantity: "))
    while quantity > 0:
        token = grab_token()
        order_id = order_full(token)
        order_single(token, order_id)
        send_product(token, order_id)
        quantity = quantity - 1



    
    
if __name__ == "__main__":
    main()

