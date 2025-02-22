from sqlalchemy.orm import Session
from sqlalchemy import text
from casebreaker_backend.database import SessionLocal
from casebreaker_backend.models import Field, Subtopic, CaseStudy

# Field definitions with unique Unsplash images
FIELDS = [
    {
        "name": "Law",
        "description": "Explore legal principles, cases, and justice system fundamentals",
        "icon_url": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=800&auto=format&fit=crop&q=60",
        "subtopics": [
            {
                "name": "Criminal Law",
                "description": "Study of criminal justice system and procedures",
                "cases": [
                    {
                        "title": "The Miranda Rights Case",
                        "description": "Analysis of the landmark case establishing police obligation to inform suspects of their rights",
                        "difficulty": 2,
                        "specialization": "Criminal Procedure",
                        "learning_objectives": [
                            "Understanding Miranda rights",
                            "Police procedure basics",
                            "Constitutional protections",
                        ],
                        "context_materials": {
                            "background": "1966 Supreme Court case",
                            "key_principles": [
                                "Right to remain silent",
                                "Right to attorney",
                            ],
                        },
                    },
                    {
                        "title": "Digital Evidence Collection",
                        "description": "Modern approaches to gathering and preserving digital evidence",
                        "difficulty": 3,
                        "specialization": "Digital Forensics",
                        "learning_objectives": [
                            "Digital evidence handling",
                            "Chain of custody",
                            "Privacy considerations",
                        ],
                        "context_materials": {
                            "background": "Digital age criminal procedure"
                        },
                    },
                ],
            },
            {
                "name": "Contract Law",
                "description": "Understanding formation and enforcement of agreements",
                "cases": [
                    {
                        "title": "Online Agreement Validity",
                        "description": "Examining the enforceability of click-wrap agreements",
                        "difficulty": 1,
                        "specialization": "E-Commerce Law",
                        "learning_objectives": [
                            "Digital contract formation",
                            "Consumer protection",
                        ],
                        "context_materials": {
                            "background": "Modern contract formation"
                        },
                    }
                ],
            },
            {
                "name": "Property Law",
                "description": "Rights and regulations regarding property ownership",
                "cases": [
                    {
                        "title": "Digital Property Rights",
                        "description": "Ownership rights in virtual assets and cryptocurrencies",
                        "difficulty": 3,
                        "specialization": "Digital Property",
                        "learning_objectives": [
                            "Virtual asset ownership",
                            "Blockchain implications",
                        ],
                        "context_materials": {
                            "background": "Evolution of property rights"
                        },
                    },
                    {
                        "title": "Airspace Rights",
                        "description": "Property rights in the context of drone usage",
                        "difficulty": 2,
                        "specialization": "Modern Property Law",
                        "learning_objectives": [
                            "Airspace regulations",
                            "Privacy rights",
                        ],
                        "context_materials": {"background": "Drone law development"},
                    },
                ],
            },
        ],
    },
    {
        "name": "Healthcare",
        "description": "Study medical practices, ethics, and healthcare management",
        "icon_url": "https://images.unsplash.com/photo-1631248055158-edec7a3c072b?w=800&auto=format&fit=crop&q=60",
        "subtopics": [
            {
                "name": "Emergency Medicine",
                "description": "Critical care and emergency response",
                "cases": [
                    {
                        "title": "Triage Decision Making",
                        "description": "Emergency resource allocation in mass casualty events",
                        "difficulty": 3,
                        "specialization": "Emergency Response",
                        "learning_objectives": [
                            "Triage protocols",
                            "Resource management",
                        ],
                        "context_materials": {"background": "Mass casualty management"},
                    }
                ],
            },
            {
                "name": "Medical Ethics",
                "description": "Ethical considerations in healthcare",
                "cases": [
                    {
                        "title": "AI in Diagnosis",
                        "description": "Ethical implications of AI-assisted medical diagnosis",
                        "difficulty": 2,
                        "specialization": "Medical Technology",
                        "learning_objectives": ["AI ethics", "Patient privacy"],
                        "context_materials": {"background": "AI in healthcare"},
                    },
                    {
                        "title": "Informed Consent",
                        "description": "Patient autonomy and medical decision-making",
                        "difficulty": 1,
                        "specialization": "Patient Rights",
                        "learning_objectives": [
                            "Consent requirements",
                            "Patient communication",
                        ],
                        "context_materials": {
                            "background": "Medical consent evolution"
                        },
                    },
                ],
            },
            {
                "name": "Public Health",
                "description": "Population health and disease prevention",
                "cases": [
                    {
                        "title": "Vaccine Distribution",
                        "description": "Equitable distribution of limited medical resources",
                        "difficulty": 2,
                        "specialization": "Health Policy",
                        "learning_objectives": [
                            "Distribution ethics",
                            "Public health planning",
                        ],
                        "context_materials": {
                            "background": "Vaccine program management"
                        },
                    }
                ],
            },
            {
                "name": "Healthcare Technology",
                "description": "Modern medical technology and innovation",
                "cases": [
                    {
                        "title": "Telemedicine Implementation",
                        "description": "Remote healthcare delivery systems",
                        "difficulty": 2,
                        "specialization": "Digital Health",
                        "learning_objectives": [
                            "Remote care protocols",
                            "Technology integration",
                        ],
                        "context_materials": {"background": "Telemedicine evolution"},
                    }
                ],
            },
        ],
    },
    {
        "name": "Economics",
        "description": "Understand economic principles and market dynamics",
        "icon_url": "https://images.unsplash.com/photo-1543286386-2e659306cd6c?w=800&auto=format&fit=crop&q=60",
        "subtopics": [
            {
                "name": "Microeconomics",
                "description": "Individual market and business decisions",
                "cases": [
                    {
                        "title": "Pricing Strategy",
                        "description": "Dynamic pricing in digital marketplaces",
                        "difficulty": 2,
                        "specialization": "Market Pricing",
                        "learning_objectives": [
                            "Price optimization",
                            "Market response",
                        ],
                        "context_materials": {
                            "background": "Digital marketplace economics"
                        },
                    }
                ],
            },
            {
                "name": "Development Economics",
                "description": "Economic growth and development strategies",
                "cases": [
                    {
                        "title": "Digital Inclusion",
                        "description": "Technology access in developing economies",
                        "difficulty": 3,
                        "specialization": "Economic Development",
                        "learning_objectives": [
                            "Digital divide",
                            "Development strategies",
                        ],
                        "context_materials": {
                            "background": "Technology adoption patterns"
                        },
                    }
                ],
            },
            {
                "name": "Environmental Economics",
                "description": "Economic aspects of environmental protection",
                "cases": [
                    {
                        "title": "Carbon Trading",
                        "description": "Market-based environmental protection",
                        "difficulty": 3,
                        "specialization": "Environmental Policy",
                        "learning_objectives": [
                            "Market mechanisms",
                            "Environmental impact",
                        ],
                        "context_materials": {
                            "background": "Carbon market development"
                        },
                    }
                ],
            },
            {
                "name": "Behavioral Economics",
                "description": "Psychology of economic decisions",
                "cases": [
                    {
                        "title": "Digital Consumer Behavior",
                        "description": "Online shopping decision patterns",
                        "difficulty": 1,
                        "specialization": "Consumer Psychology",
                        "learning_objectives": ["Decision making", "Digital influence"],
                        "context_materials": {"background": "E-commerce psychology"},
                    }
                ],
            },
        ],
    },
    {
        "name": "Finance",
        "description": "Financial markets, instruments, and strategies",
        "icon_url": "https://images.unsplash.com/photo-1590283603385-17ffb3a7f29f?w=800&auto=format&fit=crop&q=60",
        "subtopics": [
            {
                "name": "Investment Analysis",
                "description": "Evaluating investment opportunities",
                "cases": [
                    {
                        "title": "Crypto Investment",
                        "description": "Digital asset investment strategy",
                        "difficulty": 3,
                        "specialization": "Digital Assets",
                        "learning_objectives": [
                            "Risk assessment",
                            "Portfolio management",
                        ],
                        "context_materials": {"background": "Cryptocurrency markets"},
                    }
                ],
            },
            {
                "name": "Corporate Finance",
                "description": "Financial management in organizations",
                "cases": [
                    {
                        "title": "Digital Transformation",
                        "description": "Financing technology upgrades",
                        "difficulty": 2,
                        "specialization": "Technology Investment",
                        "learning_objectives": ["Investment planning", "ROI analysis"],
                        "context_materials": {"background": "Digital transformation"},
                    }
                ],
            },
            {
                "name": "Financial Technology",
                "description": "Modern financial services and technology",
                "cases": [
                    {
                        "title": "Mobile Payment Systems",
                        "description": "Digital payment infrastructure",
                        "difficulty": 1,
                        "specialization": "Payment Technology",
                        "learning_objectives": [
                            "Payment processing",
                            "Security measures",
                        ],
                        "context_materials": {
                            "background": "Digital payments evolution"
                        },
                    }
                ],
            },
            {
                "name": "Risk Management",
                "description": "Managing financial risks",
                "cases": [
                    {
                        "title": "Cybersecurity Insurance",
                        "description": "Digital risk protection strategies",
                        "difficulty": 2,
                        "specialization": "Digital Risk",
                        "learning_objectives": [
                            "Risk assessment",
                            "Insurance planning",
                        ],
                        "context_materials": {"background": "Cyber insurance market"},
                    }
                ],
            },
        ],
    },
    {
        "name": "History",
        "description": "Historical events, patterns, and their impact",
        "icon_url": "https://images.unsplash.com/photo-1461360370896-922624d12aa1?w=800&auto=format&fit=crop&q=60",
        "subtopics": [
            {
                "name": "Digital Revolution",
                "description": "History of computing and internet",
                "cases": [
                    {
                        "title": "Birth of Internet",
                        "description": "Development of the World Wide Web",
                        "difficulty": 1,
                        "specialization": "Tech History",
                        "learning_objectives": [
                            "Internet development",
                            "Key innovations",
                        ],
                        "context_materials": {"background": "Early internet history"},
                    }
                ],
            },
            {
                "name": "Modern Warfare",
                "description": "Evolution of military technology",
                "cases": [
                    {
                        "title": "Cyber Warfare",
                        "description": "Digital conflict and defense",
                        "difficulty": 3,
                        "specialization": "Military Technology",
                        "learning_objectives": [
                            "Digital warfare",
                            "Defense strategies",
                        ],
                        "context_materials": {"background": "Cyber warfare evolution"},
                    }
                ],
            },
            {
                "name": "Social Movements",
                "description": "Historical social changes",
                "cases": [
                    {
                        "title": "Digital Activism",
                        "description": "Social media's role in modern movements",
                        "difficulty": 2,
                        "specialization": "Digital Society",
                        "learning_objectives": ["Online organizing", "Movement impact"],
                        "context_materials": {"background": "Social media activism"},
                    }
                ],
            },
            {
                "name": "Economic History",
                "description": "Evolution of economic systems",
                "cases": [
                    {
                        "title": "Digital Currency Evolution",
                        "description": "History of money to cryptocurrency",
                        "difficulty": 2,
                        "specialization": "Financial History",
                        "learning_objectives": [
                            "Currency evolution",
                            "Digital transformation",
                        ],
                        "context_materials": {"background": "Money evolution"},
                    }
                ],
            },
        ],
    },
]


