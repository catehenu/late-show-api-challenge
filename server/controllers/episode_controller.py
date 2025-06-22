from flask import Blueprint, jsonify
from server.app import db
from server.models.episode import Episode
from flask_jwt_extended import jwt_required

episode_bp = Blueprint('episodes', __name__, url_prefix='/episodes')

@episode_bp.route('', methods=['GET'])
def list_episodes():
    eps = Episode.query.all()
    return jsonify([{"id":e.id, "date":e.date.isoformat(), "number":e.number} for e in eps]), 200

@episode_bp.route('/<int:id>', methods=['GET'])
def get_episode(id):
    e = Episode.query.get_or_404(id)
    appearances = [
        {"id": a.id, "rating": a.rating, "guest": {"id": a.guest.id, "name": a.guest.name}}
        for a in e.appearances
    ]
    return jsonify({"id": e.id, "date": e.date.isoformat(), "number": e.number, "appearances": appearances})

@episode_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    e = Episode.query.get_or_404(id)
    db.session.delete(e)
    db.session.commit()
    return jsonify({"msg": "Deleted"}), 200
