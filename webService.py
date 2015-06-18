#!flask/bin/python
from flask import Flask, jsonify, request
#from administradorConsultas import AdministradorConsultas
from red import xmls_to_red

DIRECTORIO_PROYECTO = '/home/vigtech/shared/repository/'

app = Flask(__name__)


@app.route('/red/', methods=['GET'])
def get_red():
	proyecto = request.args.get('proyecto')
	user = request.args.get('user')
	red = xmls_to_red([open(DIRECTORIO_PROYECTO+'%s.%s/busqueda0.xml'%(user,proyecto))], 'RedCoauth')
	cc=  red.clustering_coefficient()
	ad = red.average_degree()
	avs = red.average_strength()
	apl= red.average_path_lenght()
    
	nodos, aristas = red.generar_json()
	return jsonify({'nodes':nodos, 'links':aristas, 'averagePathLenght':apl, 'clusteringCoefficient':cc, 'averageDegree':ad})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
