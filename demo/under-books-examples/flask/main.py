from flask import Flask
app = Flask(__name__)


@app.route('/')  # 或者 app.add_url_rule('/', 'hello', hello_world)
def hello_world():
   return 'Hello World'

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

@app.route('/blog/<int:postID>')    # int
def show_blog(postID):
   return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>') # float
def revision(revNo):
   return 'Revision Number %f' % revNo

if __name__ == '__main__':
   app.run()    # app.run(host, port, debug, options)