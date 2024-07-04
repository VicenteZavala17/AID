import subprocess
from flask import Flask, jsonify, render_template, request, redirect, send_file

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejecutar-playbook', methods=['POST'])
def ejecutar_playbook():
    data = request.get_json()
    opcion = data.get('opcion')

    if opcion == '1':
        playbook_path = '/app/playbook.yml'
        try:
            resultado = subprocess.run(['ansible-playbook', playbook_path], capture_output=True, text=True)
            output = resultado.stdout
            return jsonify({'status': 'success', 'output': output,'message': output}), 200
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)}), 500

    elif opcion == '2':
        try:
            youtube_link = 'https://www.youtube.com/watch?v=fxXg6_UvBR8&ab_channel=elPato'
            return jsonify({'status': 'success', 'youtube_link': youtube_link,'message': 'Navegando Carnal pulpo'}), 200
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)}), 500

    elif opcion == '3':
        try:
            playbook_path = '/app/playbook.yml'
            return jsonify({'status': 'success', 'playbook_path': playbook_path,'message': 'Descargando playbook actual.'}), 200
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)}), 500

    else:
        return jsonify({'status': 'error', 'message': 'Opción no válida'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
