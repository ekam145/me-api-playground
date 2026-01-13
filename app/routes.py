from flask import send_from_directory
import os
from flask import Blueprint, jsonify, request
from app.models import Project, Skill

routes = Blueprint("routes", __name__)

@routes.route("/health")
def health():
    return {"status": "ok"}, 200


@routes.route("/projects")
def get_projects():
    skill = request.args.get("skill")

    if skill:
        projects = (
            Project.query
            .join(Project.skills)
            .filter(Skill.name.ilike(skill))
            .all()
        )
    else:
        projects = Project.query.all()

    return jsonify([
        {
            "id": p.id,
            "title": p.title,
            "description": p.description,
            "links": p.links,
            "skills": [s.name for s in p.skills]
        }
        for p in projects
    ])

@routes.route("/")
def frontend():
    return send_from_directory(
        os.path.join(os.getcwd(), "frontend"),
        "index.html"
    )
