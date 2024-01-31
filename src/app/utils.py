import re
from typing import Any, Iterable, List, Optional, Sequence

from sqlalchemy import Row, Table, TextClause, text
from starlette.requests import Request


def parse_conditions_from_query_params(request: Request) -> list:
    query_params = request.query_params
    conditions = []
    op_map = {
        "gte": ">=",
        "lte": "<=",
        "gt": ">",
        "lt": "<",
    }
    for key, value in query_params.items():
        if key in ("fields", "sort"):
            continue
        match = re.match(r"(.+)\[(gte|lte|gt|lt)\]", key)
        if match:
            field, op = match.groups()
            op = op_map[op]
        else:
            field, op = key, "="
        conditions.append(f"{field} {op} {value}")

    return conditions


def get_fields_from_query_params(request: Request, table: Table) -> List[str]:
    fields = request.query_params.get("fields")
    if not fields:  # return all fields
        return [field.__str__() for field in table.c.keys()]
    return fields.split(",")


def get_sort_fields_from_query_params(request: Request) -> List[str]:
    sort_by = request.query_params.get("sort")
    if not sort_by:
        return []
    return sort_by.split(",")


def build_statement(
    table_name: str,
    fields: Iterable[str],
    conditions: Optional[List[str]],
    order_by: Optional[List[str]],
) -> TextClause:
    statement = f"SELECT {','.join(fields)} " f"FROM {table_name}"
    if conditions:
        statement += f" WHERE {' AND '.join(conditions)}"

    if order_by:
        order_by = [s + " DESC" for s in order_by]
        statement += f" ORDER BY {','.join(order_by)}"

    statement += ";"
    return text(statement)


def build_response_for_compensation(query: Sequence[Row[Any]], fields: List[str]):
    response = []
    for item in query:
        response.append(dict(zip(fields, item.t)))
    return response
