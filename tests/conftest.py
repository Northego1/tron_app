import pytest

from core.container import Container


@pytest.fixture
def container() -> Container:
    return Container()
