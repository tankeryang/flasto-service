from flask_restplus import fields
from query_service.query_web.controller.crm_controller import ns


crm_member_analyse_req_dto_model = ns.model('CrmMemberAnalyseReqDtoModel', {
    'sales_modes': fields.List(fields.String(required=True, description="门店类别", enum=['正价', '长特', '短特'])),
    'store_types': fields.List(fields.String(required=True, description="门店类型", enum=['MALL', '百货', '专卖店'])),
    'store_levels': fields.List(fields.String(required=True, description="门店等级", enum=['A', 'B', 'C'])),
    'channel_types': fields.List(fields.String(required=True, description="经营方式/渠道", enum=['自营', '联营', '特许'])),
    'order_channels': fields.List(fields.String(required=True, description="订单类型(线上/线下)", enum=['线下', '线上'])),
    'country': fields.List(fields.String(description="全国", enum=['全国'])),
    'sales_areas': fields.List(fields.String(description="大区", enum=['华东', '华南', '华北', '华中'])),
    'sales_districts': fields.List(fields.String(description="片区", enum=['暂无数据'])),
    'provinces': fields.List(fields.String(description="省份", enum=['广东省', '浙江省'])),
    'cities': fields.List(fields.String(description="城市", enum=['广州市', '上海市', '北京市', '深圳市'])),
    'start_date': fields.String(required=True, description="开始日期(yyyy-mm-dd)", enum=['2018-01-01']),
    'end_date': fields.String(required=True, description="结束日期(yyyy-mm-dd)", enum=['2018-08-10'])
})