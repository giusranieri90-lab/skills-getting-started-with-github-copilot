import pytest


@pytest.mark.asyncio
async def test_get_activities_success(client):
    """Arrange: client is ready
       Act: send GET request to /activities
       Assert: response status is 200 and contains all activities"""
    # Arrange
    expected_activities = [
        "Chess Club",
        "Programming Class",
        "Gym Class",
        "Basketball",
        "Volleyball",
        "Debate Club",
        "Math Club",
        "Art Class",
        "Music Band",
    ]

    # Act
    response = await client.get("/activities")
    data = response.json()

    # Assert
    assert response.status_code == 200
    assert len(data) == 9
    for activity in expected_activities:
        assert activity in data


@pytest.mark.asyncio
async def test_get_activities_structure(client):
    """Arrange: client is ready
       Act: send GET request to /activities
       Assert: response contains correct activity structure"""
    # Arrange
    required_fields = ["description", "schedule", "max_participants", "participants"]

    # Act
    response = await client.get("/activities")
    data = response.json()

    # Assert
    assert response.status_code == 200
    for activity_name, activity_data in data.items():
        for field in required_fields:
            assert field in activity_data
        assert isinstance(activity_data["participants"], list)
