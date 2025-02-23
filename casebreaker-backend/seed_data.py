from sqlalchemy.orm import Session
from sqlalchemy import text
from casebreaker_backend.database import SessionLocal
from casebreaker_backend.models import Field, Subtopic, CaseStudy

# Field definitions with unique Unsplash images
FIELDS = [
    {
        "name": "Health & Medicine",
        "description": "Explore medical cases, healthcare innovations, and clinical practice",
        "icon_url": "https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=800&auto=format&fit=crop&q=60",
        "subtopics": [
            {
                "name": "Clinical Practice",
                "description": "Medical diagnosis, treatment planning, and patient care",
                "cases": [
                    {
                        "title": "Personalized Genomic Medicine",
                        "description": "Application of genetic testing and personalized treatment plans in modern healthcare",
                        "difficulty": 3,
                        "specialization": "Genomic Medicine",
                        "learning_objectives": [
                            "Understanding genetic testing methodologies",
                            "Interpreting genomic data for clinical decisions",
                            "Ethical considerations in genetic medicine",
                        ],
                        "context_materials": {
                            "background": "Evolution of genomic medicine",
                            "key_concepts": [
                                "DNA sequencing technologies",
                                "Pharmacogenomics",
                                "Genetic counseling principles",
                            ],
                            "required_reading": "Principles of Genomic Medicine, 2nd Edition",
                        },
                        "checkpoints": [
                            {
                                "id": "1",
                                "title": "Genetic Testing Basics",
                                "description": "Evaluate different genetic testing methods and their applications",
                                "hints": [
                                    "Consider both diagnostic and predictive testing"
                                ],
                            },
                            {
                                "id": "2",
                                "title": "Clinical Integration",
                                "description": "Design a treatment plan based on genetic test results",
                                "hints": ["Think about drug metabolism variations"],
                            },
                            {
                                "id": "3",
                                "title": "Ethical Implications",
                                "description": "Address ethical challenges in genomic medicine",
                                "hints": ["Consider privacy and discrimination issues"],
                            },
                        ],
                        "source_url": "http://example.com/genomic-medicine",
                        "source_type": "GENERATED",
                        "share_slug": "personalized-genomic-medicine",
                        "estimated_time": 15,
                    }
                ],
            },
            {
                "name": "Laboratory Medicine",
                "description": "Clinical laboratory diagnostics, test interpretation, and pathology",
                "cases": [
                    {
                        "title": "Unexpected High IgE: A Clinical Laboratory Investigation",
                        "description": "Analysis of an unusual case where extremely high IgE levels led to the discovery of a rare monoclonal gammopathy",
                        "difficulty": 3,
                        "specialization": "Clinical Chemistry",
                        "learning_objectives": [
                            "Interpret serum protein electrophoresis and immunofixation results",
                            "Understand the diagnostic approach to monoclonal gammopathies",
                            "Evaluate laboratory interferents and validation methods",
                            "Analyze the relationship between clinical presentation and laboratory findings"
                        ],
                        "context_materials": {
                            "background": "Clinical laboratory investigation of monoclonal gammopathies",
                            "key_concepts": [
                                "Serum protein electrophoresis",
                                "Immunoglobulin quantification",
                                "Monoclonal gammopathy diagnosis",
                                "Laboratory test validation",
                                "Flow cytometry in plasma cell disorders"
                            ],
                            "required_reading": "ADLM Clinical Case Studies 2025: High IgE Level Case"
                        },
                        "checkpoints": [
                            {
                                "id": "1",
                                "title": "Initial Clinical Assessment",
                                "description": "Analyze the patient's presenting symptoms and initial findings",
                                "hints": [
                                    "Consider the significance of hemoptysis in relation to the patient's history",
                                    "Review the thoracic scan findings and their implications"
                                ]
                            },
                            {
                                "id": "2",
                                "title": "Laboratory Data Interpretation",
                                "description": "Interpret the initial laboratory findings and their clinical significance",
                                "hints": [
                                    "Focus on the IgE levels and their reference ranges",
                                    "Evaluate the complete blood count abnormalities"
                                ]
                            },
                            {
                                "id": "3",
                                "title": "Protein Studies Analysis",
                                "description": "Evaluate the serum protein electrophoresis and immunofixation results",
                                "hints": [
                                    "Examine the gamma-globulin fraction abnormalities",
                                    "Consider the significance of the lambda monoclonal band"
                                ]
                            },
                            {
                                "id": "4",
                                "title": "Advanced Diagnostic Testing",
                                "description": "Analyze bone marrow findings and molecular studies",
                                "hints": [
                                    "Review flow cytometry markers in plasma cell disorders",
                                    "Consider the significance of t(11;14) translocation"
                                ]
                            },
                            {
                                "id": "5",
                                "title": "Final Diagnosis",
                                "description": "Synthesize all findings to reach the final diagnosis",
                                "hints": [
                                    "Review criteria for MGUS vs Multiple Myeloma",
                                    "Consider the significance of follow-up findings"
                                ]
                            }
                        ],
                        "source_url": "https://myadlm.org/science-and-research/clinical-chemistry/clinical-case-studies/2025/an-unexpectedly-high-ige-level-during-allergic-exploration",
                        "source_type": "EXTERNAL",
                        "share_slug": "unexpected-high-ige-case",
                        "estimated_time": 25
                    }
                ]
            }
        ],
    },
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
                            "required_reading": "Miranda v. Arizona, 384 U.S. 436 (1966)",
                        },
                        "checkpoints": [
                            {
                                "id": "1",
                                "title": "Background Understanding",
                                "description": "Explain the historical context of Miranda rights",
                                "hints": [
                                    "Consider the state of criminal procedure before 1966"
                                ],
                            },
                            {
                                "id": "2",
                                "title": "Rights Analysis",
                                "description": "List and explain each Miranda right",
                                "hints": [
                                    "Think about both explicit and implicit rights"
                                ],
                            },
                            {
                                "id": "3",
                                "title": "Modern Application",
                                "description": "Discuss how Miranda rights apply in contemporary situations",
                                "hints": [
                                    "Consider digital communications and modern police work"
                                ],
                            },
                        ],
                        "source_url": "http://example.com/miranda-rights",
                        "source_type": "GENERATED",
                        "share_slug": "miranda-rights-case",
                        "estimated_time": 20,
                    },
                    {
                        "title": "Digital Evidence Collection",
                        "description": "Modern approaches to gathering and preserving digital evidence in criminal investigations",
                        "difficulty": 3,
                        "specialization": "Digital Forensics",
                        "learning_objectives": [
                            "Digital evidence handling best practices",
                            "Chain of custody maintenance in digital environments",
                            "Privacy considerations and legal requirements",
                        ],
                        "context_materials": {
                            "background": "Digital age criminal procedure",
                            "key_concepts": [
                                "Digital forensics principles",
                                "Evidence preservation techniques",
                                "Legal framework for digital evidence",
                            ],
                            "required_reading": "Digital Evidence and Computer Crime, 3rd Edition",
                        },
                        "checkpoints": [
                            {
                                "id": "1",
                                "title": "Evidence Identification",
                                "description": "Identify potential sources of digital evidence in a case",
                                "hints": ["Consider both hardware and cloud storage"],
                            },
                            {
                                "id": "2",
                                "title": "Collection Process",
                                "description": "Design a proper evidence collection procedure",
                                "hints": ["Remember to maintain chain of custody"],
                            },
                            {
                                "id": "3",
                                "title": "Legal Compliance",
                                "description": "Ensure collection methods comply with privacy laws",
                                "hints": [
                                    "Consider jurisdiction-specific requirements"
                                ],
                            },
                        ],
                        "source_url": "http://example.com/digital-evidence",
                        "source_type": "GENERATED",
                        "share_slug": "digital-evidence-collection",
                        "estimated_time": 10,
                    },
                ],
            }
        ],
    },
    {
        "name": "Economics & Finance",
        "description": "Explore financial markets, corporate strategy, and economic decision-making",
        "icon_url": "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?w=800&auto=format&fit=crop&q=60",
        "subtopics": [
            {
                "name": "Corporate Finance",
                "description": "Study of financial decisions and strategies in corporate environments",
                "cases": [
                    {
                        "title": "Hertz Global Holdings: Capital Structure Strategy",
                        "description": "Analysis of Hertz's strategic decisions regarding debt financing, asset-backed securities, and equity issuance in 2019",
                        "difficulty": 3,
                        "specialization": "Financial Management",
                        "learning_objectives": [
                            "Analyze the use of asset-backed securities in corporate financing",
                            "Evaluate trade-offs between debt and equity financing",
                            "Understand special-purpose entities and bankruptcy-remote structures",
                            "Assess risk management in fleet financing and depreciation",
                            "Examine market reactions to corporate financing decisions"
                        ],
                        "context_materials": {
                            "background": "Evolution of Hertz's capital structure from 1918 to 2019",
                            "key_concepts": [
                                "Asset-Backed Securities (ABS)",
                                "Special Purpose Entities",
                                "Program vs Non-Program Vehicles",
                                "Capital Structure Theory",
                                "Rights Offerings",
                                "Market Signal Theory"
                            ],
                            "required_reading": "Yale SOM Case Study: Hertz Global Holdings (A)"
                        },
                        "checkpoints": [
                            {
                                "id": "1",
                                "title": "Business Model Analysis",
                                "description": "Evaluate Hertz's core business model and operational scale",
                                "hints": [
                                    "Consider the significance of fleet size and location network",
                                    "Analyze the importance of airport locations in their business model"
                                ]
                            },
                            {
                                "id": "2",
                                "title": "ABS Structure Assessment",
                                "description": "Analyze Hertz's asset-backed securities program and special-purpose entities",
                                "hints": [
                                    "Examine the benefits of bankruptcy-remote trusts",
                                    "Consider how ABS reduces interest costs"
                                ]
                            },
                            {
                                "id": "3",
                                "title": "Risk Management Evaluation",
                                "description": "Assess Hertz's approach to managing fleet depreciation risk",
                                "hints": [
                                    "Compare Program vs Non-Program vehicle strategies",
                                    "Analyze manufacturer repurchase agreements"
                                ]
                            },
                            {
                                "id": "4",
                                "title": "Debt Structure Analysis",
                                "description": "Evaluate Hertz's mix of secured and unsecured debt",
                                "hints": [
                                    "Consider the implications of high leverage",
                                    "Analyze the 2019 debt refinancing decision"
                                ]
                            },
                            {
                                "id": "5",
                                "title": "Strategic Recommendations",
                                "description": "Develop recommendations for Hertz's capital structure",
                                "hints": [
                                    "Consider market reactions to equity issuance",
                                    "Evaluate alternatives to rebalance the capital structure"
                                ]
                            }
                        ],
                        "source_url": "https://cases.som.yale.edu/hertz-global-holdings-uses-debt-and-equity",
                        "source_type": "EXTERNAL",
                        "share_slug": "hertz-capital-structure",
                        "estimated_time": 30
                    }
                ]
            }
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
                        checkpoints=case_data["checkpoints"],
                        source_url=case_data["source_url"],
                        source_type=case_data["source_type"],
                        share_slug=case_data["share_slug"],
                        estimated_time=case_data["estimated_time"],
                        subtopic_id=subtopic.id,
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
