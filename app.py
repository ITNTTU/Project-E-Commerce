from flask import Flask, render_template, url_for, flash, redirect
from models import db, Product
from forms import ProductForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route("/")
def home():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route("/product/<int:product_id>")
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product.html', product=product)

@app.route("/add", methods=['GET', 'POST'])
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(name=form.name.data, price=form.price.data, description=form.description.data)
        db.session.add(product)
        db.session.commit()
        flash('Product has been added!', 'success')
        return redirect(url_for('home'))
    return render_template('add_product.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
