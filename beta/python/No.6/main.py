from flask import Flask
from App import PortfolioApp  # Import your Dash app

# Create a Flask server
server = Flask(__name__)

# Create an instance of your Dash app
# Modify your PortfolioApp __init__ to accept server
portfolio_app = PortfolioApp(server)

# Expose the Dash app's server
application = portfolio_app.app.server  # Use .server for WSGI compatibility

if __name__ == '__main__':
    # Run the Flask server in debug mode for local development
    server.run(debug=True, host='0.0.0.0', port=8050)
