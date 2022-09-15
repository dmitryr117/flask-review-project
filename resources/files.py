from flask_jwt_extended import jwt_required
from flask_restful import Resource, Api, reqparse
import werkzeug

class UploadImage(Resource):
  @jwt_required()
  def get(self):
    return {'hello': 'world'}

  @jwt_required()
  def post(self):
    parse = reqparse.RequestParser()
    parse.add_argument('File', type=werkzeug.datastructures.FileStorage, location='files')
    args = parse.parse_args()
    image_file = args['File']
    image_file.save("images/your_file_name.png")




