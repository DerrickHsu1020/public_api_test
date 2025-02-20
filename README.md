# public_api_test


## Setup & Installation
### Prerequisites
Ensure you have the following installed:
- Python (>=3.7)

## Running the Tests
To execute the test, run:
```bash
pytest test_api.py
```

# TheSportsDB API Test Cases
## Test Case 1: Valid Team (Positive Scenario)

| Step | Action | Expected Result | Validation |
|------|--------|-----------------|------------|
| 1 | Send a GET request to `/searchteams.php?t=Manchester%20United` | Status code 200 | Validate status code is 200 |
| 2 | Check the response JSON | `teams` contains team "Manchester United" | Validate the team name in the response |

## Test Case 2: Invalid Team (Negative Scenario)

| Step | Action | Expected Result | Validation |
|------|--------|-----------------|------------|
| 1 | Send a GET request to `/searchteams.php?t=NonExistentTeam` | Status code 200 | Validate status code is 200 |
| 2 | Check the response JSON | `teams` is empty | Validate there are no teams in the response |

## Validation Methods
- **HTTP Status Code Validation**: Ensures the API responds as expected based on the request.
- **JSON Structure Validation**: Verifies that the correct keys and data types are present in the response.

### Framework Design & Modularity
- Using **pytest** with **parametrize** to reduce redundancy and improve test coverage.
- Separated test functions for clear structure and maintainability.
