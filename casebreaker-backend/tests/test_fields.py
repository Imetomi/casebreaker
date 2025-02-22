import pytest
from fastapi import status

def test_list_fields(client, sample_field):
    """Test listing all fields."""
    response = client.get("/api/v1/fields/")
    assert response.status_code == status.HTTP_200_OK
    
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1
    
    field = data[0]
    assert field["name"] == "Test Medicine"
    assert field["description"] == "Test medical field"
    assert field["icon_url"] == "https://example.com/icon.png"

def test_get_field(client, sample_field):
    """Test getting a specific field by ID."""
    response = client.get(f"/api/v1/fields/{sample_field.id}")
    assert response.status_code == status.HTTP_200_OK
    
    data = response.json()
    assert data["id"] == sample_field.id
    assert data["name"] == "Test Medicine"
    assert data["description"] == "Test medical field"

def test_get_field_not_found(client):
    """Test getting a non-existent field."""
    response = client.get("/api/v1/fields/999")
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_create_field(client):
    """Test creating a new field."""
    field_data = {
        "name": "New Field",
        "description": "New field description",
        "icon_url": "https://example.com/new-icon.png"
    }
    
    response = client.post("/api/v1/fields/", json=field_data)
    assert response.status_code == status.HTTP_200_OK
    
    data = response.json()
    assert data["name"] == "New Field"
    assert data["description"] == "New field description"
    assert data["icon_url"] == "https://example.com/new-icon.png"
    assert "id" in data

def test_delete_field(client, sample_field):
    """Test deleting a field."""
    response = client.delete(f"/api/v1/fields/{sample_field.id}")
    assert response.status_code == status.HTTP_200_OK
    
    # Verify it's deleted
    response = client.get(f"/api/v1/fields/{sample_field.id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_delete_field_not_found(client):
    """Test deleting a non-existent field."""
    response = client.delete("/api/v1/fields/999")
    assert response.status_code == status.HTTP_404_NOT_FOUND
