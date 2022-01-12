from flask_restful import Resource

from models.modern_greek import GreekLemmata, GreekForms


class Lemmata(Resource):

    @classmethod
    def get(cls, lemma):
        lemma_id = GreekLemmata.find_id_by_name(lemma, 0)

        if not lemma_id:
            return {'message': "Lemma Not Found"}, 404

        return lemma_id.json(), 200
