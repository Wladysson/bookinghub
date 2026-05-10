CREATE_PAYMENT = """
INSERT INTO payments (
    reservation_type,
    reservation_id,
    customer_id,
    amount,
    payment_method,
    status,
    transaction_id
)
VALUES (
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s
)
RETURNING *;
"""


GET_PAYMENT_BY_ID = """
SELECT
    id,
    reservation_type,
    reservation_id,
    customer_id,
    amount,
    payment_method,
    status,
    transaction_id,
    created_at
FROM payments
WHERE id = %s;
"""


GET_ALL_PAYMENTS = """
SELECT
    id,
    reservation_type,
    reservation_id,
    customer_id,
    amount,
    payment_method,
    status,
    transaction_id,
    created_at
FROM payments
ORDER BY created_at DESC;
"""


UPDATE_PAYMENT_STATUS = """
UPDATE payments
SET status = %s
WHERE id = %s;
"""


LOCK_PAYMENT = """
SELECT
    id,
    status,
    amount
FROM payments
WHERE id = %s
FOR UPDATE;
"""