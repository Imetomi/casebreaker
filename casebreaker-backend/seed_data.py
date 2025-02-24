from sqlalchemy.orm import Session
from sqlalchemy import text
from casebreaker_backend.database import SessionLocal
from casebreaker_backend.models import Field, Subtopic, CaseStudy

# Field definitions with unique Unsplash images
FIELDS = [
    {
        "name": "Marketing",
        "description": "Explore marketing strategies, consumer behavior, and brand development",
        "icon_url": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&auto=format&fit=crop&q=60",
        "subtopics": [
            {
                "name": "Digital Marketing",
                "description": "Modern digital marketing strategies and analytics",
                "cases": [
                    {
                        "title": "Netflix's Content Marketing Revolution",
                        "description": "Analysis of Netflix's innovative approach to social media and content marketing strategy",
                        "difficulty": 2,
                        "specialization": "Content Marketing",
                        "source_url": "https://about.netflix.com/en/news/social-marketing",
                        "source_type": "case_study",
                        "share_slug": "netflix-content-marketing-revolution",
                        "estimated_time": 45,
                        "learning_objectives": [
                            "Analyze Netflix's social media engagement strategies",
                            "Evaluate the effectiveness of multi-platform content distribution",
                            "Understand the role of data analytics in content personalization",
                            "Assess the impact of brand voice in social media success",
                        ],
                        "context_materials": {
                            "cards": [
                                {
                                    "title": "Netflix's Social Media Presence",
                                    "description": "Netflix maintains distinct brand voices across platforms: witty on Twitter, visual on Instagram, and engaging on TikTok. Their social media team creates platform-specific content that resonates with each audience.",
                                },
                                {
                                    "title": "Content Distribution Strategy",
                                    "description": "Netflix employs a multi-platform approach, creating behind-the-scenes content, memes, and show clips. They use data analytics to determine optimal posting times and content types for each platform.",
                                },
                                {
                                    "title": "Engagement Metrics",
                                    "description": "Key performance indicators include engagement rates, follower growth, and content virality. Netflix's social media accounts consistently outperform industry averages in these metrics.",
                                },
                                {
                                    "title": "Brand Voice Guidelines",
                                    "description": "Netflix's brand voice is characterized by humor, pop culture references, and authentic fan engagement. Their social media team follows strict guidelines while maintaining a casual, relatable tone.",
                                },
                            ]
                        },
                        "pitfalls": [
                            {
                                "id": "p1",
                                "title": "Over-reliance on Automation",
                                "description": "Focusing too much on automated posting without maintaining authentic engagement",
                            },
                            {
                                "id": "p2",
                                "title": "Inconsistent Brand Voice",
                                "description": "Failing to maintain a consistent tone and messaging across different platforms",
                            },
                            {
                                "id": "p3",
                                "title": "Ignoring Platform Specifics",
                                "description": "Using the same content approach across all platforms without considering platform-specific best practices",
                            },
                        ],
                        "checkpoints": [
                            {
                                "id": "1",
                                "title": "Platform Analysis",
                                "description": "Examine Netflix's presence across different social media platforms",
                                "hints": [
                                    "Compare content styles across platforms",
                                    "Look for platform-specific engagement strategies",
                                    "Note differences in posting frequency and timing",
                                ],
                            },
                            {
                                "id": "2",
                                "title": "Content Strategy Review",
                                "description": "Analyze the types of content and their effectiveness",
                                "hints": [
                                    "Identify different content categories",
                                    "Consider how content ties to streaming releases",
                                    "Evaluate engagement metrics for different content types",
                                ],
                            },
                            {
                                "id": "3",
                                "title": "Data Analysis",
                                "description": "Review the role of data in content optimization",
                                "hints": [
                                    "Look at how Netflix uses engagement metrics",
                                    "Consider the role of A/B testing",
                                    "Examine content performance patterns",
                                ],
                            },
                            {
                                "id": "4",
                                "title": "Strategy Recommendations",
                                "description": "Develop recommendations for improving the strategy",
                                "hints": [
                                    "Consider emerging social media trends",
                                    "Think about content scalability",
                                    "Suggest ways to improve engagement",
                                ],
                            },
                        ],
                    }
                ],
            }
        ],
    },
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
                            "cards": [
                                {
                                    "title": "Genomic Medicine Overview",
                                    "description": "Genomic medicine involves using genomic information about an individual as part of their clinical care. It includes genetic testing and counseling to guide treatment decisions.",
                                },
                                {
                                    "title": "Genetic Testing",
                                    "description": "Genetic testing involves analyzing DNA to identify changes in genes that may cause illness or disease. It helps in diagnosing genetic disorders and tailoring personalized treatments.",
                                },
                                {
                                    "title": "Ethical Considerations",
                                    "description": "Ethical considerations in genetic medicine include informed consent, privacy of genetic information, and the potential for genetic discrimination.",
                                },
                                {
                                    "title": "Clinical Integration",
                                    "description": "Integrating genetic information into clinical practice involves using genetic tests to inform diagnosis, treatment, and prevention strategies.",
                                },
                                {
                                    "title": "Key Concepts",
                                    "description": "Key concepts include DNA sequencing technologies, pharmacogenomics, and genetic counseling principles.",
                                },
                                {
                                    "title": "Required Reading",
                                    "description": "Principles of Genomic Medicine, 2nd Edition provides comprehensive insights into the field of genomic medicine.",
                                },
                            ]
                        },
                        "pitfalls": [
                            {
                                "id": "p1",
                                "title": "Overemphasis on Technical Details",
                                "description": "Getting too focused on technical genetic data without considering practical clinical applications",
                            },
                            {
                                "id": "p2",
                                "title": "Privacy Oversight",
                                "description": "Neglecting patient privacy considerations when handling genetic information",
                            },
                        ],
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
                            "Analyze the relationship between clinical presentation and laboratory findings",
                        ],
                        "context_materials": {
                            "cards": [
                                {
                                    "title": "Laboratory Medicine Overview",
                                    "description": "Laboratory medicine focuses on the analysis of bodily fluids and tissues for diagnostic purposes. It plays a critical role in disease detection and management.",
                                },
                                {
                                    "title": "Serum Protein Electrophoresis",
                                    "description": "Serum protein electrophoresis is used to separate proteins in the blood based on their size and charge. It helps identify abnormal protein levels indicative of disease.",
                                },
                                {
                                    "title": "Monoclonal Gammopathy Diagnosis",
                                    "description": "Monoclonal gammopathy is diagnosed through serum protein electrophoresis, which identifies abnormal monoclonal protein bands. Further tests, such as immunofixation electrophoresis and bone marrow biopsy, help confirm the diagnosis and assess the extent of plasma cell proliferation.",
                                },
                                {
                                    "title": "Laboratory Test Validation",
                                    "description": "Validation of laboratory tests ensures accuracy and reliability, involving calibration, quality control, and proficiency testing.",
                                },
                                {
                                    "title": "Key Concepts",
                                    "description": "Key concepts include serum protein electrophoresis, immunoglobulin quantification, and laboratory test validation.",
                                },
                                {
                                    "title": "Required Reading",
                                    "description": "ADLM Clinical Case Studies 2025: High IgE Level Case provides detailed case studies for practical understanding.",
                                },
                            ],
                        },
                        "pitfalls": [
                            {
                                "id": "p1",
                                "title": "Premature Conclusions",
                                "description": "Jumping to diagnostic conclusions based on initial IgE levels without considering other possibilities",
                            },
                            {
                                "id": "p2",
                                "title": "Incomplete Analysis",
                                "description": "Failing to consider the full spectrum of laboratory findings in the diagnostic process",
                            },
                        ],
                        "checkpoints": [
                            {
                                "id": "1",
                                "title": "Initial Clinical Assessment",
                                "description": "Analyze the patient's presenting symptoms and initial findings",
                                "hints": [
                                    "Consider the significance of hemoptysis in relation to the patient's history",
                                    "Review the thoracic scan findings and their implications",
                                ],
                            },
                            {
                                "id": "2",
                                "title": "Laboratory Data Interpretation",
                                "description": "Interpret the initial laboratory findings and their clinical significance",
                                "hints": [
                                    "Focus on the IgE levels and their reference ranges",
                                    "Evaluate the complete blood count abnormalities",
                                ],
                            },
                            {
                                "id": "3",
                                "title": "Protein Studies Analysis",
                                "description": "Evaluate the serum protein electrophoresis and immunofixation results",
                                "hints": [
                                    "Examine the gamma-globulin fraction abnormalities",
                                    "Consider the significance of the lambda monoclonal band",
                                ],
                            },
                            {
                                "id": "4",
                                "title": "Advanced Diagnostic Testing",
                                "description": "Analyze bone marrow findings and molecular studies",
                                "hints": [
                                    "Review flow cytometry markers in plasma cell disorders",
                                    "Consider the significance of t(11;14) translocation",
                                ],
                            },
                            {
                                "id": "5",
                                "title": "Final Diagnosis",
                                "description": "Synthesize all findings to reach the final diagnosis",
                                "hints": [
                                    "Review criteria for MGUS vs Multiple Myeloma",
                                    "Consider the significance of follow-up findings",
                                ],
                            },
                        ],
                        "source_url": "https://myadlm.org/science-and-research/clinical-chemistry/clinical-case-studies/2025/an-unexpectedly-high-ige-level-during-allergic-exploration",
                        "source_type": "EXTERNAL",
                        "share_slug": "unexpected-high-ige-case",
                        "estimated_time": 25,
                    }
                ],
            },
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
                            "cards": [
                                {
                                    "title": "Miranda Rights Overview",
                                    "description": "Miranda rights are a legal requirement ensuring that individuals are informed of their rights during an arrest, including the right to remain silent and the right to an attorney.",
                                },
                                {
                                    "title": "Police Procedure",
                                    "description": "Police procedures involve the standardized methods used by law enforcement to ensure legal compliance and protect individual rights during investigations.",
                                },
                                {
                                    "title": "Constitutional Protections",
                                    "description": "Constitutional protections safeguard individual rights against government actions, ensuring due process and equal protection under the law.",
                                },
                                {
                                    "title": "Landmark Case Analysis",
                                    "description": "Analyzing landmark cases like Miranda v. Arizona helps understand the evolution of legal precedents and their impact on modern law enforcement.",
                                },
                                {
                                    "title": "Key Concepts",
                                    "description": "Key concepts include the right to remain silent and the right to an attorney.",
                                },
                                {
                                    "title": "Required Reading",
                                    "description": "Miranda v. Arizona, 384 U.S. 436 (1966) is a foundational case for understanding Miranda rights and their application.",
                                },
                            ],
                        },
                        "pitfalls": [
                            {
                                "id": "p1",
                                "title": "Oversimplification",
                                "description": "Treating Miranda rights as a simple checklist without understanding their deeper legal implications",
                            },
                            {
                                "id": "p2",
                                "title": "Historical Context Neglect",
                                "description": "Failing to consider the historical context and evolution of criminal procedure rights",
                            },
                        ],
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
                            "cards": [
                                {
                                    "title": "Digital Forensics Overview",
                                    "description": "Digital forensics involves the recovery and investigation of material found in digital devices, often related to computer crime. It includes data preservation, analysis, and presentation in court.",
                                },
                                {
                                    "title": "Evidence Preservation",
                                    "description": "Preserving digital evidence involves securing and maintaining the integrity of data to ensure it is admissible in court. It includes proper handling and storage procedures.",
                                },
                                {
                                    "title": "Legal Framework",
                                    "description": "The legal framework for digital evidence includes laws and regulations governing the collection, preservation, and use of digital data in legal proceedings.",
                                },
                                {
                                    "title": "Chain of Custody",
                                    "description": "Chain of custody refers to the documentation and handling of evidence to maintain its integrity and traceability from collection to presentation in court.",
                                },
                                {
                                    "title": "Key Concepts",
                                    "description": "Key concepts include digital forensics principles, evidence preservation techniques, and the legal framework for digital evidence.",
                                },
                                {
                                    "title": "Required Reading",
                                    "description": "Digital Evidence and Computer Crime, 3rd Edition provides comprehensive coverage of digital forensics and its application in criminal investigations.",
                                },
                            ],
                        },
                        "pitfalls": [
                            {
                                "id": "p1",
                                "title": "Chain of Custody Breaks",
                                "description": "Not maintaining proper documentation and handling procedures for digital evidence",
                            },
                            {
                                "id": "p2",
                                "title": "Data Alteration",
                                "description": "Inadvertently modifying digital evidence during the collection process",
                            },
                        ],
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
                            "Examine market reactions to corporate financing decisions",
                        ],
                        "context_materials": {
                            "cards": [
                                {
                                    "title": "Corporate Finance Overview",
                                    "description": "Corporate finance involves managing a company's financial resources to achieve its goals, including investment decisions, capital structuring, and financial risk management.",
                                },
                                {
                                    "title": "Capital Structure Strategy",
                                    "description": "Capital structure strategy involves determining the optimal mix of debt and equity financing to minimize costs and maximize shareholder value.",
                                },
                                {
                                    "title": "Risk Management",
                                    "description": "Risk management in corporate finance involves identifying, assessing, and mitigating financial risks to protect a company's assets and earnings.",
                                },
                                {
                                    "title": "Market Reactions",
                                    "description": "Analyzing market reactions to corporate financing decisions helps understand investor sentiment and the impact on a company's stock price.",
                                },
                                {
                                    "title": "Key Concepts",
                                    "description": "Key concepts include asset-backed securities, capital structure theory, and market signal theory.",
                                },
                                {
                                    "title": "Required Reading",
                                    "description": "Yale SOM Case Study: Hertz Global Holdings (A) provides insights into corporate finance strategies and their implications.",
                                },
                            ],
                        },
                        "pitfalls": [
                            {
                                "id": "p1",
                                "title": "Risk Assessment Oversight",
                                "description": "Underestimating the impact of high leverage on financial stability",
                            },
                            {
                                "id": "p2",
                                "title": "Market Timing Focus",
                                "description": "Overemphasizing market timing instead of fundamental business analysis",
                            },
                        ],
                        "checkpoints": [
                            {
                                "id": "1",
                                "title": "Business Model Analysis",
                                "description": "Evaluate Hertz's core business model and operational scale",
                                "hints": [
                                    "Consider the significance of fleet size and location network",
                                    "Analyze the importance of airport locations in their business model",
                                ],
                            },
                            {
                                "id": "2",
                                "title": "ABS Structure Assessment",
                                "description": "Analyze Hertz's asset-backed securities program and special-purpose entities",
                                "hints": [
                                    "Examine the benefits of bankruptcy-remote trusts",
                                    "Consider how ABS reduces interest costs",
                                ],
                            },
                            {
                                "id": "3",
                                "title": "Risk Management Evaluation",
                                "description": "Assess Hertz's approach to managing fleet depreciation risk",
                                "hints": [
                                    "Compare Program vs Non-Program vehicle strategies",
                                    "Analyze manufacturer repurchase agreements",
                                ],
                            },
                            {
                                "id": "4",
                                "title": "Debt Structure Analysis",
                                "description": "Evaluate Hertz's mix of secured and unsecured debt",
                                "hints": [
                                    "Consider the implications of high leverage",
                                    "Analyze the 2019 debt refinancing decision",
                                ],
                            },
                            {
                                "id": "5",
                                "title": "Strategic Recommendations",
                                "description": "Develop recommendations for Hertz's capital structure",
                                "hints": [
                                    "Consider market reactions to equity issuance",
                                    "Evaluate alternatives to rebalance the capital structure",
                                ],
                            },
                        ],
                        "source_url": "https://cases.som.yale.edu/hertz-global-holdings-uses-debt-and-equity",
                        "source_type": "EXTERNAL",
                        "share_slug": "hertz-capital-structure",
                        "estimated_time": 30,
                    }
                ],
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
                        pitfalls=case_data["pitfalls"],
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
