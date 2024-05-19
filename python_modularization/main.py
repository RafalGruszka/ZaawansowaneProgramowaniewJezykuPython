'''
1. Stworzyć strukturę plików i katalogów, jak powyżej. Następnie:
 a. w module Product i Order zaimportować moduł utils
 b. w module main zaimportować jedynie moduł Product
'''


import python_modularization.magazine.Product as Product


# Wydruk listy produktów posortowanej alfabetycznie - przykład poprawnego wywołania funkcji getproductlist() z modułu Product
print(Product.getproductlist())

# Przykład błednego wywołania funkcji getorderlist() z modułu Order (nie zaimportowanego w main)
print(getorderlist())
