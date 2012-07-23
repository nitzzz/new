import flask, flask.views
import fbconsole
app = flask.Flask(__name__)
# Don't do this!
app.secret_key = "nitish"
fbconsole.AUTH_SCOPE = ['publish_stream', 'publish_checkins']
fbconsole.APP_ID = '266828850095076'
fbconsole.authenticate()
class View(flask.views.MethodView):
    def get(self):
        return flask.render_template('index.html')
        
    def post(self):
        result = flask.request.form['expression']
	status = fbconsole.post('/me/feed', {'message':result})
	likes = fbconsole.get('/'+status['id']+'/likes')
        flask.flash(result)
        fbconsole.logout()
        return self.get()
    
app.add_url_rule('/', view_func=View.as_view('main'), methods=['GET', 'POST'])

app.debug = True
app.run()
