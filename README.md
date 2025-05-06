# 🛒 Checkout Kata

A simple web-based shopping cart application where users can view products, add them to the cart, and proceed to checkout. It supports product-specific discount offers and displays a dynamic cart count.

---

## 🚀 Features

- View list of products with prices and discounts
- Add products to cart with quantity tracking
- View cart count dynamically
- Simple checkout navigation
- Highlighted offers and image previews

---

## 🧰 Tech Stack

- HTML, CSS, JavaScript (Frontend)
- Python (Django or Flask assumed)
- REST API for product and cart operations

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/gary1998/agrichain-assessment.git
cd agrichain-assessment
````

### 2. Create a Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations

```bash
python manage.py migrate
```

### 5. Start the Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` or as shown in your terminal.

---

## 🧪 How to Use

### 📥 1. Add New Products

Use your admin panel or API to add new products. Example fields:

```json
{
  "name": "Apple",
  "unit_price": 10,
  "discount_qty": 3,
  "discount_price": 25,
  "image": "https://example.com/apple.jpg"
}
```

Endpoint (example):

```http
POST /api/products/
```

> All other operations on Products can also be done via admin panel or the CRUD APIs. 
---

### 🛒 2. Add to Cart

Each product card has an **"Add to Cart"** button. Clicking it:

* Adds the item to your cart via `POST /api/add-to-cart/`
* Updates the cart count in real-time

---

### 💳 3. Checkout

Click the **"Checkout"** button on the bottom-right of the screen. It navigates to `/checkout`, where the cart summary and further actions (payment/order) can be implemented.

---

## 🛠 API Overview

| Endpoint                  | Method | Description                              |
| ------------------------- | ------ | ---------------------------------------- |
| `/api/products/`          | GET    | Fetch all available products             |
| `/api/add-to-cart/`       | POST   | Add a product to the cart                |
| `/api/checkout/`          | GET    | Fetch cart summary                       |
| `api/reduce-from-cart/`   | POST   | Reduce the product quantity from cart    |
| `api/remove-from-cart/`   | POST   | Remove the product from cart             |

> ⚠️ CSRF token handling is required for POST operations.
