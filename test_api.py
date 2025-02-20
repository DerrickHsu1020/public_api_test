import pytest
import requests

BASE_URL = "https://www.thesportsdb.com/api/v1/json/3/searchteams.php"
    

def get_team_response(team_name: str) -> object:
    """ Sends a GET request to fetch team details and returns the response JSON. 

    :param team_name: The team name for search
    """
    response = requests.get(BASE_URL, params={"t": team_name})
    return response  # Return the whole response object

def parse_team_response(response: object) -> list:
    """ Parses the JSON response and returns the teams list. 

    :param response: reponse from search team API request
    """
    json_response = response.json()
    teams = json_response.get("teams", [])  # Default to empty list if "teams" is None
    return teams

# Test case for valid team (Positive case)
@pytest.mark.parametrize("team_name, expected_status, expected_team_name", [
    ("Manchester United", 200, "Manchester United"),  
    ("Manchester City", 200, "Manchester City"),
    ("Chelsea", 200, "Chelsea"),
    ("Arsenal", 200, "Arsenal"),
    ("Liverpool", 200, "Liverpool"),
    ("Tottenham", 200, "Tottenham"),
])
def test_valid_team(team_name, expected_status, expected_team_name):
    """Test the valid team and expected the api return the correct expected team name
        
    """
    response = get_team_response(team_name)
    
    assert response.status_code == expected_status, "http status is not 200"
    
    team_data = parse_team_response(response)[0]
    assert team_data["strTeam"] == expected_team_name, f'strTeam is not expected, current strTeam:{team_data["strTeam"]}, expected: {expected_team_name}'

@pytest.mark.parametrize("team_name, expected_status", [
    ("NonExistentTeam", 200)
])
def test_invalid_team(team_name, expected_status):
    """Make sure the api does not return any value when the request is invalid
    
    """
    response = get_team_response(team_name)
    assert response.status_code == expected_status
    team_data = parse_team_response(response)  # Default to empty list if "teams" is None
    assert team_data is None, f'Test failed, team data should be null, {team_data}'