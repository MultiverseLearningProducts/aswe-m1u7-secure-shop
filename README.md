# SecureShop

Welcome to SecureShop, a fictional e-commerce platform. This project is designed for evaluating and improving code security using various tools.

**IMPORTANT: THIS REPO IS A PURPOSEFULLY INSECURE WEB APP - USE WITH CAUTION**

## Features

- Search for products
- Add new products
- Submit feedback

## Getting Started

Follow these instructions to set up and run the SecureShop application on your local machine.

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- pip (Python package installer)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/MultiverseLearningProducts/aswe-m1u7-secure-shop.git
    cd secureshop
    ```

2. **Set up a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/Scripts/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install
    ```

4. **Initialize the database:**

    - Run the database initialization script:

      ```bash
      python init_db.py
      ```

### Running the Application

1. **Start the Flask app:**

    ```bash
    python app.py
    ```

2. **Access the application:**

    Open your web browser and navigate to `http://127.0.0.1:5000`.

### Usage

- **Home Page:**
  - Visit `http://127.0.0.1:5000` to see the welcome message.

- **Search for Products:**
  - Visit `http://127.0.0.1:5000/search?query=your_query` to search for products by name.

- **Add a Product:**
  - Send a POST request to `http://127.0.0.1:5000/add_product` with form data:
    - `name`: The name of the product
    - `price`: The price of the product

- **Submit Feedback:**
  - Send a POST request to `http://127.0.0.1:5000/submit_feedback` with form data:
    - `feedback`: Your feedback

### Security Evaluation

To evaluate the security of this codebase, consider using the following tools:

- **Static Code Analysis:** Tools like SonarQube
- **Dynamic Analysis:** Tools like OWASP ZAP
- **Specialized Python Security Analysis:** Tools like Bandit

Refer to the respective tool's documentation for setup and usage instructions.

### Contributing

If you would like to contribute to this project, please create a fork and submit a pull request with your changes.
