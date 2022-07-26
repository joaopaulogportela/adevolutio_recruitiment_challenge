from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from collections import Counter

from urllib.request import urlopen
import json


class Order:

    def __init__(self, id, brand_id, customer_name, reference, order_date, price_total):
        self.__id = id
        self.__brand_id = brand_id
        self.__customer_name = customer_name
        self.__reference = reference
        self.__order_date = order_date
        self.__price_total = price_total

    def to_dict(self):
        return {'id': self.id,
                'brand_id': self.brand_id,
                'customer_name': self.customer_name,
                'reference': self.reference,
                'order_date': self.order_date,
                'price_total': self.price_total}

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def del_id(self):
        del self.__id

    id = property(get_id, set_id, del_id)

    def get_brand_id(self):
        return self.__brand_id

    def set_brand_id(self, brand_id):
        self.__brand_id = brand_id

    def del_brand_id(self):
        del self.__brand_id

    brand_id = property(get_brand_id, set_brand_id, del_brand_id)

    def get_customer_name(self):
        return self.__customer_name

    def set_customer_name(self, customer_name):
        self.__customer_name = customer_name

    def del_customer_name(self):
        del self.__customer_name

    customer_name = property(get_customer_name, set_customer_name, del_customer_name)

    def get_reference(self):
        return self.__reference

    def set_reference(self, reference):
        self.__reference = reference

    def del_reference(self):
        del self.__reference

    reference = property(get_reference, set_reference, del_reference)

    def get_order_date(self):
        return self.__order_date

    def set_order_date(self, order_date):
        self.__order_date = order_date

    def del_order_date(self):
        del self.__order_date

    order_date = property(get_order_date, set_order_date, del_order_date)

    def get_price_total(self):
        return self.__price_total

    def set_price_total(self, price_total):
        self.__price_total = price_total

    def del_price_total(self):
        del self.__price_total

    price_total = property(get_price_total, set_price_total, del_price_total)
    
class Deliveries:
    products = {}

    def __init__(self, id, order_id, shipped, products):
        self.__id = id
        self.__order_id = order_id
        self.__shipped = shipped
        self.__products = products

    def to_dict(self):
        return {'id': self.id,
                'order_id': self.order_id,
                'shipped': self.shipped,
                'products': self.products}

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def del_id(self):
        del self.__id

    id = property(get_id, set_id, del_id)

    def get_order_id(self):
        return self.__order_id

    def set_order_id(self, order_id):
        self.__order_id = order_id

    def del_order_id(self):
        del self.__order_id

    order_id = property(get_order_id, set_order_id, del_order_id)

    def get_shipped(self):
        return self.__shipped

    def set_shipped(self, shipped):
        self.__shipped = shipped

    def del_shipped(self):
        del self.__shipped

    shipped = property(get_shipped, set_shipped, del_shipped)

    def get_products(self):
        return self.__products

    def set_products(self, products):
        self.__products = products

    def del_products(self):
        del self.__products

    products = property(get_products, set_products, del_products)

def get_deliveries():
    url_deliveries = "https://evolutio.pt/media/challenges/deliveries.json"

    response_deliveries = urlopen(url_deliveries)
    json_data_deliveries = json.loads(response_deliveries.read())

    nova_deliveries = []

    for index in range(len(json_data_deliveries['data'])):
        id_dto = json_data_deliveries['data'][index]['id']
        order_id_dto = json_data_deliveries['data'][index]['order_id']
        shipped_dto = json_data_deliveries['data'][index]['shipped']
        products_dto = {}
        for index2 in range(len(json_data_deliveries['data'][index]['products'])):
            products_dto[json_data_deliveries['data'][index]['products'][index2]['product_name']] = \
                json_data_deliveries['data'][index]['products'][index2]['quantity']

        nova_deliveries.append(Deliveries(id_dto, order_id_dto, shipped_dto, products_dto))
    return nova_deliveries

