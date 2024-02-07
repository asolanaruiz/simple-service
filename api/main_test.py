# Copyright 2024 Flower Labs GmbH. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from api.main import read_root
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


def test_read_root():
    # Prepare
    expected = {"Hello": "World"}

    # Execute
    actual = read_root()

    # Assert
    assert expected == actual


def test_create_user():
    response = client.post(
        '/users', data={'email': 'foo@bar.com', 'password': 'asdf1234'})
    assert response.status_code == 200
