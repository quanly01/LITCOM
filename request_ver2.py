import requests
import json

# Set Shopify API credentials
API_KEY = "c02d23ed5ecbd19a0c1d8a5e306e13c3"
API_SECRET = "6fe7604ea97cf70d790c673a157923e2"
API_PASS = "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"

# Set shop domain
SHOP_DOMAIN = "{}:{}@always2k23.myshopify.com".format(API_KEY,API_PASS)

#set end point for collection, product
end_point_for_smart_collection = "smart_collections.json"
end_point_for_custom_collection = "custom_collections.json"
end_point_for_product = "products.json"
end_point_for_customer = "customers.json"
end_point_for_orders = "orders.json"

#Create smart collection
def create_smart_collection():
    # Create the smart collection data
    data = {
	    "smart_collection": {
            "title": "Shoe's Smart Collection",
            "body_html": "Products which belong to shoe’s category manually go to this custom collection.",
            "published_scope": "web",
            "rules": [
                    {
                        "column": "type",
                        "relation": "equals",
                        "condition": "Shoes",
                    }
            ],
        }
    }
    
    url = "https://%s/admin/api/2023-04/" % SHOP_DOMAIN + end_point_for_smart_collection
    print(url)
    headers = {
        "Authorization": "Dale %s" % API_KEY, 
        "Content-Type": "application/json",
    }

    # Make the API request
    response = requests.post(url, data=json.dumps(data), headers=headers)

    # Check the response status code
    if response.status_code == 201:
    # The smart collection was created successfully
        print("Smart collection created successfully")
    else:
        # An error occurred
        print("Error creating smart collection: %s" % response.status_code)
    return response.json()

#Create custom collection
def create_custom_collection():
    # Create the custom collection data
    data = {
	    "custom_collection": {
            "title": "Highlight Shoes Custom Collection.",
            "body_html": "Products which belong to shoe’s category manually go to this custom collection.",
            "published_scope": "web",
        }
    }
    
    url = "https://%s/admin/api/2023-04/" % SHOP_DOMAIN + end_point_for_custom_collection
    print(url)
    headers = {
        "Authorization": "Dale %s" % API_KEY, 
        "Content-Type": "application/json",
    }

    # Make the API request
    response = requests.post(url, data=json.dumps(data), headers=headers)

    # Check the response status code
    if response.status_code == 201:
    # The smart collection was created successfully
        print("Custom collection created successfully")
    else:
        # An error occurred
        print("Error creating custom collection: %s" % response.status_code)
    return response.json()

#Create product with no option
def create_product():
    # Create product with no option
    data = {
	    "product": {
            "title": "AF1 sneakers",
            "body_html": "AF1 full white",
            "vendor": "always2k23",
            "product_type": "Test",
            "status": "active",
            "published_scope": "global",
            "tags": "Test",
            "variants": [],
            "options": [],
            "images": [],
            "image": None,
        }
    }
    
    url = "https://%s/admin/api/2023-04/" % SHOP_DOMAIN + end_point_for_product
    print(url)
    headers = {
        "Authorization": "Dale %s" % API_KEY, 
        "Content-Type": "application/json",
    }

    # Make the API request
    response = requests.post(url, data=json.dumps(data), headers=headers)

    # Check the response status code
    if response.status_code == 201:
    # The smart collection was created successfully
        print("Product created successfully")
    else:
        # An error occurred
        print("Error creating product: %s" % response.status_code)
    return response.json()

def add_option(product_id):
    # Create product with no option
    end_point_for_specific_product = f"products/{product_id}.json"
    data = {
	    "product": {
            "variants": [
                    {
                        "option1": "Red",
                        "option2": "42"
                    },
                    {
                        "option1": "White",
                        "option2": "43"
                    }
                ],
            "options": [
                    {
                        "name": "Color",
                        "position": 1,
                        "values": [
                            "Red",
                            "White",
                            "Green",
                            "Blue",
                            "Orange"
                        ]
                    },
                    {
                        "name": "Size",
                        "position": 2,
                        "values": [
                            "35", "36", "37", "38", "39", "40", "41", "42", "43", "44"
                        ]
                    }
                ],
        }
    }
    
    url = "https://%s/admin/api/2023-04/" % SHOP_DOMAIN + end_point_for_specific_product
    print(url)
    headers = {
        "Authorization": "Dale %s" % API_KEY, 
        "Content-Type": "application/json",
    }

    # Make the API request
    response = requests.put(url, json = data, headers=headers)

    # Check the response status code
    if response.status_code == 201:
    # The smart collection was created successfully
        print("Product variants created successfully")
    else:
        # An error occurred
        print("Error creating product variant: %s" % response.status_code)
    return response.json()

#Update product

def update_price(variants_id: int):
    end_point = f"variants/{variants_id}.json"
    data = {
	     "variant": {
            "price": 100,
            "compare_at_price": 150,
            "inventory_management": "shopify",
            }
    }
    
    url = "https://%s/admin/api/2023-04/" % SHOP_DOMAIN + end_point
    print(url)
    headers = {
        "Authorization": "Dale %s" % API_KEY, 
        "Content-Type": "application/json",
    }

    # Make the API request
    response = requests.put(url, data=json.dumps(data), headers=headers)

    # Check the response status code
    if response.status_code == 201:
    # The smart collection was created successfully
        print("Update Price created successfully")
    else:
        # An error occurred
        print("Error Update Price: %s" % response.status_code)
    return response.json()

