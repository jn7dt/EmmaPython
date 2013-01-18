from . import BaseApiModel, ModelWithDateFields
from import_status import ImportStatus
from import_style import ImportStyle


class EmmaImport(BaseApiModel, ModelWithDateFields):
    def __init__(self, account, raw = None):
        self.account = account
        self._dict = self._parse_raw(raw) if raw is not None else {}

    def _parse_raw(self, raw):
        if 'status' in raw:
            raw['status'] = ImportStatus.factory(raw['status'])
        if 'style' in raw:
            raw['style'] = ImportStyle.factory(raw['style'])
        self._str_fields_to_datetime(
            ['import_started', 'import_finished'],
            raw)
        return raw
