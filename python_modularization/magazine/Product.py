import python_modularization.magazine.utils as utils


def getproductlist() -> [str]:
    products = ['Product 2', 'Product 1', 'Product 3']
    return utils.sortlist(products)

