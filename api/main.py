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

import random
import string
from api.models import User, UserUI
from fastapi import Depends, FastAPI
from sqlalchemy.orm.session import Session

from db.db import get_db, Base, engine
import db.db_user as db_user

import uuid

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post('/users')
def create_user(request: User, db: Session = Depends(get_db)):
    token = get_random_string(10)
    db_user.create_user(db, request, token)

    return {
        'email': request.email,
        'token': token
    }


@app.get('/users/{email}', response_model=UserUI)
def get_user(email: str, token: str, db: Session = Depends(get_db)):
    user = db_user.get_user(db, email, token)
    return UserUI(
        email=user.email,
        id=user.id
    )


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)
    return result_str


Base.metadata.create_all(engine)
