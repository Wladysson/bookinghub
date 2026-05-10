from fastapi import APIRouter

from modules.reports.service import (
    ReportsService
)

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.get(
    "/dashboard"
)
def dashboard_metrics():

    return ReportsService \
        .get_dashboard_metrics()


@router.get(
    "/top-destinations"
)
def top_destinations():

    return ReportsService \
        .get_top_destinations()


@router.get(
    "/hotel-occupancy"
)
def hotel_occupancy():

    return ReportsService \
        .get_hotel_occupancy()


@router.get(
    "/payments-by-method"
)
def payments_by_method():

    return ReportsService \
        .get_payments_by_method()


@router.get(
    "/monthly-revenue"
)
def monthly_revenue():

    return ReportsService \
        .get_monthly_revenue()