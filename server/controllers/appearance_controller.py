from flask import Blueprint, request, jsonify
from server.app import db
from server.models.appearance import Appearance
from flask_jwt_extended import jwt_required

appearance_bp = Blueprint('appearances', __name__, url_prefix='/appearances')

@appearance_bp.route('', methods=['POST'])
@jwt_required()
def create_appearance():
    d = request.get_json()
    a = Appearance(rating=d['rating'], guest_id=d['guest_id'], episode_id=d['episode_id'])
    db.session.add(a)
    db.session.commit()
    return jsonify({"id": a.id, "rating": a.rating}), 201
