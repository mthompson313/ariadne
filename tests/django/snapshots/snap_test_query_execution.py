# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_post_request_fails_if_request_content_type_is_not_json 1'] = b'Posted content must be of type application/json or multipart/form-data'

snapshots['test_post_request_fails_if_request_data_is_malformed_json 1'] = b'Request body is not a valid JSON'

snapshots['test_query_in_valid_post_request_is_executed 1'] = b'{"data": {"status": true}}'

snapshots['test_query_is_executed_for_multipart_form_request_with_file 1'] = b'{"data": {"upload": "InMemoryUploadedFile"}}'
