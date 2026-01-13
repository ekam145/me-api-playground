from app.db import  db
from app.models import Profile, Skill, Project, Links

def seed_if_empty():
    # If profile exists, assume DB is already seeded
    if Profile.query.first():
        return


    # Profile
    profile = Profile(
        name="Ekamjot Singh",
        email="ejot145@gmail.com",
        education="B.Tech (CSE)"
    )

    # Skills
    python = Skill(name="python")
    flask = Skill(name="flask")
    sql = Skill(name="sql")

    # Project
    project = Project(
        title="Me API Playground",
        description="Personal profile API using Flask and SQLite",
        links="https://github.com/ekam145/me-api-playground"
    )
    project.skills.extend([python, flask, sql])

    # Links
    links = Links(
        github="https://github.com/ekam145",
        linkedin="https://www.linkedin.com/in/ekamjot-singh-a5b0b92b5",
        portfolio="https://drive.google.com/file/d/1mkta3i8moXtPMMxNg1gK26d3Ow1S5ZEf/view?usp=drivesdk"
    )

    db.session.add_all([
        profile,
        python, flask, sql,
        project,
        links
    ])
    db.session.commit()
