from flask import Flask, jsonify


def create_app(test_config=None):
    app = Flask(__name__)

    @app.route('/api/v1/nft/<int:nft_id>/water-level', methods=['GET'])
    def get_water_level(nft_id: int):
        return jsonify({
            "type": "water-level",
            "timestamp": "2021-10-30 12:44:02.3",
            "value": "normal",
            "nft": nft_id,
        })
    return app
