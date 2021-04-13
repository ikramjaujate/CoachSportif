from flask import Flask, request, jsonify, redirect, url_for, Blueprint
import model as models
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager, create_refresh_token
import app as app

encodage = Blueprint('encodage', __name__)


@encodage.route('', methods=['POST'])
def post_encodage():
    if request.method == 'POST':
        info = request.get_json(force=True)
        print(info)

        user_encodage = models.Encodage(info["id_user"], info["id_activite"], info["id_encodage"], info["date"], info["heure"],
                                        info["distance"], info["duree"], info["vitesse_moyenne"])
        app.db.session.add(user_encodage)
        app.db.session.commit()

        return redirect('http://localhost:5000/')
