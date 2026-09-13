from flask import Flask, jsonify, render_template_string
import os
from datetime import datetime

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Auto Deploy App</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            color: white;
        }
        .container {
            text-align: center;
            padding: 60px 40px;
            background: rgba(255,255,255,0.1);
            border-radius: 24px;
            backdrop-filter: blur(20px);
            box-shadow: 0 25px 45px rgba(0,0,0,0.2);
            max-width: 500px;
        }
        h1 { font-size: 3.5em; margin-bottom: 10px; }
        .subtitle { font-size: 1.3em; opacity: 0.9; margin-bottom: 30px; }
        .badge {
            display: inline-block;
            background: #4CAF50;
            padding: 12px 24px;
            border-radius: 30px;
            font-weight: bold;
            font-size: 1.1em;
            margin: 20px 0;
        }
        .info {
            margin-top: 30px;
            padding-top: 30px;
            border-top: 1px solid rgba(255,255,255,0.2);
            font-size: 0.95em;
            opacity: 0.8;
        }
        .timestamp { font-family: monospace; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀</h1>
        <h1>Привет!</h1>
        <p class="subtitle">Приложение успешно задеплоено</p>
        <div class="badge">✅ Работает отлично</div>
        <div class="info">
            <p>⏰ Запущено: <span class="timestamp">{{ time }}</span></p>
            <p>🌐 Порт: {{ port }}</p>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(
        HTML,
        time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        port=os.environ.get('PORT', 5000)
    )

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})

@app.route('/api/status')
def status():
    return jsonify({
        'app': 'auto-deploy-app',
        'version': '1.0.0',
        'timestamp': datetime.now().isoformat(),
        'environment': os.environ.get('RAILWAY_ENVIRONMENT', 'development')
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
