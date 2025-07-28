from .products import products_bp


def register_routes(app):
    app.register_blueprint(products_bp, url_prefix='/products')
