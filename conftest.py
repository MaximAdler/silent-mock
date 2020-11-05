from typing import Type

import pytest
from _pytest.fixtures import SubRequest

from model import ModelsConstructor


@pytest.fixture(scope='class', params=[66666, 77777, 88888, 99999])
def mocker(request: SubRequest) -> Type[ModelsConstructor]:
    ModelsConstructor.param = request.param
    return ModelsConstructor
