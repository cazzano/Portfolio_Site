from App import PortfolioApp

if __name__ == '__main__':
    portfolio_app = PortfolioApp()
    portfolio_app.app.run_server(debug=True)