def seed_data():
    db = SessionLocal()
    try:
        # Purge all tables
        db.execute(text("PRAGMA foreign_keys=OFF"))
        db.execute(text("DELETE FROM case_studies"))
        db.execute(text("DELETE FROM subtopics"))
        db.execute(text("DELETE FROM fields"))
        db.execute(text("PRAGMA foreign_keys=ON"))
        db.commit()

        # Create all fields
        fields = {}
        for field_data in FIELDS:
            field = Field(
                name=field_data["name"],
                description=field_data["description"],
                icon_url=field_data["icon_url"],
            )
            db.add(field)
            db.commit()
            db.refresh(field)
            fields[field_data["name"]] = field

        # Create all subtopics
        subtopics = {}
        for field_data in FIELDS:
            field = fields[field_data["name"]]
            for subtopic_data in field_data["subtopics"]:
                subtopic = Subtopic(
                    name=subtopic_data["name"],
                    description=subtopic_data["description"],
                    field_id=field.id,
                )
                db.add(subtopic)
                db.commit()
                db.refresh(subtopic)
                subtopics[f"{field_data['name']}_{subtopic_data['name']}"] = subtopic

        # Create all cases
        for field_data in FIELDS:
            for subtopic_data in field_data["subtopics"]:
                subtopic = subtopics[f"{field_data['name']}_{subtopic_data['name']}"]
                for case_data in subtopic_data["cases"]:
                    # Create a unique share_slug
                    title_slug = case_data["title"].lower().replace(" ", "-")

                    case = CaseStudy(
                        title=case_data["title"],
                        description=case_data["description"],
                        difficulty=case_data["difficulty"],
                        specialization=case_data["specialization"],
                        learning_objectives=case_data["learning_objectives"],
                        context_materials=case_data["context_materials"],
                        subtopic_id=subtopic.id,
                        share_slug=title_slug,
                    )
                    db.add(case)
                    db.commit()

    except Exception as e:
        print(f"Error seeding data: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_data()
    print("Data seeding completed successfully!")
