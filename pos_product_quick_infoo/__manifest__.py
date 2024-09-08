{
    "name": "PoS Product Quick Info",
    "version": "16.0.1.0.2",
    "summary": "Display product info by one click in Point of Sale",
    "author": "Abdelwahab El dweik",
    "category": "Point Of Sale",
    "license": "AGPL-3",
    "depends": ["point_of_sale"],
    "data": ["views/res_config_settings_view.xml"],
    "assets": {
        "point_of_sale.assets": [
            "pos_product_quick_infoo/static/src/css/pos.css",
            "pos_product_quick_infoo/static/src/js/Screens/ProductScreen/ProductItem.js",
            "pos_product_quick_infoo/static/src/xml/Screens/ProductScreen/ProductItem.xml",
        ],
    },
    "installable": True,
}
