import concurrent.futures
import requests


URLS = [
    "http://127.0.0.1:8000/health",
    "http://127.0.0.1:8000/api/v1/flights",
    "http://127.0.0.1:8000/api/v1/hotels",
    "http://127.0.0.1:8000/api/v1/airports"
]


def make_request(url):

    try:

        response = requests.get(
            url,
            timeout=5
        )

        return (
            url,
            response.status_code
        )

    except Exception as error:

        return (
            url,
            str(error)
        )


with concurrent.futures.ThreadPoolExecutor(
    max_workers=200
) as executor:

    futures = []

    for _ in range(1000):

        for url in URLS:

            futures.append(
                executor.submit(
                    make_request,
                    url
                )
            )

    for future in futures:

        print(
            future.result()
        )