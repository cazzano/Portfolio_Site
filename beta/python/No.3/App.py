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

        self.app.title = "Creative Portfolio"
        self.app.layout = self.create_layout()
        self.register_callbacks()

    def create_layout(self):
        return html.Div([
            # Sidebar Navigation
            html.Div([
                # Profile Section
                html.Div([
                    html.Div(
                        html.Div(
                            html.I(className="fas fa-user-astronaut text-6xl text-blue-600"),
                            className="w-32 h-32 rounded-full bg-yellow-100 flex items-center justify-center"
                        ),
                        className="mb-4"
                    ),
                    html.H2("Alex Rodriguez", className="text-2xl font-bold text-red-600"),
                    html.P("Creative Developer", className="text-sm text-blue-500")
                ], className="text-center p-6"),

                # Navigation Links
                html.Nav([
                    html.Ul([
                        html.Li(html.A([
                            html.I(className="fas fa-home mr-3 text-red-500"),
                            "Home"
                        ], href="/", className="block py-2 px-4 hover:bg-yellow-100")),
                        html.Li(html.A([
                            html.I(className="fas fa-project-diagram mr-3 text-blue-500"),
                            "Projects"
                        ], href="/projects", className="block py-2 px-4 hover:bg-yellow-100")),
                        html.Li(html.A([
                            html.I(className="fas fa-code mr-3 text-red-500"),
                            "Skills"
                        ], href="/skills", className="block py-2 px-4 hover:bg-yellow-100")),
                        html.Li(html.A([
                            html.I(className="fas fa-envelope mr-3 text-blue-500"),
                            "Contact"
                        ], href="/contact", className="block py-2 px-4 hover:bg-yellow-100"))
                    ], className="space-y-2")
                ], className="mt-6"),

                # Social Links
                html.Div([
                    html.Div([
                        html.A(html.I(className="fab fa-github text-2xl text-red-600 hover:text-blue-600"), href="#", className="mx-2"),
                        html.A(html.I(className="fab fa-linkedin text-2xl text-blue-600 hover:text-red-600"), href="#", className="mx-2"),
                        html.A(html.I(className="fab fa-twitter text-2xl text-yellow-500 hover:text-blue-600"), href="#", className="mx-2")
                    ], className="flex justify-center mt-6")
                ])
            ], className="fixed left-0 top-0 h-full w-64 bg-white border-r border-yellow-200 shadow-lg"),

            # Main Content Area
            html.Div([
                # Content will be dynamically loaded here
                html.Div(id='page-content', className='p-8')
            ], className="ml-64 bg-gray-50 min-h-screen"),

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
            html.Div([
                html.H1("Welcome to My Digital World",
                        className="text-5xl font-bold mb-6 text-red-600"),
                html.P("Crafting innovative solutions with code and creativity",
                       className="text-xl text-blue-500 mb-8"),
                html.Div([
                    html.A("View Projects", href="/projects",
                           className="px-6 py-3 bg-blue-600 text-white rounded-full hover:bg-red-600 transition duration-300 mr-4"),
                    html.A("Download CV", href="#",
                           className="px-6 py-3 border-2 border-yellow-500 text-yellow-500 rounded-full hover:bg-yellow-500 hover:text-white transition duration-300")
                ], className="flex items-center")
            ], className="container mx-auto px-4 py-20 text-center")
        ], className="bg-gray-50")

    def projects_page(self):
        projects = [
            {
                "name": "AI Recommendation System",
                "description": "Advanced machine learning platform",
                "technologies": ["Python", "TensorFlow", "scikit-learn"],
                "icon": "fas fa-robot"
            },
            {
                "name": "Interactive Dashboard",
                "description": "Real-time data visualization tool",
                "technologies": ["Dash", "Plotly", "React"],
                "icon": "fas fa-chart-line"
            }
        ]

        return html.Div([
            html.H2("Featured Projects",
                    className="text-4xl font-bold text-center mb-12 text-blue-600"),
            html.Div([
                html.Div([
                    html.Div([
                        html.I(className=f"{project['icon']} text-4xl mb-4 text-red-600"),
                        html.H3(project["name"],
                                className="text-2xl font-semibold mb-4 text-blue-600"),
                        html.P(project["description"],
                               className="text-gray-700 mb-4"),
                        html.Div([
                            html.Span(tech,
                                      className="bg-yellow-100 text-red-600 px-3 py-1 rounded-full mr-2 text-sm")
                            for tech in project["technologies"]
                        ])
                    ], className="p-6 bg-white rounded-lg shadow-md hover:shadow-xl transition duration-300")
                ], className="mb-6") for project in projects
            ], className="grid md:grid-cols-2 gap-6 container mx-auto")
        ], className="bg-gray-50 py-20")

    def skills_page(self):
        skills = {
            "Programming": ["Python", "JavaScript", "Java"],
            "Frameworks": ["Dash", "React", "Django"],
            "Tools": ["Git", "Docker", "Kubernetes"]
        }

        return html.Div([
            html.H2("Technical Skills",
                    className="text-4xl font-bold text-center mb-12 text-red-600"),
            html.Div([
                html.Div([ html.H3(category, className="text-2xl font-semibold mb-6 text-blue-600"),
                    html.Div([
                        html.Span(skill, className="bg-red-600 text-white px-4 py-2 rounded-full mr-2 mb-2 inline-block")
                        for skill in skill_list
                    ])
                ], className="bg-white p-6 rounded-lg shadow-md")
                for category, skill_list in skills.items()
            ], className="grid md:grid-cols-3 gap-6 container mx-auto")
        ], className="bg-gray-50 py-20")

    def contact_page(self):
        return html.Div([
            html.H2("Get in Touch", className="text-4xl font-bold text-center mb-12 text-blue-600"),
            html.Div([
                html.Form([
                    html.Div([
                        dcc.Input(
                            type="text",
                            placeholder="Your Name",
                            className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:border-red-600"
                        )
                    ], className="mb-4"),
                    html.Div([
                        dcc.Input(
                            type="email",
                            placeholder="Your Email",
                            className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:border-red-600"
                        )
                    ], className="mb-4"),
                    html.Div([
                        dcc.Textarea(
                            placeholder="Your Message",
                            className="w-full px-4 py-2 border rounded-lg focus:outline-none focus:border-red-600"
                        )
                    ], className="mb-4"),
                    html.Button("Send Message",
                                className="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-red-600 transition duration-300")
                ])
            ], className="bg-white p-6 rounded-lg shadow-md")
        ], className="bg-gray-50 py-20")

if __name__ == "__main__":
    app = PortfolioApp()
    app.app.run_server(debug=True)