def get_orders():
    url_orders = "https://evolutio.pt/media/challenges/orders.json"

    response_orders = urlopen(url_orders)
    json_data_orders = json.loads(response_orders.read())

    nova_order = []

    for index in range(len(json_data_orders['data'])):
        id_dto = (json_data_orders['data'][index]['id'])
        brand_id_dto = (json_data_orders['data'][index]['brand_id'])
        customer_name_dto = (json_data_orders['data'][index]['customer_name'])
        reference_dto = (json_data_orders['data'][index]['reference'])
        order_date_dto = (json_data_orders['data'][index]['order_date'])
        price_total_dto = (json_data_orders['data'][index]['price_total'])

        nova_order.append(
            Order(id_dto, brand_id_dto, customer_name_dto, reference_dto, order_date_dto, price_total_dto))
    return nova_order

def filter_orders_by_brand_id(orders, brand_id_query):
    return [order for order in orders if order.get_brand_id() == brand_id_query]

def filter_deliveries_by_order_id(filtered_orders, deliveries):
    filtered_deliveries_by_order_id = []

    for order in filtered_orders:
        for delivery in deliveries:
            if order.get_id() == delivery.get_order_id():
                filtered_deliveries_by_order_id.append(delivery)

    return filtered_deliveries_by_order_id

def dump_json_deliveries_orders_filtered(filtered_orders, filtered_deliveries):
    dict_aux = {'orders': [order.to_dict() for order in filtered_orders],
                'deliveries': [delivery.to_dict() for delivery in filtered_deliveries]}
    return json.dumps(dict_aux, ensure_ascii=False)

def filter_orders_by_id(orders, id_query):
    return [order for order in orders if order.get_id() == id_query]

def filter_orders_by_reference(orders, reference_query):
    return [order for order in orders if order.get_reference() == reference_query]

def sum_delivered_products(deliveries_query):
    sum_products = {}

    for index in range(len(deliveries_query)):
        if(deliveries_query[index].shipped):
            if index == 0:
                sum_products = dict(Counter(deliveries_query[index].get_products()))
            else:
                sum_products = dict(Counter(sum_products) + Counter(deliveries_query[index].get_products()))
    dict_return = {}
    dict_return['products']=sum_products
    return dict_return
   
def dump_json_sum_products(sum_products_delivered_id):
    dict_aux = {}
    dict_aux['products'] = [sum_products_delivered_id]
    return json.dumps(dict_aux)



def query_by_brand_id(request):
    
    brand_id=(request.GET.get('brand_id', None))
    
    if request.method =='GET':
        if brand_id != None:
            brand_id=int(brand_id)
            
            orders = get_orders()
            deliveries = get_deliveries()

            filtered_orders= filter_orders_by_brand_id(orders, brand_id)

            filtered_deliveries = filter_deliveries_by_order_id (filtered_orders, deliveries)

            json_dict={}
            json_dict['orders']=[order.to_dict() for order in filtered_orders]
            json_dict['deliveries']=[delivery.to_dict() for delivery in filtered_deliveries]

            return JsonResponse(json_dict,safe=False,json_dumps_params={'indent': 2,'ensure_ascii':False})
        return JsonResponse({'Bad_Request':'Passed invalid parameters'})


def query_products_by_id_or_reference(request):
    
    id=(request.GET.get("id", None)) 
          
    reference=str(request.GET.get("reference", None)) 
    if request.method =='GET':
        if (reference == None and id == None):
            return JsonResponse({'Bad_Request':'Passed no parameters'})   
        
        if id == None:            
            orders = get_orders()
            deliveries = get_deliveries()

            filtered_orders = filter_orders_by_reference(orders, reference)
            
            deliveries_query = filter_deliveries_by_order_id(filtered_orders, deliveries)

            products_sum = sum_delivered_products(deliveries_query)
                        
            return JsonResponse(products_sum, safe=False, json_dumps_params={'indent': 2,'ensure_ascii':False})
            
        else:
            ident = int(id)
            
            orders = get_orders()
            deliveries = get_deliveries()

            filtered_orders = filter_orders_by_id(orders, ident)
            deliveries_query = filter_deliveries_by_order_id(filtered_orders, deliveries)

            products_sum = sum_delivered_products(deliveries_query)

            return JsonResponse(products_sum, safe=False, json_dumps_params={'indent': 2,'ensure_ascii':False})


        
# Create your views here.