def update_image(product_id: int):
    end_point = f"products/{product_id}/images.json"
    data = {
	    "image": {
            "product_id": product_id,
            "src": "https://www.kicksonfire.com/wp-content/uploads/2022/07/Nike-Air-Force-1-Low-Since-82-White-DJ3911-100-Release-Date.jpeg"
        }
    }
    
    url = "https://%s/admin/api/2023-04/" % SHOP_DOMAIN + end_point
    print(url)
    headers = {
        "Authorization": "Dale %s" % API_KEY, 
        "Content-Type": "application/json",
    }

    # Make the API request
    response = requests.post(url, data=json.dumps(data), headers=headers)

    # Check the response status code
    if response.status_code == 201:
    # The smart collection was created successfully
        print("Update Image successfully")
    else:
        # An error occurred
        print("Error creating product variant: %s" % response.status_code)
    return response.json()

def update_quantity(inventory_item_id, available):
    end_point = f"inventory_items/{inventory_item_id}.json"
    tracked = {
        "inventory_item": {
            "tracked": True
        }
    }
    url = "https://%s/admin/api/2023-04/" % SHOP_DOMAIN 
    print(url)
    headers = {
        "Authorization": "Dale %s" % API_KEY, 
        "Content-Type": "application/json",
    }
    requests.put(url + end_point, json=tracked, headers=headers)

    endpoint_get_level = f"inventory_levels.json?inventory_item_ids={inventory_item_id}"
    
    inventory_level = requests.get(url + endpoint_get_level, headers=headers)
    print(inventory_level.json())
    location_id = inventory_level.json()["inventory_levels"][0]["location_id"]

    qty = {
        "inventory_item_id": inventory_item_id,
        "location_id": location_id,
        "available": available,
    }

    endpoint_set_qty = "/api/2023-04/inventory_levels/set.json"

    # Make the API request
    response = requests.post(url + endpoint_set_qty, json=qty, headers=headers)

    # Check the response status code
    if response.status_code == 201:
    # The smart collection was created successfully
        print("Update quanity  successfully")
    else:
        # An error occurred
        print("Error update quantity: %s" % response.status_code)
    return response.json()

def update_product(product, available):
    update_image(product['product']['id'])
    for variant in product['variants']:
        update_price(variant['id'])
        update_quantity(variant['inventory_item_id', available])

#Create customer

def create_customer():
    data = {
	    "customer": {
            "first_name": "Myfirst",
            "last_name": "Mylast",
            "email": "custom@example.com",
            "phone": "+555-555-555"
        }
    }
    
    url = "https://%s/admin/api/2023-04/" % SHOP_DOMAIN + end_point_for_customer
    print(url)
    headers = {
        "Authorization": "Dale %s" % API_KEY, 
        "Content-Type": "application/json",
    }

    # Make the API request
    response = requests.post(url, json = data, headers=headers)

    # Check the response status code
    if response.status_code == 201:
    # The smart collection was created successfully
        print("Customers created successfully")
    else:
        # An error occurred
        print("Error creating customer: %s" % response.status_code)
    return response.json()

def add_customer_address(customer_id):
    end_point = f"customers/{customer_id}/addresses.json"
    data = {
	    "customer_address": {
            "customer_id": customer_id,
            "first_name": "Dung",
            "last_name": "Nguyen",
            "company": "LITCOM",
            "address1": "1 hanoi",
            "address2": "2 hai ba trung",
            "city": "Hanoi",
            "province": "HBT",
            "country": "VN",
            "zip": "100000",
            "phone": "123-555-5555",
            "name": "Dung Nguyen",
            "province_code": "HBT",
            "country_code": "VN",
            "country_name": "Vietnam",
            "default": False
        }
    }
    
    url = "https://%s/admin/api/2023-04/" % SHOP_DOMAIN + end_point
    print(url)
    headers = {
        "Authorization": "Dale %s" % API_KEY, 
        "Content-Type": "application/json",
    }

    # Make the API request
    response = requests.post(url, json = data, headers=headers)

    # Check the response status code
    if response.status_code == 201:
    # The smart collection was created successfully
        print("Add customer address successfully")
    else:
        # An error occurred
        print("Error add customer address: %s" % response.status_code)
    return response.json()

#Create orders

def add_order(customer_email):
    data = {
	    "order":{
            "line_items": [
                {
                    "variant_id": 8359429472558,
                    "quantity": 2
                }
            ],
            "customer": {
                "email": customer_email,
            },
            "shipping_address": {
                "first_name": "Dung",
                "address1": "HBT",
                "phone": "555-555-555",
                "city": "Hanoi",
                "zip": "10000",
                "province": "HBT",
                "country": "Viet Nam",
                "last_name": "Nguyen",
                "address2": "",
                "company": None,
                "name": "Dung Nguyen",
                "country_code": "10000",
                "province_code": "10000"
            }
        }
    }
    
    url = "https://%s/admin/api/2023-04/" % SHOP_DOMAIN + end_point_for_orders
    print(url)
    headers = {
        "Authorization": "Dale %s" % API_KEY, 
        "Content-Type": "application/json",
    }

    # Make the API request
    response = requests.post(url, json = data, headers=headers)

    # Check the response status code
    if response.status_code == 201:
    # The smart collection was created successfully
        print("Orders created successfully")
    else:
        # An error occurred
        print("Error creating orders: %s" % response.status_code)
    return response.json()

def main():
    smart_collection = create_smart_collection()
    print()
    custom_collection = create_custom_collection()
    print()
    product_no_option = create_product()
    print()
    product_with_option = create_product()
    print()
    #option = add_option(product_with_option['product']['id']) # error 200 product variants
    print()
    #update_product(product_no_option, 120) # error 200 product variants
    customer = create_customer() #Error creating customer: 422
    print()
    add_customer_address(customer['customer']['id'])
    print()
    order = add_order(customer['customer']['email'])
    print()


if __name__ == '__main__':
    main()
    