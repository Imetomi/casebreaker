import pytest
from datetime import datetime
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from casebreaker_backend.database import Base, get_db
from casebreaker_backend.main import app

# Create in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite://"

@pytest.fixture
def test_db():
    """Create a fresh database for each test."""
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    # Create tables
    Base.metadata.create_all(bind=engine)
    
    # Create a new session for the test
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

@pytest.fixture
def client(test_db):
    """Create a test client using the test database."""
    def override_get_db():
        try:
            yield test_db
        finally:
            test_db.close()
    
    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)

@pytest.fixture
def sample_field(test_db):
    """Create a sample field for testing."""
    from casebreaker_backend.models import Field
    
    field = Field(
        name="Test Medicine",
        description="Test medical field",
        icon_url="https://example.com/icon.png"
    )
    test_db.add(field)
    test_db.commit()
    test_db.refresh(field)
    return field

@pytest.fixture
def sample_subtopic(test_db, sample_field):
    """Create a sample subtopic for testing."""
    from casebreaker_backend.models import Subtopic
    
    subtopic = Subtopic(
        name="Test Practice",
        description="Test medical practice",
        field_id=sample_field.id
    )
    test_db.add(subtopic)
    test_db.commit()
    test_db.refresh(subtopic)
    return subtopic

@pytest.fixture
def sample_case_study(test_db, sample_subtopic):
    """Create a sample case study for testing."""
    from casebreaker_backend.models import CaseStudy
    from datetime import datetime
    
    case_study = CaseStudy(
        title="Test Case Study",
        description="Test description",
        difficulty=3,
        specialization="Test Specialty",
        learning_objectives=["objective1", "objective2"],
        context_materials={
            "background": "test background",
            "key_concepts": ["concept1", "concept2"],
            "required_reading": "test reading"
        },
        checkpoints=[
            {
                "id": "1",
                "title": "Test Checkpoint",
                "description": "Test checkpoint description",
                "hints": ["hint1"]
            }
        ],
        source_url="http://example.com/test",
        source_type="GENERATED",
        subtopic_id=sample_subtopic.id,
        estimated_time=60,
        share_slug="test-case-study",
        last_updated=datetime.utcnow(),
        created_at=datetime.utcnow()
    )
    test_db.add(case_study)
    test_db.commit()
    test_db.refresh(case_study)
    return case_study

@pytest.fixture
def sample_session(test_db, sample_case_study):
    """Create a sample session for testing."""
    from casebreaker_backend.models import Session
    
    session = Session(
        case_study_id=sample_case_study.id,
        device_id="test_device",
        status="active",
        completed_checkpoints=[],
        start_time=datetime.utcnow()
    )
    test_db.add(session)
    test_db.commit()
    test_db.refresh(session)
    return session

@pytest.fixture
def sample_chat_message(test_db, sample_session):
    """Create a sample chat message for testing."""
    from casebreaker_backend.models import ChatMessage
    from datetime import datetime
    
    message = ChatMessage(
        role="user",
        content="Test message",
        session_id=sample_session.id,
        checkpoint_id="1",
        timestamp=datetime.utcnow()
    )
    test_db.add(message)
    test_db.commit()
    test_db.refresh(message)
    return message
