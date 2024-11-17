from flask import Flask
from routes.users import users_bp
from routes.products import products_bp
from routes.sales import sales_bp

app = Flask(__name__)

# Registro de Blueprints
app.register_blueprint(users_bp, url_prefix="/api/users")
app.register_blueprint(products_bp, url_prefix="/api/products")
app.register_blueprint(sales_bp, url_prefix="/api/sales")

@app.route("/")
def home():
    return {"message": "API do Sistema de Vendas está ativa!"}

if __name__ == "__main__":
    app.run(debug=True)
