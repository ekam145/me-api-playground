from .db import db

project_skills = db.Table(
    "project_skills",
    db.Column("project_id", db.Integer, db.ForeignKey("project.id")),
    db.Column("skill_id", db.Integer, db.ForeignKey("skill.id"))
)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    education = db.Column(db.String)

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    links = db.Column(db.String)

    skills = db.relationship(
        "Skill",
        secondary=project_skills,
        backref="projects"
    )

class Links(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    github = db.Column(db.String)
    linkedin = db.Column(db.String)
    portfolio = db.Column(db.String)
