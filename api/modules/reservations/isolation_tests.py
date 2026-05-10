import threading

from modules.reservations.flight_reservation_service import (
    FlightReservationService
)


class IsolationTests:

    @staticmethod
    def concurrent_flight_test():

        def reserve():

            try:

                FlightReservationService \
                    .reserve_flight(
                        customer_id=1,
                        flight_id=1
                    )

                print(
                    "Reserva realizada"
                )

            except Exception as error:

                print(
                    f"Erro: {error}"
                )

        threads = []

        for _ in range(50):

            thread = threading.Thread(
                target=reserve
            )

            thread.start()

            threads.append(thread)

        for thread in threads:

            thread.join()