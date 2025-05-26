from flask import Flask, render_template, request, redirect, url_for

app = Flask(_name_)

# In-memory data storage (replace with a database in a real app)
price_data = {}

@app.route('/')
def index():
    return render_template('index.html', price_data=price_data)

@app.route('/add', methods=['GET', 'POST'])
def add_price():
    if request.method == 'POST':
        product_name = request.form['product_name'].strip().lower()
        supplier = request.form['supplier'].strip()
        price = request.form['price']
        try:
            price = float(price)
        except ValueError:
            return "Invalid price. Please enter a number."

        if product_name not in price_data:
            price_data[product_name] = {}
        price_data[product_name][supplier] = price
        return redirect(url_for('index'))
    return render_template('add.html')

if _name_ == '_main_':
    app.run(debug=True, host='0.0.0.0') # Make it accessible on the network