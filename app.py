from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('secureshop.db')
    conn.row_factory = sqlite3.Row
    return conn

# Home route
@app.route('/')
def index():
    return "Welcome to SecureShop!"

# Product search route
@app.route('/search')
def search():
    query = request.args.get('query', '')
    print(query)
    conn = get_db_connection()
    sql_query = "SELECT * FROM products WHERE name LIKE '%" + query + "%'"
    results = conn.execute(sql_query).fetchall()
    conn.close()
    
    # Vulnerable to XSS
    result_template = '''
    <h1>Search Results</h1>
    <ul>
        {% for row in results %}
            <li>{{ row['name'] }} - {{ row['price'] }}</li>
        {% endfor %}
    </ul>
    '''
    return render_template_string(result_template, results=results)

# Add product route
@app.route('/add_product', methods=['POST'])
def add_product():
    name = request.form['name']
    price = request.form['price']
    
    conn = get_db_connection()
    conn.execute(f"INSERT INTO products (name, price) VALUES ('{name}', {price})")
    conn.commit()
    conn.close()
    
    return "Product added!"

# Vulnerable buffer overflow route
@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    feedback = request.form['feedback']
    
    buffer = [''] * 10  # Small fixed-size buffer
    for i in range(len(feedback)):
        buffer[i] = feedback[i]  # Potential buffer overflow if feedback is too long
    
    return "Feedback received!"

if __name__ == '__main__':
    app.run(debug=True)
