import traceback

from django.shortcuts import render
from products.models import Product
from django.db import connection
import logging
# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'main/home.html',{'products': products})


def vulnerable_search(request):
    log = logging.getLogger('django')
    query = request.GET.get('q', '')  # user input

    products = []
    if query:
        # WARNING: vulnerable to SQL injection
        sql = f"SELECT * FROM products_product WHERE name LIKE '%{query}%'"
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                rows = cursor.fetchall()
            for r in rows:
                products.append({'id': r[0], 'name': r[1], 'price': r[2], 'description': r[3]})
        except Exception:
            error = traceback.format_exc()
            log.error("Error in search: " + sql)
    return render(request, 'main/home.html', {'products': products})