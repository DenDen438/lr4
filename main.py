from flask import Flask, Blueprint
from flask_restplus import Api, Resource
app = Flask(__name__)
api = Api(app = app)
# описание главного блока нашего api http://127.0.0.1:5000/main/.
name_space = api.namespace('main', description='Main APIs')
from flask_restplus import fields
# определение модели данных массива
list_ = api.model('list', {
 'id': fields.Integer(required=True, description='id'),
 'country': fields.String(required=True, description='holiday country'),
 'client': fields.String(required=True, description='client name'),
 'cost': fields.Integer(required=True, description='the cost of travel '),
 'place': fields.Integer(required=True, description='number of seats '),
 'array': fields.List(fields.Raw,required=True, description='all list')
})
# массив, который хранится в оперативной памяти
ls=[{"id": 0, "country":"Italy ", "client":"Egor", "cost":13000,"place":30}]
universalID=int(0)
allarray = ls
name_space1 = api.namespace('list', description='list APIs')
@name_space1.route("/")
class ListClass(Resource):
 @name_space1.doc("")
 @name_space1.marshal_with(list_)
 def get(self):
 """Получение всего массива"""
 return { 'array': ls}
 @name_space1.doc("")
 # ожидаем на входе данных в соответствии с моделью list
 @name_space1.expect(list_)
 # маршалинг данных в соответствии с list_
 @name_space1.marshal_with(list_)
 def post(self):
 """Создание массива"""
 global allarray
 # получить переданный массив из тела запроса
 cntr={"id":api.payload['id'], "country": api.payload['country'], "client":
api.payload['client'], "cost": api.payload['cost'],"place": api.payload['place'] }
 ls.append(cntr)
 # возвратить новый созданный массив клиенту
 return { 'array': ls}
# модель данные с двумя параметрами строкового типа
sortsc = api.model('lst', { 'array':fields.List(fields.Raw,required=True,
description='all list')})
# url 127.0.0.1/list/mimmax
@name_space1.route("/getsortid")
class getsortId(Resource):
 @name_space1.doc("")
 # маршаллинг данных в соответствии с моделью minmax
 @name_space1.marshal_with(sortsc)
 def get(self):
 """сортировка по id"""
 global ls
 ide=sorted(ls,key=lambda cntr: cntr['id'])
 return {'array': ide}
@name_space1.route("/getsortCountry")
class getsortCountry(Resource):
 @name_space1.doc("")
 # маршаллинг данных в соответствии с моделью minmax
 @name_space1.marshal_with(sortsc)
 def get(self):
 """сортировка по стране"""
 global ls
 cntry=sorted(ls,key=lambda cntr: cntr['country'])
 return {'array': cntry}
@name_space1.route("/getsortClient")
class getsortClient(Resource):
 @name_space1.doc("")
 # маршаллинг данных в соответствии с моделью minmax
 @name_space1.marshal_with(sortsc)
 def get(self):
  """сортировка по имени"""
  global ls
  name=sorted(ls,key=lambda cntr: cntr['client'])
  return {'array': name}
@name_space1.route("/getsortCost")
class getsortCost(Resource):
 @name_space1.doc("")
 # маршаллинг данных в соответствии с моделью minmax
 @name_space1.marshal_with(sortsc)
 def get(self):
 """сортировка по цене"""
 global ls
 cst=sorted(ls,key=lambda cntr: cntr['cost'])
 return {'array': cst}
@name_space1.route("/getsortPlace")
class getsortPlace(Resource):
 @name_space1.doc("")
 # маршаллинг данных в соответствии с моделью minmax
 @name_space1.marshal_with(sortsc)
 def get(self):
 """сортировка по местам"""
 global ls
 pls=sorted(ls,key=lambda cntr: cntr['place'])
 return {'array': pls}
@name_space1.route("/delmaxMaxcost")
class delmaxMaxcost(Resource):
 @name_space1.doc("")
 # маршаллинг данных в соответствии с моделью minmax
 @name_space1.marshal_with(sortsc)
 def delete(self):
 """Удаление удаление самой дорогой поездки"""
 global ls
 mx=max([cntr['cost'] for cntr in ls ])
 ls=[cntr for cntr in ls if cntr['cost']!=mx]
 return {'array': ls}
maxznc=api.model('one', {'val':fields.String}, required=True, description='one
values')
@name_space1.route("/getmaxCost")
class getmaxCost(Resource):
 @name_space1.doc("")
 global ls
 srd=sum([cntr['cost'] for cntr in ls ])/len(ls)
 return {'val': srd}
@name_space1.route("/getsredPlace")
class getsredPlace(Resource):
 @name_space1.doc("")
 # маршаллинг данных в соответствии с моделью minmax
 @name_space1.marshal_with(maxznc)
 def get(self):
 """Получение среднего по местам"""
 global ls
 srd=sum([cntr['place'] for cntr in ls ])/len(ls)
 return {'val': srd}
@name_space1.route("/autoChangePrice")
class autoChangePrice(Resource):
 @name_space1.doc("")
 # маршаллинг данных в соответствии с моделью minmax
 @name_space1.marshal_with(list_)
 def patch(self):
 """Изменение цены на 10%"""
 global ls
 srdWeight=sum([cntr['cost'] for cntr in ls ])/len(ls)
 for cntr in ls:
 if(cntr["cost"] > srdWeight):
 cntr['cost'] = cntr['cost'] * 0.9
 return ls
api.add_namespace(name_space1)
from flask_restplus import reqparse
from random import random
reqp = reqparse.RequestParser()
reqp.add_argument('id', type=int, required=False)
@name_space1.route("/izmdfilm")
class IzmfilClass(Resource):
 @name_space1.doc("")
 # маршаллинг данных в соответствии с моделью minmax
 @name_space1.expect(reqp)
 @name_space1.marshal_with(list_)
 def get(self):
 """удаление записи ид"""
 global ls
 args = reqp.parse_args()
 ls=[cntr for cntr in ls if cntr['id']!=args['id']]
 return { 'array': ls}
@name_space1.doc("")
# ожидаем на входе данных в соответствии с моделью list_
@name_space1.expect(list_)
# маршалинг данных в соответствии с list_
@name_space1.marshal_with(list_)
def put(self):
"""Изменение записи по ид"""
global ls
for cntr in ls:
if(api.payload['id'] == cntr["id"]):
cntr["country"] = api.payload['country']
cntr["client"] = api.payload['client']
cntr["cost"] = api.payload['cost']
cntr["place"] = api.payload['place']
return { 'array': ls}
cntr={"id":api.payload['id'], "country": api.payload['country'], "client":
api.payload['client'], "cost": api.payload['cost'], "place": api.payload['place'] }
ls.append(cntr)
return ls
app.run(debug=True)
