@pytest.fixture
def user():
    from .factories import UserFactory
    return UserFactory(name="ピチュー")  # 実在の人物や団体とは関係ありません

@pytest.fixture
def user_client(user):
    from rest_framework.test import APIClient
    user_client = APIClient()
    user_client.force_authenticate(user=user)
    return user_client

def test_get(user_client):
    res = user_client.post(f"/api/me/")
    assert res.data["name"] == "ピチュー"

def test_patch(user, user_client):
    res = user_client.post(f"/api/me/", data={"name": "ピカチュウ"}, content_type="application/json")
    user.refresh_from_db()
    assert user.name == "ピカチュウ", "ピカチュウじゃないっす"  # 実在の人物や団体とは関係ありません