from unittest.mock import AsyncMock, Mock

mock_get_response = {
    "data": [
        {"balance": 666},
    ],
}
mock_post_response = {
    "freeNetLimit": 666,
    "EnergyLimit": 666,
}


http_mock = Mock()
mock_post = AsyncMock(return_value=AsyncMock(json=Mock(return_value=mock_post_response)))
mock_get = AsyncMock(return_value=AsyncMock(json=Mock(return_value=mock_get_response)))
http_mock.client.post = mock_post
http_mock.client.get = mock_get
