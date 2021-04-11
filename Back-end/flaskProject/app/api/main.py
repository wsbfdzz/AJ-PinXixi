from flask import Blueprint, jsonify, request, g, render_template
from app.libs.error_code import UrlException, Success
from app.models.base import db
from app.models.good import Good
from app.models.tag import Tag
from app.models.image import Image
from app.models.user import User
from app.libs.token_auth import auth

Good_show = Blueprint('good', __name__)

@Good_show.route('/test')
def test():
    return 'success'

@Good_show.route('/get_detail',methods=['GET'])
def get_information():
    name = request.args.get('name').strip()
    result = []
    good = Good.query.filter_by(name=name).first_or_404()
    good_id = good.id_good
    tag = Tag.query.filter_by(id_good=good_id).all()
    image = Image.query.filter_by(id_good=good_id).all()
    tag_list = []
    image_list = []
    for i in tag:
        tag_list.append(i.tag)
    for i in image:
        image_list.append(i.base64)
    result_dict = {'good_id': good.id_good, 'good_name': good.name, 'good_price': good.price, 'good_count': good.count,
                   'good_rel': good.rel, 'good_info': good.info, 'tag': tag_list, 'image': image_list}
    return jsonify(result_dict)

@Good_show.route('/get_all_goods',methods=['GET'])
def get_all():
    good = Good.query.filter_by(status=1).all()
    result = []
    for i in good:
        tag = Tag.query.filter_by(id_good=i.id_good).all()
        tag_list = []
        for j in tag:
            tag_list.append(j.tag)
        image_list = []
        image = Image.query.filter_by(id_good=i.id_good).all()
        for k in image:
            image_list.append(k.base64)
        result_dict = {'good_id':i.id_good,'good_name':i.name,'good_price':i.price,'good_count':i.count,
                       'good_rel':i.rel,'good_info':i.info,'tag':tag_list,'image':image_list}
        result.append(result_dict)
    return jsonify(result)

@Good_show.route('/upload',methods=['POST'])
def upload():
    name = request.values.get('name')
    price = request.values.get('price').strip()
    count = request.values.get('count').strip()
    rel = request.values.get('rel').strip()
    info = request.values.get('info').strip()
    tag = request.values.get('tag').strip()
    base = request.values.get('base64').strip()

    tag_list = tag.split(',')
    base_list = base.split(',')

    Good.add_good(name,price,count,rel,info)
    number = Good.query.order_by(Good.id_good.desc()).first_or_404().id_good
    for i in tag_list:
        Tag.add_one_record(i,number)
    for i in base_list:
        Image.add_one_record(i,number)
    return Success()


