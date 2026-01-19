from flask import Blueprint, jsonify
from flasgger import swag_from
from models.drafts import Draft
from schemas.drafts import DraftSchema
from models import db

drafts_bp = Blueprint('drafts_bp', __name__)