from sqlalchemy.orm import Session
from casebreaker_backend.database import SessionLocal
from casebreaker_backend.models import Field, Subtopic, CaseStudy


def seed_data():
    db = SessionLocal()
    try:
        # Create Fields
        law = Field(
            name="Law",
            description="Explore real-world legal cases and ethical dilemmas across different areas of law.",
            icon_url="https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=800&auto=format&fit=crop&q=60",
        )

        healthcare = Field(
            name="Healthcare",
            description="Analyze medical cases, diagnostic challenges, and healthcare management scenarios.",
            icon_url="https://images.unsplash.com/photo-1631248055158-edec7a3c072b?w=800&auto=format&fit=crop&q=60",
        )

        economics = Field(
            name="Economics",
            description="Study economic principles through real business cases and market analyses.",
            icon_url="https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=800&auto=format&fit=crop&q=60",
        )

        finance = Field(
            name="Finance",
            description="Master financial concepts through real-world investment and corporate finance cases.",
            icon_url="https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=800&auto=format&fit=crop&q=60",
        )

        history = Field(
            name="History",
            description="Analyze pivotal historical events, decisions, and their lasting impact on society.",
            icon_url="https://images.unsplash.com/photo-1461360370896-922624d12aa1?w=800&auto=format&fit=crop&q=60",
        )

        db.add_all([law, healthcare, economics, finance, history])
        db.commit()

        # Create Subtopics for Law
        law_subtopics = [
            Subtopic(
                name="Criminal Law",
                description="Study criminal cases involving various offenses and legal procedures.",
                field_id=law.id,
            ),
            Subtopic(
                name="Corporate Law",
                description="Examine business-related legal cases and corporate governance issues.",
                field_id=law.id,
            ),
            Subtopic(
                name="Constitutional Law",
                description="Analyze cases involving constitutional rights and governmental powers.",
                field_id=law.id,
            ),
        ]

        # Create Subtopics for Healthcare
        healthcare_subtopics = [
            Subtopic(
                name="Emergency Medicine",
                description="Learn from emergency room cases and critical care scenarios.",
                field_id=healthcare.id,
            ),
            Subtopic(
                name="Medical Ethics",
                description="Explore ethical dilemmas in healthcare decision-making.",
                field_id=healthcare.id,
            ),
            Subtopic(
                name="Public Health",
                description="Study cases related to population health and healthcare policy.",
                field_id=healthcare.id,
            ),
        ]

        # Create Subtopics for Economics
        economics_subtopics = [
            Subtopic(
                name="Microeconomics",
                description="Analyze individual market behaviors and business decisions.",
                field_id=economics.id,
            ),
            Subtopic(
                name="Macroeconomics",
                description="Study economic trends, policies, and their global impact.",
                field_id=economics.id,
            ),
            Subtopic(
                name="Financial Markets",
                description="Examine cases involving financial instruments and market dynamics.",
                field_id=economics.id,
            ),
        ]

        finance_subtopics = [
            Subtopic(
                name="Investment Management",
                description="Learn portfolio management and investment strategies.",
                field_id=finance.id,
            ),
            Subtopic(
                name="Corporate Finance",
                description="Study mergers, acquisitions, and corporate financial decisions.",
                field_id=finance.id,
            ),
            Subtopic(
                name="Risk Management",
                description="Analyze financial risk assessment and mitigation strategies.",
                field_id=finance.id,
            ),
        ]

        history_subtopics = [
            Subtopic(
                name="World Wars",
                description="Examine the causes, events, and consequences of global conflicts.",
                field_id=history.id,
            ),
            Subtopic(
                name="Civil Rights Movement",
                description="Study the struggle for equality and civil rights in America.",
                field_id=history.id,
            ),
            Subtopic(
                name="Ancient Civilizations",
                description="Explore the rise and fall of great ancient societies.",
                field_id=history.id,
            ),
        ]

        db.add_all(law_subtopics + healthcare_subtopics + economics_subtopics + finance_subtopics + history_subtopics)
        db.commit()

        # Create a test case study
        miranda_case = CaseStudy(
            title="The Miranda Rights Case",
            description="A landmark case that established the requirement for law enforcement to inform suspects of their rights.",
            difficulty=3,
            specialization="Criminal Procedure",
            learning_objectives=[
                "Understand the importance of Miranda rights",
                "Learn about police procedure requirements",
            ],
            context_materials={
                "background": "Miranda v. Arizona was a landmark decision...",
                "key_concepts": ["Right to remain silent", "Right to an attorney"],
            },
            checkpoints=[
                {
                    "id": "introduction",
                    "title": "Introduction",
                    "content": "Welcome! I'm here to help you analyze the Miranda Rights case. Let's start by discussing the historical context of this landmark decision.\n\nWhat aspects of the Miranda v. Arizona case would you like to explore first?\n1. The facts of the case\n2. The Supreme Court's decision\n3. The impact on law enforcement\n4. Modern applications\n\nFeel free to ask any questions!",
                }
            ],
            source_type="GENERATED",
            share_slug="miranda-1",
            subtopic_id=law_subtopics[0].id,
        )

        db.add(miranda_case)
        db.commit()

    except Exception as e:
        print(f"Error seeding data: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_data()
    print("Data seeding completed successfully!")
