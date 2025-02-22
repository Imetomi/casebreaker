import pytest
from fastapi import status

def test_list_case_studies(client, sample_case_study):
    """Test listing all case studies."""
    response = client.get("/api/v1/case-studies/")
    assert response.status_code == status.HTTP_200_OK
    
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 1
    
    case_study = data[0]
    assert case_study["title"] == "Test Case Study"
    assert case_study["subtopic"]["case_count"] == 1

def test_list_case_studies_by_subtopic(client, sample_case_study, sample_subtopic):
    """Test listing case studies filtered by subtopic."""
    response = client.get(f"/api/v1/case-studies/?subtopic_id={sample_subtopic.id}")
    assert response.status_code == status.HTTP_200_OK
    
    data = response.json()
    assert len(data) == 1
    assert data[0]["subtopic_id"] == sample_subtopic.id
    assert data[0]["subtopic"]["case_count"] == 1

def test_get_case_study(client, sample_case_study):
    """Test getting a specific case study by ID."""
    response = client.get(f"/api/v1/case-studies/{sample_case_study.id}")
    assert response.status_code == status.HTTP_200_OK
    
    data = response.json()
    assert data["id"] == sample_case_study.id
    assert data["title"] == "Test Case Study"
    assert data["estimated_time"] == 60
    assert data["subtopic"]["case_count"] == 1

def test_get_case_study_not_found(client):
    """Test getting a non-existent case study."""
    response = client.get("/api/v1/case-studies/999")
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_get_case_study_by_slug(client, sample_case_study):
    """Test getting a case study by its share slug."""
    response = client.get(f"/api/v1/case-studies/by-slug/{sample_case_study.share_slug}")
    assert response.status_code == status.HTTP_200_OK
    
    data = response.json()
    assert data["id"] == sample_case_study.id
    assert data["share_slug"] == "test-case-study"
    assert data["subtopic"]["case_count"] == 1

def test_get_case_study_by_slug_not_found(client):
    """Test getting a case study with non-existent slug."""
    response = client.get("/api/v1/case-studies/by-slug/non-existent")
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_create_case_study(client, sample_subtopic):
    """Test creating a new case study."""
    case_study_data = {
        "title": "New Case Study",
        "description": "New description",
        "difficulty": 2,
        "specialization": "New Specialty",
        "learning_objectives": ["new objective"],
        "context_materials": {
            "background": "new background",
            "key_concepts": ["new concept"],
            "required_reading": "new reading"
        },
        "checkpoints": [
            {
                "id": "1",
                "title": "New Checkpoint",
                "description": "New checkpoint description",
                "hints": ["new hint"]
            }
        ],
        "source_url": "http://example.com/new",
        "source_type": "GENERATED",
        "subtopic_id": sample_subtopic.id,
        "estimated_time": 20
    }
    
    response = client.post("/api/v1/case-studies/", json=case_study_data)
    assert response.status_code == status.HTTP_200_OK
    
    data = response.json()
    assert data["title"] == "New Case Study"
    assert data["estimated_time"] == 20
    assert "share_slug" in data
    assert "created_at" in data
    assert "last_updated" in data
    assert data["subtopic"]["case_count"] == 1

def test_create_case_study_invalid_subtopic(client):
    """Test creating a case study with non-existent subtopic."""
    case_study_data = {
        "title": "Invalid Case Study",
        "description": "Test description",
        "difficulty": 1,
        "specialization": "Test Specialty",
        "learning_objectives": ["objective"],
        "context_materials": {
            "background": "background",
            "key_concepts": ["concept"],
            "required_reading": "reading"
        },
        "checkpoints": [],
        "source_url": "http://example.com/test",
        "source_type": "GENERATED",
        "subtopic_id": 999,
        "estimated_time": 10
    }
    
    response = client.post("/api/v1/case-studies/", json=case_study_data)
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_delete_case_study(client, sample_case_study):
    """Test deleting a case study."""
    response = client.delete(f"/api/v1/case-studies/{sample_case_study.id}")
    assert response.status_code == status.HTTP_200_OK
    
    # Verify it's deleted
    response = client.get(f"/api/v1/case-studies/{sample_case_study.id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_delete_case_study_not_found(client):
    """Test deleting a non-existent case study."""
    response = client.delete("/api/v1/case-studies/999")
    assert response.status_code == status.HTTP_404_NOT_FOUND
