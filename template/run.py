import os

from {{ app_name }} import app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', app.config['PORT']))
    app.run(debug=app.debug, host=app.config['HOST'], port=port)
