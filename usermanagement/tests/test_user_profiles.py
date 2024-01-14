import pytest 
pytestmark = pytest.mark.django_db

class TestUserProfile:
    def test_str_return(self, user_profile_factory, user_factory):
        user = user_factory()
        user_profile = user_profile_factory(user=user)
        assert user_profile.__str__() == f"{user_profile.user}"
        assert user_profile is not None
        assert user_profile.user == user