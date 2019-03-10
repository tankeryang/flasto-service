from marshmallow import Schema, fields
from query_service.apis.utils.fields import NotEmptyList


class CicStaticQOValidator(Schema):
    brands = NotEmptyList(fields.String(description="品牌名"), required=True)
