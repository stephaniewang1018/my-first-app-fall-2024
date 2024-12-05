# this is the "web_app/__init__.py" file...


#import os 
#from flask import Flask
#
#from web_app.routes.home_routes import home_routes
#from web_app.routes.stocks_routes import stocks_routes
#from web_app.routes.unemployment_routes import unemployment_routes
#
#SECRET_KEY = os.getenv("SECRET_KEY", default="super secret") # set this to something else on production!!!
#
#def create_app():
#    app = Flask(__name__)
#
#    app.config["SECRET_KEY"] = SECRET_KEY
#
#    app.register_blueprint(home_routes)
#    app.register_blueprint(stocks_routes)
#    app.register_blueprint(unemployment_routes)
#
#from flask import Flask
#
#from web_app.routes.home_routes import home_routes
##from web_app.routes.stocks_routes import stocks_routes
#
#def create_app():
#    app = Flask(__name__)
#    app.register_blueprint(home_routes)
#    #app.register_blueprint(stocks_routes)
# main
#    return app
#
#if __name__ == "__main__":
#    my_app = create_app()
#    my_app.run(debug=True)

import os 
from flask import Flask

from web_app.routes.home_routes import home_routes
from web_app.routes.stocks_routes import stocks_routes
from web_app.routes.unemployment_routes import unemployment_routes
from web_app.routes.product_routes import product_routes


# Security best practice: Set a unique key for production environments
SECRET_KEY = os.getenv("SECRET_KEY", default="super secret")  # Update this for production!

def create_app():
    app = Flask(__name__)

    # Configure the application
    app.config["SECRET_KEY"] = SECRET_KEY

    # Register blueprints
    app.register_blueprint(home_routes)
    app.register_blueprint(stocks_routes)
    app.register_blueprint(unemployment_routes)
    app.register_blueprint(product_routes)

    return app

# Run the application
if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
