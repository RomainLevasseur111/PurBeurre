
recup NB_PAGEPRODUCT*20 codebar
pour chaque code bar :
result.add((cat, code bar))

c

result = [(cat1, prod1), (cat1, prod2), (cat2, prod1)...]


def prodcat(cat, link):
    i = 1
    urls = []
    while i < NB_PAGEPRODUCT + 1:
        urls.append(link+"/"+str(i))
        i += 1
    for l in urls :
        response = requests.request("GET", l+".json")
        json_prod = response.json()
        products_prod = json_prod.get('products')
        product_code = [(data.get('id'),)for data in products_prod]
        for elem in product_code :
            Categoryproduct(cat, elem).save()
