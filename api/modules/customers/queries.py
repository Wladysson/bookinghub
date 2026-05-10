GET_ALL_CUSTOMERS = """
SELECT
    id,
    first_name,
    last_name,
    email,
    phone,
    document_number,
    nationality,
    created_at
FROM customers
ORDER BY created_at DESC;
"""


GET_CUSTOMER_BY_ID = """
SELECT
    id,
    first_name,
    last_name,
    email,
    phone,
    document_number,
    nationality,
    created_at
FROM customers
WHERE id = %s;
"""


GET_CUSTOMER_BY_EMAIL = """
SELECT
    id,
    email
FROM customers
WHERE email = %s;
"""


GET_CUSTOMER_BY_DOCUMENT = """
SELECT
    id,
    document_number
FROM customers
WHERE document_number = %s;
"""


CREATE_CUSTOMER = """
INSERT INTO customers (
    first_name,
    last_name,
    email,
    phone,
    document_number,
    nationality
)
VALUES (
    %s,
    %s,
    %s,
    %s,
    %s,
    %s
)
RETURNING *;
"""


UPDATE_CUSTOMER = """
UPDATE customers
SET
    first_name = COALESCE(%s, first_name),
    last_name = COALESCE(%s, last_name),
    phone = COALESCE(%s, phone),
    nationality = COALESCE(%s, nationality)
WHERE id = %s
RETURNING *;
"""


DELETE_CUSTOMER = """
DELETE FROM customers
WHERE id = %s;
"""