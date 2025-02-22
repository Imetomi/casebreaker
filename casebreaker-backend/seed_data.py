from sqlalchemy.orm import Session
from sqlalchemy import text
from casebreaker_backend.database import SessionLocal
from casebreaker_backend.models import Field, Subtopic, CaseStudy


def seed_data():
    db = SessionLocal()
    try:
        # Clear existing data
        db.execute(text('PRAGMA foreign_keys=OFF'))
        db.execute(text('DELETE FROM case_studies'))
        db.execute(text('DELETE FROM subtopics'))
        db.execute(text('DELETE FROM fields'))
        db.execute(text('PRAGMA foreign_keys=ON'))
        db.commit()
        # Create Fields
        law = Field(
            name="Law",
            description="Legal studies and jurisprudence",
            icon_url="https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=800&auto=format&fit=crop&q=60"
        )
        db.add(law)
        db.commit()
        db.refresh(law)

        # Create subtopics
        subtopics_data = [
            {
                "name": "Criminal Law",
                "description": "Study of crime and criminal justice"
            },
            {
                "name": "Constitutional Law",
                "description": "Study of fundamental rights and government structure"
            },
            {
                "name": "Contract Law",
                "description": "Study of legally binding agreements"
            },
            {
                "name": "Tort Law",
                "description": "Study of civil wrongs and liabilities"
            }
        ]

        subtopics = {}
        for subtopic_data in subtopics_data:
            subtopic = Subtopic(
                field_id=law.id,
                **subtopic_data
            )
            db.add(subtopic)
            db.commit()
            db.refresh(subtopic)
            subtopics[subtopic_data["name"]] = subtopic

        # Create case studies
        cases_data = [
            # Criminal Law Cases
            {
                "subtopic": "Criminal Law",
                "title": "The Miranda Rights Case",
                "description": "Explore the landmark case that established the requirement for police to inform suspects of their rights",
                "difficulty": 3,
                "specialization": "Criminal Procedure",
                "learning_objectives": ["Understanding Miranda rights", "Police procedure", "Constitutional protections"],
                "context_materials": {"background": "1966 Supreme Court case", "key_principles": ["Right to remain silent", "Right to attorney"]}
            },
            {
                "subtopic": "Criminal Law",
                "title": "Double Jeopardy Analysis",
                "description": "Study of protection against multiple prosecutions",
                "difficulty": 4,
                "specialization": "Constitutional Criminal Law",
                "learning_objectives": ["Double jeopardy clause", "Exceptions and limitations"],
                "context_materials": {"background": "Fifth Amendment protections"}
            },
            {
                "subtopic": "Criminal Law",
                "title": "Search and Seizure Rights",
                "description": "Fourth Amendment protections in criminal procedure",
                "difficulty": 3,
                "specialization": "Criminal Procedure",
                "learning_objectives": ["Fourth Amendment analysis", "Warrant requirements"],
                "context_materials": {"background": "Fourth Amendment history"}
            },
            {
                "subtopic": "Criminal Law",
                "title": "Cybercrime and Digital Evidence",
                "description": "Modern criminal investigation in digital age",
                "difficulty": 5,
                "specialization": "Digital Forensics",
                "learning_objectives": ["Digital evidence handling", "Cybercrime elements"],
                "context_materials": {"background": "Digital investigation techniques"}
            },
            {
                "subtopic": "Criminal Law",
                "title": "White Collar Crime Analysis",
                "description": "Study of financial and corporate crimes",
                "difficulty": 4,
                "specialization": "Financial Crime",
                "learning_objectives": ["Financial fraud", "Corporate criminal liability"],
                "context_materials": {"background": "Corporate crime principles"}
            },

            # Constitutional Law Cases
            {
                "subtopic": "Constitutional Law",
                "title": "First Amendment Analysis",
                "description": "Deep dive into freedom of speech protections",
                "difficulty": 4,
                "specialization": "Civil Rights",
                "learning_objectives": ["First Amendment scope", "Modern applications"],
                "context_materials": {"background": "First Amendment history"}
            },
            {
                "subtopic": "Constitutional Law",
                "title": "Equal Protection Deep Dive",
                "description": "Comprehensive study of equality under law",
                "difficulty": 5,
                "specialization": "Civil Rights",
                "learning_objectives": ["Equal protection analysis", "Levels of scrutiny"],
                "context_materials": {"background": "14th Amendment principles"}
            },
            {
                "subtopic": "Constitutional Law",
                "title": "Executive Power Limits",
                "description": "Analysis of presidential power boundaries",
                "difficulty": 4,
                "specialization": "Government Powers",
                "learning_objectives": ["Executive authority", "Separation of powers"],
                "context_materials": {"background": "Presidential power history"}
            },
            {
                "subtopic": "Constitutional Law",
                "title": "Privacy Rights Evolution",
                "description": "Study of constitutional privacy protections",
                "difficulty": 3,
                "specialization": "Privacy Law",
                "learning_objectives": ["Privacy rights development", "Modern challenges"],
                "context_materials": {"background": "Privacy rights history"}
            },
            {
                "subtopic": "Constitutional Law",
                "title": "Federalism Challenges",
                "description": "Analysis of state and federal power balance",
                "difficulty": 4,
                "specialization": "Federal Powers",
                "learning_objectives": ["Federal-state relations", "Commerce clause"],
                "context_materials": {"background": "Federalism principles"}
            },

            # Contract Law Cases
            {
                "subtopic": "Contract Law",
                "title": "Digital Contract Formation",
                "description": "Modern contract creation in digital age",
                "difficulty": 2,
                "specialization": "Digital Law",
                "learning_objectives": ["Online contracts", "Digital signatures"],
                "context_materials": {"background": "E-commerce law"}
            },
            {
                "subtopic": "Contract Law",
                "title": "Breach and Remedies",
                "description": "Comprehensive study of contract breaches",
                "difficulty": 3,
                "specialization": "Business Law",
                "learning_objectives": ["Types of breach", "Available remedies"],
                "context_materials": {"background": "Contract remedies"}
            },
            {
                "subtopic": "Contract Law",
                "title": "International Contracts",
                "description": "Cross-border agreement analysis",
                "difficulty": 5,
                "specialization": "International Business",
                "learning_objectives": ["International law", "Choice of law"],
                "context_materials": {"background": "International trade law"}
            },
            {
                "subtopic": "Contract Law",
                "title": "Consumer Contracts",
                "description": "Study of consumer protection in contracts",
                "difficulty": 2,
                "specialization": "Consumer Law",
                "learning_objectives": ["Consumer rights", "Standard terms"],
                "context_materials": {"background": "Consumer protection"}
            },
            {
                "subtopic": "Contract Law",
                "title": "Employment Contracts",
                "description": "Analysis of workplace agreements",
                "difficulty": 3,
                "specialization": "Employment Law",
                "learning_objectives": ["Employment terms", "Worker rights"],
                "context_materials": {"background": "Labor law principles"}
            },

            # Tort Law Cases
            {
                "subtopic": "Tort Law",
                "title": "Medical Negligence",
                "description": "Healthcare provider liability analysis",
                "difficulty": 4,
                "specialization": "Healthcare Law",
                "learning_objectives": ["Medical standard of care", "Causation"],
                "context_materials": {"background": "Medical liability"}
            },
            {
                "subtopic": "Tort Law",
                "title": "Product Liability Study",
                "description": "Manufacturing defect analysis",
                "difficulty": 3,
                "specialization": "Consumer Protection",
                "learning_objectives": ["Defect types", "Liability standards"],
                "context_materials": {"background": "Product safety law"}
            },
            {
                "subtopic": "Tort Law",
                "title": "Environmental Torts",
                "description": "Study of environmental damage liability",
                "difficulty": 5,
                "specialization": "Environmental Law",
                "learning_objectives": ["Environmental harm", "Causation challenges"],
                "context_materials": {"background": "Environmental regulation"}
            },
            {
                "subtopic": "Tort Law",
                "title": "Digital Privacy Torts",
                "description": "Modern privacy violations analysis",
                "difficulty": 4,
                "specialization": "Privacy Law",
                "learning_objectives": ["Online privacy", "Data protection"],
                "context_materials": {"background": "Digital privacy law"}
            },
            {
                "subtopic": "Tort Law",
                "title": "Defamation in Digital Age",
                "description": "Online reputation damage analysis",
                "difficulty": 3,
                "specialization": "Media Law",
                "learning_objectives": ["Digital defamation", "Social media impact"],
                "context_materials": {"background": "Modern defamation law"}
            }
        ]

        # Add cases
        for case_data in cases_data:
            subtopic_name = case_data.pop("subtopic")
            # Check if case already exists
            existing_case = db.query(CaseStudy).filter(
                CaseStudy.title == case_data["title"]
            ).first()
            
            if not existing_case:
                # Create a unique share_slug
                title_slug = case_data["title"].lower().replace(" ", "-")
                case = CaseStudy(
                    subtopic_id=subtopics[subtopic_name].id,
                    share_slug=title_slug,
                    **case_data
                )
                db.add(case)

        db.commit()


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
