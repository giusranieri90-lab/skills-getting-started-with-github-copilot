import pytest


@pytest.mark.asyncio
async def test_signup_success(client):
    """Arrange: client is ready with new student
       Act: sign up new student for activity
       Assert: response status is 200 and participant is added"""
    # Arrange
    activity = "Chess Club"
    email = "newstudent@mergington.edu"

    # Act
    response = await client.post(
        f"/activities/{activity}/signup",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 200
    assert "Signed up" in response.json()["message"]


@pytest.mark.asyncio
async def test_signup_already_registered(client):
    """Arrange: client is ready with already-registered student
       Act: attempt to sign up already-registered student
       Assert: response status is 400"""
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"  # Already in Chess Club

    # Act
    response = await client.post(
        f"/activities/{activity}/signup",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"]


@pytest.mark.asyncio
async def test_signup_activity_not_found(client):
    """Arrange: client is ready with non-existent activity
       Act: attempt to sign up for non-existent activity
       Assert: response status is 404"""
    # Arrange
    activity = "Non-Existent Activity"
    email = "student@mergington.edu"

    # Act
    response = await client.post(
        f"/activities/{activity}/signup",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 404
    assert "Activity not found" in response.json()["detail"]


@pytest.mark.asyncio
async def test_unregister_success(client):
    """Arrange: client is ready with registered student
       Act: unregister student from activity
       Assert: response status is 200 and participant is removed"""
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"

    # Act
    response = await client.delete(
        f"/activities/{activity}/unregister",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 200
    assert "Unregistered" in response.json()["message"]


@pytest.mark.asyncio
async def test_unregister_not_registered(client):
    """Arrange: client is ready with unregistered student
       Act: attempt to unregister student not in activity
       Assert: response status is 400"""
    # Arrange
    activity = "Chess Club"
    email = "notregistered@mergington.edu"

    # Act
    response = await client.delete(
        f"/activities/{activity}/unregister",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 400
    assert "not registered" in response.json()["detail"]


@pytest.mark.asyncio
async def test_unregister_activity_not_found(client):
    """Arrange: client is ready with non-existent activity
       Act: attempt to unregister from non-existent activity
       Assert: response status is 404"""
    # Arrange
    activity = "Non-Existent Activity"
    email = "student@mergington.edu"

    # Act
    response = await client.delete(
        f"/activities/{activity}/unregister",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 404
    assert "Activity not found" in response.json()["detail"]
