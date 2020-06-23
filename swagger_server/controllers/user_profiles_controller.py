import connexion
import six

from swagger_server.models.assessment import Assessment  # noqa: E501
from swagger_server.models.profile_item import ProfileItem  # noqa: E501
from swagger_server import util


def create_user_profile(body=None):  # noqa: E501
    """Create a new user profile

    adds user profile object to user profile collection # noqa: E501

    :param body: user profile to add
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ProfileItem.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_user_profile(id):  # noqa: E501
    """Delete User by id

    Delete a User profile in a collection # noqa: E501

    :param id: unique id number of user
    :type id: str

    :rtype: None
    """
    return 'do some magic!'


def profile_id_get(id):  # noqa: E501
    """Returns a User by it&#x27;s id

    Returns a single object of UserProfile # noqa: E501

    :param id: unique id number of user
    :type id: str

    :rtype: ProfileItem
    """
    return 'do some magic!'


def read_assessment_by_id(id):  # noqa: E501
    """Return list of assessment of a particular user

    Exposes user assessment  # noqa: E501

    :param id: assessment instance of userid id
    :type id: str

    :rtype: List[Assessment]
    """
    return 'do some magic!'


def search_user_profile(search_term=None):  # noqa: E501
    """Returns a list of all user profiles

    Exposes all user profiles without filters  # noqa: E501

    :param search_term: Pass an optional search string for looking up the userprofile collection
    :type search_term: str

    :rtype: List[ProfileItem]
    """
    term = search_term
    return 'do some magic!'


def update_user_profile(id, body=None):  # noqa: E501
    """Update User by id

    Update User profile by id # noqa: E501

    :param id: unique id number of user
    :type id: int
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ProfileItem.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
