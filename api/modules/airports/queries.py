GET_ALL_AIRPORTS = """
SELECT
    id,
    code,
    name,
    city,
    country
FROM airports
ORDER BY city, code;
"""


GET_AIRPORT_BY_ID = """
SELECT
    id,
    code,
    name,
    city,
    country
FROM airports
WHERE id = %s;
"""


GET_AIRPORT_BY_CODE = """
SELECT
    id,
    code,
    name,
    city,
    country
FROM airports
WHERE code = %s;
"""


CREATE_AIRPORT = """
INSERT INTO airports (
    code,
    name,
    city,
    country
)
VALUES (
    %s,
    %s,
    %s,
    %s
)
RETURNING
    id,
    code,
    name,
    city,
    country;
"""


DELETE_AIRPORT = """
DELETE FROM airports
WHERE id = %s;
"""