import subprocess
import webbrowser
from flask import Flask, jsonify, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejecutar-playbook', methods=['POST'])
def ejecutar_playbook():
    data = request.get_json()
    opcion = data.get('opcion')

    if opcion == '1':
        try:
            # Ruta al video local en tu sistema Windows
            video_path = r'C:\Users\Jeffy\Desktop\Product2.mp4'
            
            # Comando para abrir el video en Windows
            subprocess.Popen(['start', '', video_path], shell=True)
            
            return jsonify({'status': 'success', 'message': 'Video abierto correctamente'}), 200
        except Exception as e:
            return jsonify({'status': 'error 1', 'message': str(e)}), 500

    elif opcion == '2':
        try:
            # Abrir un enlace de YouTube
            youtube_link = 'https://www.youtube.com/watch?v=fxXg6_UvBR8&ab_channel=elPato'  # Reemplaza con tu enlace de YouTube
            webbrowser.open(youtube_link)
            return jsonify({'status': 'success', 'message': 'Enlace de YouTube abierto correctamente'}), 200
        except Exception as e:
            return jsonify({'status': 'error 2', 'message': str(e)}), 500

    elif opcion == '3':
        # Simular la ejecución de un playbook (simplemente devuelve un mensaje)
        return jsonify({'status': 'success', 'message': 'Simulación de ejecución de playbook'}), 200
    
    else:
        return jsonify({'status': 'error 3', 'message': 'Opción no válida'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')




# import subprocess
# from flask import Flask, jsonify, render_template, request
# import os

# app = Flask(__name__, template_folder='templates')

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/ejecutar-playbook', methods=['POST'])
# def ejecutar_playbook():
#     opcion = request.form.get('opcion')
#     playbook_path = '/app/playbook.yml'
    
#     if opcion == '1':
#         # Acción para obtener el playbook (ejemplo)
#         try:
#             with open(playbook_path, 'r') as f:
#                 playbook_content = f.read()
#             return jsonify({'status': 'success', 'output': playbook_content}), 200
#         except Exception as e:
#             return jsonify({'status': 'error', 'message': str(e)}), 500
    
#     elif opcion == '2':
#         # Acción para obtener la configuración de Ansible (ejemplo)
#         try:
#             ansible_config = "Aquí va la configuración de Ansible"
#             return jsonify({'status': 'success', 'output': ansible_config}), 200
#         except Exception as e:
#             return jsonify({'status': 'error', 'message': str(e)}), 500
    
#     elif opcion == '3':
#         # Acción para ejecutar el playbook con Ansible
#         try:
#             resultado = subprocess.run(['ansible-playbook', playbook_path], capture_output=True, text=True)
#             output = resultado.stdout
#             return jsonify({'status': 'success', 'output': output}), 200
#         except Exception as e:
#             return jsonify({'status': 'error', 'message': str(e)}), 500
    
#     else:
#         return jsonify({'status': 'error', 'message': 'Opción no válida'}), 400

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')



# import subprocess
# from flask import Flask, jsonify, render_template
# import os

# app = Flask(__name__, template_folder='templates')

# @app.route('/')
# def index():
#     app.logger.info(app.template_folder)
#     return render_template('index.html')

# @app.route('/ejecutar-playbook', methods=['POST'])
# def ejecutar_playbook():
#     playbook_path = '/app/playbook.yml'
#     try:
#         resultado = subprocess.run(['ansible-playbook', playbook_path], capture_output=True, text=True)
#         output = resultado.stdout
#         return jsonify({'status': 'success', 'output': output}), 200
#     except Exception as e:
#         return jsonify({'status': 'error', 'message': str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0')
