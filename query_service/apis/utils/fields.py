from aniso8601 import parse_date
from aniso8601.exceptions import ISOFormatError

from marshmallow import utils, ValidationError
from marshmallow.compat import basestring
from marshmallow.fields import List, String, Date, Integer
from marshmallow.utils import missing as missing_


class NotEmptyList(List):
    """
    非空List
    """
    default_error_messages = {
        'invalid': 'Not a valid list.',
        'invalid_empty': 'List length is less then {length}.'
    }
    
    def __init__(self, cls_or_instance, length=1, **kwargs):
        super(NotEmptyList, self).__init__(cls_or_instance, **kwargs)
        
        self.length = length
    
    def _deserialize(self, value, attr, data):
        if not utils.is_collection(value):
            self.fail('invalid')
        elif value.__len__() < self.length:
            self.fail('invalid_empty', length=str(self.length))
        else:
            result = []
            errors = {}
            for idx, each in enumerate(value):
                try:
                    result.append(self.container.deserialize(each))
                except ValidationError as e:
                    result.append(e.data)
                    errors.update({idx: e.messages})
    
            if errors:
                raise ValidationError(errors, data=result)
    
            return result


class EnumString(String):
    """
    枚举字符验证类型
    """
    default_error_messages = {
        'invalid': 'Not a valid string.',
        'invalid_utf8': 'Not a valid utf-8 string.',
        'invalid_enum': 'Element Not in enum list.'
    }

    def __init__(
            self,
            default=missing_,
            attribute=None,
            load_from=None,
            dump_to=None,
            error=None,
            validate=None,
            required=False,
            allow_none=None,
            load_only=False,
            dump_only=False,
            missing=missing_,
            enum=None,
            **metadata
    ):
        super(EnumString, self).__init__(
            self,
            default,
            attribute,
            load_from,
            dump_to,
            error,
            validate,
            required,
            allow_none,
            load_only,
            dump_only,
            missing,
            **metadata
        )
        
        self.enum = enum

    def _deserialize(self, value, attr, data):
        if not isinstance(value, basestring):
            self.fail('invalid')
        elif value not in self.enum:
            self.fail('invalid_enum')
        else:
            try:
                return utils.ensure_text_type(value)
            except UnicodeDecodeError:
                self.fail('invalid_utf8')


class StringDate(Date):
    """
    字符日期
    """
    def _deserialize(self, value, attr, data):
        """
        不对 value 进行类型转换, 保持字符类型
        :param value:
        :param attr:
        :param data:
        :return:
        """
        if not value:
            self.fail('invalid')
        try:
            parse_date(value)
        except (AttributeError, TypeError, ValueError, ISOFormatError):
            self.fail('invalid')
        else:
            return value


class MinMaxInteger(Integer):
    num_type = int
    default_error_messages = {
        'invalid': 'Not a valid integer.',
        'invalid_min': 'Value is less then {min}.',
        'invalid_max': 'Value is greater then {max}.'
    }

    def __init__(self, as_string=False, **kwargs):
        super(MinMaxInteger, self).__init__(as_string, **kwargs)
        
        self.min = kwargs.get('min', None)
        self.max = kwargs.get('max', None)
    
    def _format_num(self, value):
        """Return the number value for value, given this field's `num_type`."""
        if value is None:
            return None
        
        num_value = self.num_type(value)
        
        if self.min and num_value < self.min:
            self.fail('invalid_min', min=self.min)
        elif self.max and num_value > self.max:
            self.fail('invalid_max', max=self.max)
        else:
            return num_value

    def _validated(self, value):
        """Format the value or raise a :exc:`ValidationError` if an error occurs."""
        try:
            return self._format_num(value)
        except (TypeError, ValueError):
            self.fail('invalid')

    def _to_string(self, value):
        return str(value)

    def _serialize(self, value, attr, obj):
        """Return a string if `self.as_string=True`, otherwise return this field's `num_type`."""
        ret = self._validated(value)
        return self._to_string(ret) if (self.as_string and ret not in (None, missing_)) else ret

    def _deserialize(self, value, attr, data):
        return self._validated(value)
