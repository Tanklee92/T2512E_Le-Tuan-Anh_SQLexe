-- Câu 1
SELECT 
    c.category_name,
    COUNT(p.product_id) AS total_products
FROM Categories c
LEFT JOIN Products p ON c.category_id = p.category_id
GROUP BY c.category_id, c.category_name;

-- câu 2
SELECT
    c.category_name,
    ROUND(AVG(p.price), 2) AS avg_price,
    MAX(p.price) AS max_price,
    MIN(p.price) AS min_price
FROM Categories c
JOIN Products p
    ON c.category_id = p.category_id
GROUP BY c.category_id, c.category_name;

-- câu 3
SELECT
    status,
    COUNT(order_id) AS total_orders
FROM Orders
GROUP BY status;

-- câu 4:
SELECT
    c.customer_name,
    COUNT(o.order_id) AS total_completed
FROM Customers c
LEFT JOIN Orders o
    ON c.customer_id = o.customer_id
    AND o.status = 'Completed'
GROUP BY c.customer_id, c.customer_name;

-- câu 5

SELECT
    o.order_id,
    o.order_date,
    SUM(od.quantity * od.unit_price) AS total_revenue
FROM Orders o
JOIN OrderDetails od
    ON o.order_id = od.order_id
WHERE o.status = 'Completed'
GROUP BY o.order_id, o.order_date
ORDER BY o.order_id;

-- câu 6

SELECT
    p.product_name,
    SUM(od.quantity) AS total_quantity
FROM Products p
JOIN OrderDetails od
    ON p.product_id = od.product_id
JOIN Orders o
    ON od.order_id = o.order_id
WHERE o.status = 'Completed'
GROUP BY p.product_id, p.product_name
ORDER BY total_quantity DESC;