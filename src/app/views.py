from fastapi import APIRouter, Depends, responses
from sqlalchemy import MetaData
from sqlalchemy.orm import Session
from sqlalchemy.testing.schema import Table
from starlette.requests import Request

from app.db import engine, yield_session  # noqa
from app.models import Compensation  # noqa
from app.schemas import CompensationSchema  # noqa
from app.utils import build_response_for_compensation  # noqa
from app.utils import build_statement  # noqa
from app.utils import get_fields_from_query_params  # noqa
from app.utils import get_sort_fields_from_query_params  # noqa
from app.utils import parse_conditions_from_query_params  # noqa

router = APIRouter()


@router.get("/ping/")
async def ping_view() -> str:
    return "pong"


@router.get("/compensation_documented/", response_model=list[CompensationSchema])
async def compensation_doc_view():
    """
    for openapi docs input scheme. actual /compensation endpoint's docs doesn't work
    because we can't declate response model (because of sparse fieldset)
    :return:
    """
    return "validation error here"


@router.get("/compensation/", response_class=responses.JSONResponse)
async def compensation_view(
    request: Request, session: Session = Depends(yield_session)
):
    table_name = Compensation.__tablename__
    table = Table(table_name, MetaData(), autoload_with=engine)

    conditions = parse_conditions_from_query_params(request)
    select_fields = get_fields_from_query_params(request, table)
    sort_fields = get_sort_fields_from_query_params(request)

    statement = build_statement(
        table_name=table_name,
        fields=select_fields,
        conditions=conditions,
        order_by=sort_fields,
    )
    query = session.execute(statement).all()

    return build_response_for_compensation(query, select_fields)
