import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import flask

class PortfolioApp:
    def __init__(self, server=None):
        # If no server is provided, create a new Flask server
        if server is None:
            server = flask.Flask(__name__)

        # Initialize Dash app with the server
        self.app = dash.Dash(
            __name__,
            server=server,
            external_stylesheets=[
                "https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css",
                "https://cdn.jsdelivr.net/npm/daisyui@1.14.0/dist/full.css",
                "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css"
            ],
            meta_tags=[
                {"name": "viewport", "content": "width=device-width, initial-scale=1"}
            ]
        )

        self.app.title = "Colorful Developer Portfolio"

        self.app.layout = self.create_layout()
        self.register_callbacks()

    def create_layout(self):
        return html.Div([
            # Navbar with Red, Yellow, Blue Theme
            html.Nav(className="navbar bg-gradient-to-r from-red-600 via-yellow-500 to-blue-600 text-white shadow-lg", children=[
                html.Div(className="flex-1", children=[
                    html.A(
                        html.I(className="fas fa-user-circle text-2xl"),
                        href="/",
                        className="btn btn-ghost normal-case text-xl"
                    ),
                    html.Span("Your Name", className="text-xl font-bold ml-2")
                ]),
                html.Div(className="flex-none", children=[
                    html.Ul(className="menu menu-horizontal p-0", children=[
                        html.Li(html.A([
                            html.I(className="fas fa-home mr-2 text-red-300"),
                            "Home"
                        ], href="/")),
                        html.Li(html.A([
                            html.I(className="fas fa-project-diagram mr-2 text-yellow-300"),
                            "Projects"
                        ], href="/projects")),
                        html.Li(html.A([
                            html.I(className="fas fa-code mr-2 text-blue-300"),
                            "Skills"
                        ], href="/skills")),
                        html.Li(html.A([
                            html.I(className="fas fa-envelope mr-2 text-red-300"),
                            "Contact"
                        ], href="/contact")),
                    ])
                ])
            ]),

            # Content area with Soft Background
            html.Div(id='page-content', className='p-4 bg-gradient-to-br from-red-50 via-yellow-50 to-blue-50 text-gray-800'),

            # Pages
            dcc.Location(id='url', refresh=False)
        ])

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
        return html.Div(className="hero min-h-screen", children=[
            html.Div(className="hero-content flex-col lg:flex-row", children=[
                html.Div(className="max-w-md", children=[
                    html.H1("Welcome to My Portfolio", className="text-5xl font-bold text-red-600"),
                    html.P("I'm a passionate developer creating innovative solutions", className="py-6 text-blue-600"),
                    html.A([
                        html.I(className="fas fa-eye mr-2"),
                        "View My Projects"
                    ], href="/projects", className="btn btn-primary bg-yellow-500 hover:bg-yellow-600 text-white")
                ]),
                html.Div(className="max-w-sm flex justify-center items-center", children=[
                    html.I(className="fas fa-user-circle text-6xl text-blue-600")
                ])
            ])
        ])

    def projects_page(self):
        projects = [
            {
                "name": "Project 1",
                "description": "A web application for task management",
                "technologies": ["Python", "Dash", "Bootstrap"],
                "link": "#"
            },
            {
                "name": "Project 2",
                "description": "Machine learning recommendation system",
                "technologies": ["Python", "scikit-learn", "Pandas"],
                "link": "#"
            }
        ]

        return html.Div(className="p-4", children=[
            html.H2("My Projects", className="text-3xl font-bold mb-4 text-red-600"),
            html.Div(className="grid grid-cols-1 md:grid-cols-2 gap-4", children=[
                html.Div(className="card bg-white shadow-lg rounded-lg border-2 border-yellow-500", children=[
                    html.Div(className="card-body", children=[
                        html.H5(project["name"], className="card-title text-xl font-semibold text-blue-600"),
                        html.P(project["description"], className="card-text text-red-600"),
                        html.P(f"Technologies: {', '.join(project['technologies'])}", className="card-text text-yellow-600"),
                        html.A([
                            html.I(className="fas fa-link mr-2"),
                            "View Project"
                        ], href=project["link"], className="btn btn-primary bg-blue-500 hover:bg-blue-600 text-white")
                    ])
                ]) for project in projects
            ])
        ])

    def skills_page(self):
        skills = {
            "Programming Languages": ["Python", "JavaScript", "Java"],
            "Web Technologies": ["Dash", "Flask", "React"],
            "Data Science": ["Pandas", "NumPy", "scikit-learn"]
        }

        return html.Div(className="p-4", children=[
            html.H2("My Skills", className="text-3xl font-bold mb-4 text-yellow-600"),
            html.Div(className="grid grid-cols-1 md:grid-cols-3 gap-4", children=[
                html.Div(className="card bg-white shadow-lg rounded-lg border-2 border-red-500", children=[
                    html.Div(className="card-body", children=[
                        html.H4(category, className="card-title text-xl font-semibold text-blue-600"),
                        html.Ul(className="list-disc pl-5", children=[
                            html.Li([
                                html.I(className="fas fa-check mr-2 text-yellow-500"),
                                skill
                            ]) for skill in skills_list
                        ])
                    ])
                ]) for category, skills_list in skills.items()
            ])
        ])

    def contact_page(self):
        return html.Div(className="p-4", children=[
            html.H2("Contact Me", className="text-3xl font-bold mb-4 text-blue-600"),
            html.Form(children=[
                html.Div(className="form-control mb-4", children=[
                    html.Label("Name", className="label text-red-600"),
                    dcc.Input(type="text", placeholder="Your Name", className="input input-bordered border-yellow-500") ]),
                html.Div(className="form-control mb-4", children=[
                    html.Label("Email", className="label text-red-600"),
                    dcc.Input(type="email", placeholder="Your Email", className="input input-bordered border-yellow-500")
                ]),
                html.Div(className="form-control mb-4", children=[
                    html.Label("Message", className="label text-red-600"),
                    dcc.Textarea(placeholder="Your Message", className="textarea textarea-bordered border-yellow-500")
                ]),
                html.Button([
                    html.I(className="fas fa-paper-plane mr-2"),
                    "Send Message"
                ], className="btn btn-primary bg-blue-600 hover:bg-blue-700 text-white")
            ])
        ])

if __name__ == "__main__":
    app = PortfolioApp()
    app.app.run_server(debug=True)
