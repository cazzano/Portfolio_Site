import dash
from dash import html, dcc
from dash.dependencies import Input, Output

class PortfolioApp:
    def __init__(self):
        self.app = dash.Dash(__name__,
                              external_stylesheets=[
                                  "https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css",
                                  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css"
                              ],
                              meta_tags=[
                                  {"name": "viewport",
                                   "content": "width=device-width, initial-scale=1"}
                              ])

        self.app.title = "Colorful Creative Portfolio"
        self.app.layout = self.create_layout()
        self.register_callbacks()

    def create_layout(self):
        return html.Div([
            # Colorful Navigation
            html.Nav([
                html.Div([
                    # Circular Logo with Red, Yellow, Blue Gradient
                    html.Div([
                        html.Span("AR", className="text-3xl font-bold text-white")
                    ], className="w-16 h-16 rounded-full bg-gradient-to-br from-red-500 via-yellow-400 to-blue-500 flex items-center justify-center"),

                    # Navigation Links with Colorful Hover Effects and Icons
                    html.Div([
                        html.A([html.I(className="fas fa-home mr-2"), "Home"], href="/", className="nav-link text-red-600 hover:text-blue-500"),
                        html.A([html.I(className="fas fa-project-diagram mr-2"), "Projects"], href="/projects", className="nav-link text-yellow-600 hover:text-red-500"),
                        html.A([html.I(className="fas fa-code mr-2"), "Skills"], href="/skills", className="nav-link text-blue-600 hover:text-yellow-500"),
                        html.A([html.I(className="fas fa-envelope mr-2"), "Contact"], href="/contact", className="nav-link text-red-500 hover:text-blue-600")
                    ], className="flex space-x-6")
                ], className="container mx-auto flex justify-between items-center p-4")
            ], className="fixed top-0 left-0 right-0 bg-white shadow-md z-50"),

            # Main Content Area with Colorful Background
            html.Div([
                html.Div(id='page-content', className='pt-20')
            ], className="min-h-screen bg-gradient-to-br from-red-50 via-yellow-50 to-blue-50"),

            # Floating Colorful Social Links
            html.Div([
                html.A(html.I(className="fab fa-github text-red-600 hover:text-blue-500"), href="#", className="social-icon"),
                html.A(html.I(className="fab fa-linkedin text-yellow-600 hover:text-red-500"), href="#", className="social-icon"),
                html.A(html.I(className="fab fa-twitter text-blue-600 hover:text-yellow-500"), href="#", className="social-icon")
            ], className="fixed bottom-8 right-8 flex space-x-4"),

            # Location for routing
            dcc.Location(id='url', refresh=False)
        ], className="relative")

    def register_callbacks(self):
        @self.app.callback(
            Output('page-content', 'children'),
            [Input('url', 'pathname')]
        )
        def display_page(pathname):
            if pathname == "/" or pathname == "/home":
                return self.home_page()
            elif pathname == "/projects":
                return self.projects_page()
            elif pathname == "/skills":
                return self.skills_page()
            elif pathname == "/contact":
                return self.contact_page()
            return self.home_page()

    def home_page(self):
        return html.Div([
            html.Div([
                html.Div([
                    # Colorful Heading with Icon
                    html.H1([
                        html.I(className="fas fa-user-astronaut mr-4 text-transparent bg-clip-text bg-gradient-to-r from-red-500 via-yellow-400 to-blue-500"),
                        "Alex Rodriguez"
                    ], className="text-6xl font-bold mb-4 text-transparent bg-clip-text bg-gradient-to-r from-red-500 via-yellow-400 to-blue-500"),

                    # Subtitle with Colorful Touch
                    html.P([
                        html.I(className="fas fa-laptop-code mr-2 text-red-500"),
                        "Creative Developer | Innovator | Designer"
                    ], className="text-xl text-gray-700 mb-8"),

                    # Call to Action Buttons with Colorful Design and Icons
                    html.Div([
                        html.A([
                            html.I(className="fas fa-eye mr-2"),
                            "View Projects"
                        ], href="/projects",
                               className="px-8 py-3 bg-red-500 text-white rounded-full hover:bg-blue-500 transition duration-300 mr-4"),
                        html.A([
                            html.I(className="fas fa-paper-plane mr-2"),
                            "Contact Me"
                        ], href="/contact",
                               className="px-8 py-3 border-2 border-yellow-500 text-yellow-500 rounded-full hover:bg-yellow-500 hover:text-white transition duration-300")
                    ], className="flex items-center")
                ], className="text-center max-w-2xl mx-auto")
            ], className="container mx-auto px-4 py-20 flex items-center justify-center h-screen")
        ], className="bg-gradient-to-br from-red-50 via-yellow-50 to-blue-50")

    def projects_page(self):
        projects = [
            {
                "name": "AI Visualization Engine",
                "description": "Advanced data visualization with machine learning",
                "technologies": ["Python", "TensorFlow", "D3.js"],
                "icon": "fas fa-chart-pie",
                "color": "from-red-500 to-yellow-400"
            },
            {
                "name": "Interactive Dashboard",
                "description": "Real-time data storytelling platform",
                "technologies": ["Dash", "Plotly", "React"],
                "icon": "fas fa-chart-line",
                "color": "from-blue-500 to-red-400"
            }
        ]

        return html.Div([
            html.Div([
                html.H2([
                    html.I(className="fas fa-project-diagram mr-4 text-transparent bg-clip-text bg-gradient-to-r from-red-500 via-yellow-400 to-blue-500"),
                    "Creative Projects"
                ], className="text-4xl font-bold text-center mb-12 text-transparent bg-clip-text bg-gradient-to-r from-red-500 via-yellow-400 to-blue-500"),
                html.Div([
                    html.Div([
                        html.Div([
                            html.I(className=f"{project['icon']} text-4xl mb-4",
                                   style={"background": f"linear-gradient(to right, {project['color']})",
                                          "-webkit-background-clip": "text",
                                          "-webkit-text-fill-color": "transparent"}),
                            html.H3(project["name"],
                                    className="text-2xl font-semibold mb-4 text-gray-800"),
                            html .P(project["description"],
                                   className="text-gray-600 mb-4"),
                            html.Div([
                                html.Span(tech,
                                          className="bg-red-100 text-red-600 px-3 py-1 rounded-full mr-2 text-sm")
                                for tech in project["technologies"]
                            ])
                        ], className="p-8 bg-white rounded-lg shadow-lg transform hover:scale-105 transition duration-300")
                    ], className="mb-8") for project in projects
                ])
            ], className="container mx-auto px-4 py-20")
        ], className="bg-gradient-to-br from-red-50 via-yellow-50 to-blue-50")

    def skills_page(self):
        skills = {
            "Programming": ["Python", "JavaScript", "Rust"],
            "Design": ["UI/UX", "Data Visualization", "Creative Coding"],
            "Tools": ["Dash", "React", "Machine Learning"]
        }

        return html.Div([
            html.Div([
                html.H2([
                    html.I(className="fas fa-tools mr-4 text-transparent bg-clip-text bg-gradient-to-r from-red-500 via-yellow-400 to-blue-500"),
                    "My Skill Set"
                ], className="text-4xl font-bold text-center mb-12 text-transparent bg-clip-text bg-gradient-to-r from-red-500 via-yellow-400 to-blue-500"),
                html.Div([
                    html.Div([
                        html.H3(category,
                                className="text-2xl font-semibold mb-6 text-gray-800"),
                        html.Div([
                            html.Span(skill,
                                      className="bg-gradient-to-r from-red-500 to-yellow-400 text-white px-4 py-2 rounded-full mr-2 mb-2 inline-block")
                            for skill in skill_list
                        ])
                    ], className="bg-white p-8 rounded-lg shadow-lg")
                    for category, skill_list in skills.items()
                ], className="grid md:grid-cols-3 gap-8")
            ], className="container mx-auto px-4 py-20")
        ], className="bg-gradient-to-br from-red-50 via-yellow-50 to-blue-50")

    def contact_page(self):
        return html.Div([
            html.Div([
                html.H2([
                    html.I(className="fas fa-envelope-open-text mr-4 text-transparent bg-clip-text bg-gradient-to-r from-red-500 via-yellow-400 to-blue-500"),
                    "Get in Touch"
                ], className="text-4xl font-bold text-center mb-12 text-transparent bg-clip-text bg-gradient-to-r from-red-500 via-yellow-400 to-blue-500"),
                html.Div([
                    html.Form([
                        html.Div([
                            dcc.Input(id='name', type='text', placeholder='Your Name',
                            className='border border-gray-300 p-2 rounded w-full mb-4')
                        ]),
                        dcc.Input(
                            id='email', type='email', placeholder='Your Email',
                            className='border border-gray-300 p-2 rounded w-full mb-4'
                        ),
                        dcc.Textarea(
                            id='message', placeholder='Your Message',
                            className='border border-gray-300 p-2 rounded w-full mb-4',
                            rows=5
                        ),
                        html.Button([
                            html.I(className="fas fa-paper-plane mr-2"),
                            'Send Message'
                        ], className='bg-gradient-to-r from-red-500 to-yellow-500 text-white px-4 py-2 rounded hover:bg-blue-500 transition duration-300')
                    ], className='flex flex-col max-w-md mx-auto')
                ])
            ], className='container mx-auto px-4 py-20')
        ], className='bg-gradient-to-br from-red-50 via-yellow-50 to-blue-50')

    def run(self):
        self.app.run_server(debug=True)

if __name__ == "__main__":
    portfolio_app = PortfolioApp()
    portfolio_app.run()
