# CaseBreaker - Application Specification

## Overview
CaseBreaker is a lightweight educational application that provides AI-guided case study learning experiences in law, healthcare, and economics. The application operates without user accounts, focusing purely on case study management and interactive learning sessions.

## Core User Journey

```
Landing Page -> Field Selection -> Subtopic List -> Case Study List -> Case Study Session
```

### Landing Page
- Value proposition + Get Started button

### Field Selection
- Law, Health/Medicine, Economics as clickable cards

### Navigation Flow
- Subtopics listed under each field
- Case studies listed under each subtopic
- Interactive session starts on case study selection

## URL Structure
```
Landing: /
Fields: /fields
Subtopic: /fields/{field-id}
Cases: /fields/{field-id}/{subtopic-id}
Session: /case/{share-slug}
```

## Data Structure

### Basic Models
```
Field: {
  name, description, icon
  has_many: subtopics
}

Subtopic: {
  name, description
  has_many: case_studies
  belongs_to: field
}

CaseStudy: {
  title, description, difficulty(1-5)
  specialization, objectives
  context_materials(text), checkpoints(5)
  source_url, source_type(SCRAPED|GENERATED)
  last_updated, share_slug
  belongs_to: subtopic
}

Session: {
  tracks: checkpoint_progress, completion
  has: chat_history, current_checkpoint
  device_id: unique_device_identifier
}

ChatMessage: {
  session_id: string
  role: 'user' | 'assistant'
  content: string
  timestamp: datetime
  checkpoint_id: string (optional)
}
```

## Data Storage - SQLite

### Schema
```sql
fields
  - id
  - name
  - description
  - icon_url

subtopics
  - id
  - field_id
  - name
  - description

case_studies
  - id
  - subtopic_id
  - title
  - description
  - difficulty
  - specialization
  - learning_objectives (JSON)
  - context_materials (JSON)
  - checkpoints (JSON)
  - source_url
  - source_type
  - last_updated
  - share_slug (UNIQUE)
  - created_at

sessions
  - id
  - case_study_id
  - start_time
  - completed_checkpoints (JSON)
  - status
  - device_id

chat_messages
  - id
  - session_id
  - role
  - content
  - timestamp
  - checkpoint_id
```

[Rest of the specification remains the same]

Would you like me to show the complete specs with all sections?

## Learning Flow

### Case Study Session Types
- Law: Evidence -> Analysis -> Strategy -> Decision -> Outcome
- Medical: History -> Symptoms -> Tests -> Diagnosis -> Treatment
- Economics: Data -> Analysis -> Impact -> Strategy -> Recommendation

### Checkpoint Structure
1. Understanding Context (background, stakeholders, facts)
2. Problem Analysis (critical info, patterns)
3. Strategy Development (options, risks)
4. Implementation (decisions, actions)
5. Outcome & Reflection (evaluation, learning)

### AI Tutor Role
- Socratic questioning
- Contextual hints
- Checkpoint validation
- Expert guidance
- Progress tracking

### Content Generation Pipeline
```
Raw Source -> Scraper -> Claude Processing -> Case Study Structure
```

## Technical Stack

### Frontend
- React/TypeScript + Radix UI

### Backend
- Python
- Claude API integration
- SQLite storage
- Python-based scraper system

### Scraper System
```python
Scraper -> Claude Processor -> Content Validator -> Storage
```
- Collects source material
- Transforms into case study format
- Generates checkpoints and hints
- Validates content quality
- Stores in database

### Device Identification
- Generate unique device ID on first visit
- Store in browser's local storage
- Use for session tracking
- Allow multiple sessions per device