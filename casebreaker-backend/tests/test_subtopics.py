import pytest
from fastapi import status

def test_list_subtopics(client, sample_subtopic):
    """Test listing all subtopics."""
    response = client.get("/api/v1/subtopics/")
    assert response.status_code == status.HTTP_200_OK
    
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1
    
    subtopic = data[0]
    assert subtopic["name"] == "Test Practice"
    assert subtopic["description"] == "Test medical practice"
    assert subtopic["case_count"] == 0
    assert "field" in subtopic

def test_list_subtopics_by_field(client, sample_field, sample_subtopic):
    """Test listing subtopics filtered by field."""
    response = client.get(f"/api/v1/subtopics/?field_id={sample_field.id}")
    assert response.status_code == status.HTTP_200_OK
    
    data = response.json()
    assert len(data) == 1
    assert data[0]["field_id"] == sample_field.id
    assert data[0]["case_count"] == 0

def test_list_subtopics_with_case_count(client, sample_subtopic, sample_case_study):
    """Test that case_count is computed correctly."""
    response = client.get("/api/v1/subtopics/")
    assert response.status_code == status.HTTP_200_OK
    
    data = response.json()
    assert len(data) == 1
    assert data[0]["case_count"] == 1

def test_get_subtopic(client, sample_subtopic):
    """Test getting a specific subtopic by ID."""
    response = client.get(f"/api/v1/subtopics/{sample_subtopic.id}")
    assert response.status_code == status.HTTP_200_OK
    
    data = response.json()
    assert data["id"] == sample_subtopic.id
    assert data["name"] == "Test Practice"
    assert data["description"] == "Test medical practice"
    assert "field" in data

def test_get_subtopic_not_found(client):
    """Test getting a non-existent subtopic."""
    response = client.get("/api/v1/subtopics/999")
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_create_subtopic(client, sample_field):
    """Test creating a new subtopic."""
    subtopic_data = {
        "name": "New Subtopic",
        "description": "New subtopic description",
        "field_id": sample_field.id
    }
    
    response = client.post("/api/v1/subtopics/", json=subtopic_data)
    assert response.status_code == status.HTTP_200_OK
    
    data = response.json()
    assert data["name"] == "New Subtopic"
    assert data["description"] == "New subtopic description"
    assert data["field_id"] == sample_field.id
    assert "id" in data

def test_create_subtopic_invalid_field(client):
    """Test creating a subtopic with non-existent field."""
    subtopic_data = {
        "name": "Invalid Subtopic",
        "description": "Test description",
        "field_id": 999
    }
    
    response = client.post("/api/v1/subtopics/", json=subtopic_data)
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_delete_subtopic(client, sample_subtopic):
    """Test deleting a subtopic."""
    response = client.delete(f"/api/v1/subtopics/{sample_subtopic.id}")
    assert response.status_code == status.HTTP_200_OK
    
    # Verify it's deleted
    response = client.get(f"/api/v1/subtopics/{sample_subtopic.id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_delete_subtopic_not_found(client):
    """Test deleting a non-existent subtopic."""
    response = client.delete("/api/v1/subtopics/999")
    assert response.status_code == status.HTTP_404_NOT_FOUND
