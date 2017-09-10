from main import app
from controller import user_role
from conf.config import listen_port
from main import api
api.add_resource(user_role.Userinfo,'/getpage/')
app.run(debug = True, host ="192.168.0.73", port =5001, threaded = True)
