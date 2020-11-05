from typing import Type

from model import ModelsConstructor
from test_models import SomeTest



class TestSome:
    async def test_simple_example(self, mocker: Type[ModelsConstructor]):
        async with mocker(SomeTest) as mck:
            assert mck['some'].example_col == 1

