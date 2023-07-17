# Online-Training-Store

This is a web application for a online store.

**Functionality:**

**1. Superuser:**

Has access to the pages: main, add_product, change_product, return_list, admin_approve.
main - a list of products, showing the prices and quantity of products in stock. There is a link to change the product.
add_product - create a new product with all fields, including price and quantity in stock.
change_product - change an existing product. Superuser can change all fields, including the quantity of product in stock (to replenish the quantity of products).
return_list - a list with return objects (its can be created by logged in users) with two buttons: confirm or reject. If the superuser confirms the return, the purchase object is deleted, the quantity of the products is returned to the product model, and the value of the products is returned to the user's wallet field.
If the superuser rejects the return of products, the return object is deleted.

**2. User (logged in):**

Has access to the pages:
main - a list of products, indicating prices and quantities in stock, near the description of the goods there is a form with the ability to specify the number of goods, and the buy button.
list_of_purchased_products - a list of purchases. A list of products already purchased by the current user, there is a "return purcase" button next to each purchase. User can only return an purchase within 3 minutes of purchase if the button is pressed later and user receive a message that the products can no longer be returned. Creates a return object for a completed purchase (which must be confirmed by the superuser).

If the user is not logged in, then he sees only a list of goods, without any buttons.
After registration, the user automatically receives a certain amount of money in his wallet.

**REST API**

All actions performed by both admins and users have corresponding REST API endpoints. These endpoints can be accessed using Postman or similar tools.

**Technologies Used**

Django

Django REST framework

SQLite

HTML
