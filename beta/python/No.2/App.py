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

        self.app.title = "Developer Portfolio"
        self.app.layout = self.create_layout()
        self.register_callbacks()

    def create_layout(self):
        return html.Div([
            # Sidebar Navigation
            html.Div([
                # Profile Section
                html.Div([
                    html.Img(src="/assets/profile.png", className="rounded-full w-24 h-24 mx-auto mb-4"),
                    html.H2("Alex Rodriguez", className="text-xl font-bold text-center text-white"),
                    html.P("Full Stack Developer", className="text-sm text-center text-gray-400")
                ], className="mb-8"),

                # Navigation Links
                html.Nav([
                    html.Ul([
                        html.Li(html.A([
                            html.I(className="fas fa-home mr-3"),
                            "Home"
                        ], href="/", className="nav-link")),
                        html.Li(html.A([
                            html.I(className="fas fa-project-diagram mr-3"),
                            "Projects"
                        ], href="/projects", className="nav-link")),
                        html.Li(html.A([
                            html.I(className="fas fa-code mr-3"),
                            "Skills"
                        ], href="/skills", className="nav-link")),
                        html.Li(html.A([
                            html.I(className="fas fa-envelope mr-3"),
                            "Contact"
                        ], href="/contact", className="nav-link"))
                    ])
                ]),

                # Social Links
                html.Div([
                    html.A(html.I(className="fab fa-github"), href="#", className="social-icon"),
                    html.A(html.I(className="fab fa-linkedin"), href="#", className="social-icon"),
                    html.A(html.I(className="fab fa-twitter"), href="#", className="social-icon")
                ], className="flex justify-center mt-8")
            ], className="fixed left-0 top-0 h-full w-64 bg-gray-900 p-6 text-white"),

            # Main Content Area
            html.Div([
                # Content will be dynamically loaded here
                html.Div(id='page-content', className='p-8')
            ], className="ml-64 bg-gray-100 min-h-screen"),

            # Location for routing
            dcc.Location(id='url', refresh=False)
        ], className="flex")

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
            html.H1("Welcome to My Digital Space", className="text-4xl font-bold mb-6 text-gray-800"),
            html.Div([
                html.P("I craft elegant solutions through code, transforming complex problems into simple, efficient applications.",
                       className="text-xl text-gray-600 mb-6"),
                html.A("View My Work", href="/projects",
                       className="px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition duration-300")
            ])
        ])

    def projects_page(self):
        projects = [
            {
                "name": "AI Recommendation Engine",
                "description": "Machine learning system for personalized recommendations",
                "technologies": ["Python", "TensorFlow", "scikit-learn"],
                "icon": "fas fa-robot"
            },
            {
                "name": "Real-time Dashboard",
                "description": "Interactive data visualization platform",
                "technologies": ["Dash", "Plotly", "React"],
                "icon": "fas fa-chart-line"
            }
        ]

        return html.Div([
            html.H2("Featured Projects", className="text-3xl font-bold mb-6 text-gray-800"),
            html.Div([
                html.Div([
                    html.Div([
                        html.I(className=f"{project['icon']} text-4xl mb-4 text-blue-600"),
                        html.H3(project["name"], className="text-xl font-semibold mb-2"),
                        html.P(project["description"], className="text-gray-600 mb-4"),
                        html.Div([
                            html.Span(tech, className="bg-gray-200 px-2 py-1 rounded mr-2 text-sm")
                            for tech in project["technologies"]
                        ])
                    ], className="p-6 bg-white rounded-lg shadow-md hover:shadow-xl transition duration-300")
                    for project in projects
                ], className="grid grid-cols-2 gap-6")
            ])
        ])

    def skills_page(self):
        skills = {
            "Languages": ["Python", "JavaScript", "Java"],
            "Frameworks": ["Dash", "React", "Django"],
            "Tools": ["Git", "Docker", "Kubernetes"]
        }

        return html.Div([
            html.H2("Technical Skills", className="text-3xl font-bold mb-6 text-gray-800"),
            html.Div([
                html.Div([
                    html.H3(category, className="text-xl font-semibold mb-4"),
                    html.Div([
                        html.Span(skill, className="bg-blue-100 text-blue-800 px-3 py-1 rounded-full mr-2 mb-2 inline-block")
                        for skill in skill_list
                    ])
                ], className="bg-white p-6 rounded-lg shadow-md")
                for category, skill_list in skills.items()
            ], className="grid grid-cols-3 gap-6")
        ])

    def contact_page(self):
        return html.Div([
            html.H2("Get in Touch", className="text-3xl font-bold mb-6 text-gray-800"),
            html.Form([
                html.Div([
                    dcc.Input(
                        type="text",
                        placeholder="Your Name",
                        className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:border-blue-500"
                    )
                ], className="mb-4"),
                html.Div([
                    dcc.Input(
                        type="email",
                        placeholder="Your Email",
                        className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:border-blue-500"
                    )
                ], className="mb-4"),
                html.Div([
                    dcc.Textarea( placeholder="Your Message",
                        className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:border-blue-500"
                    )
                ], className="mb-4"),
                html.Button("Send Message",
                            className="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition duration-300")
            ])
        ])

if __name__ == "__main__":
    app = PortfolioApp()
    app.app.run_server(debug=True)
