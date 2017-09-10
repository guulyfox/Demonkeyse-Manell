from main import app
from conf.config import listen_port
app.run(debug=True,host = '0.0.0.0', port = listen_port, threaded = True)
