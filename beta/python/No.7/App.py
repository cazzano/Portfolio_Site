import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
from dataclasses import dataclass, field
from typing import List, Dict
import flask

@dataclass
class ProjectConfig:
    name: str
    description: str
    technologies: List[str]
    icon: str
    color_scheme: Dict[str, str]

@dataclass
class ExperienceConfig:
    company: str
    role: str
    duration: str
    highlights: List[str]
    color_scheme: Dict[str, str]

class PortfolioConfig:
    def __init__(self):
        self.projects = [
            ProjectConfig(
                name="Geometric AI",
                description="Innovative machine learning platform",
                technologies=["Python", "TensorFlow", "React"],
                icon="fas fa-cube",
                color_scheme={
                    "primary": "bg-blue-500",
                    "secondary": "text-blue-700",
                    "accent": "border-blue-300"
                }
            ),
            ProjectConfig(
                name="Quantum Network",
                description="Decentralized communication ecosystem",
                technologies=["Rust", "GraphQL", "WebAssembly"],
                icon="fas fa-hexagon",
                color_scheme={
                    "primary": "bg-red-500",
                    "secondary": "text-red-700",
                    "accent": "border-red-300"
                }
            )
        ]

        self.experiences = [
            ExperienceConfig(
                company="Innovative Solutions Inc.",
                role="Senior Software Architect",
                duration="2020 - Present",
                highlights=[
                    "Led cross-functional engineering teams",
                    "Developed scalable cloud infrastructure",
                    "Implemented advanced machine learning solutions"
                ],
                color_scheme={
                    "primary": "bg-yellow-500",
                    "secondary": "text-yellow-700",
                    "accent": "border-yellow-300"
                }
            )
        ]

class PortfolioApp:
    def __init__(self, server=None):
        # If no server is provided, create a new Flask server
        if server is None:
            server = flask.Flask(__name__)

        self.config = PortfolioConfig()
        self.app = dash.Dash(
            __name__,
            server=server,
            external_stylesheets=[
                "https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css",
                "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css"
            ],
            meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}]
        )

        # Custom geometric CSS
        self.app.index_string = '''
        <!DOCTYPE html>
        <html>
            <head>
                {%metas%}
                <title>{%title%}</title>
                {%favicon%}
                {%css%}
                <style>
                    body {
                        background-color: #f4f4f6;
                        font-family: 'Inter', sans-serif;
                    }
                    .geometric-bg {
                        background-image:
                            linear-gradient(45deg, rgba(0,0,0,0.05) 25%, transparent 25%),
                            linear-gradient(-45deg, rgba(0,0,0,0.05) 25%, transparent 25%);
                        background-size: 50px 50px;
                    }
                    .shape-icon {
                        position: relative;
                        width: 80px;
                        height: 80px;
                        clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        margin: 0 auto;
                    }
                    .cube {
                        clip-path: polygon(25% 0%, 75% 0%, 100% 50%, 75% 100%, 25% 100%, 0% 50%);
                    }
                    .hexagon {
                        clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%);
                    }
                </style>
            </head>
            <body>
                {%app_entry%}
                <footer>
                    {%config%}
                    {%scripts%}
                    {%renderer%}
                </footer>
            </body>
        </html>
        '''

        self.app.title = "Geometric Digital Portfolio"
        self.app.layout = self._create_layout()
        self._register_callbacks()

    def _create_layout(self):
        return html.Div([
            # Sidebar Navigation
            html.Div([
                html.Div([
                    # Geometric Logo
                    html .Div([
                        html.Div(
                            html.Span("AR", className="text-white text-2xl font-bold"),
                            className="shape-icon bg-black"
                        )
                    ], className="mb-12 flex justify-center"),

                    # Navigation Links
                    html.Div([
                        html.A([
                            html.I(className="fas fa-home mr-3"),
                            "Home"
                        ], href="/", className="block py-3 px-4 hover:bg-gray-100 rounded-lg"),
                        html.A([
                            html.I(className="fas fa-project-diagram mr-3"),
                            "Projects"
                        ], href="/projects", className="block py-3 px-4 hover:bg-gray-100 rounded-lg"),
                        html.A([
                            html.I(className="fas fa-briefcase mr-3"),
                            "Experience"
                        ], href="/experience", className="block py-3 px-4 hover:bg-gray-100 rounded-lg"),
                        html.A([
                            html.I(className="fas fa-envelope mr-3"),
                            "Contact"
                        ], href="/contact", className="block py-3 px-4 hover:bg-gray-100 rounded-lg")
                    ], className="space-y-2")
                ], className="p-6")
            ], className="fixed left-0 top-0 h-full w-64 bg-white border-r geometric-bg"),

            # Main Content Area
            html.Div([
                # Dynamic Content Container
                html.Div(id='page-content', className='ml-64 p-12')
            ]),

            # Routing Component
            dcc.Location(id='url', refresh=False)
        ], className="min-h-screen")

    def _register_callbacks(self):
        @self.app.callback(
            Output('page-content', 'children'),
            [Input('url', 'pathname')]
        )
        def display_page(pathname):
            page_routes = {
                '/': self.home_page,
                '/projects': self.projects_page,
                '/experience': self.experience_page,
                '/contact': self.contact_page
            }
            return page_routes.get(pathname, self.home_page)()

    def home_page(self):
        return html.Div([
            html.Div([
                html.H1("Geometric Digital Solutions",
                        className="text-5xl font-bold mb-6 text-center"),
                html.P("Crafting innovative technologies with precision and creativity",
                       className="text-xl text-gray-600 text-center mb-12"),

                # Geometric Action Buttons
                html.Div([
                    html.A("View Projects", href="/projects",
                           className="px-8 py-3 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition duration-300 mr-4"),
                    html.A("Download CV", href="#",
                           className="px-8 py-3 border-2 border-red-500 text-red-500 rounded-lg hover:bg-red-500 hover:text-white transition duration-300")
                ], className="flex justify-center")
            ], className="max-w-2xl mx-auto text-center mt-24")
        ])

    def projects_page(self):
        return html.Div([
            html.H2("Featured Projects", className="text-4xl font-bold text-center mb-12 text-gray-800"),
            html.Div([
                html.Div([
                    html.Div([
                        # Project Icon
                        html.Div(className=f"shape-icon {project.color_scheme['primary']} mb-4"),
                        html.H3(project.name, className=f"text-2xl font-bold mb-2 {project.color_scheme['secondary']}"),
                        html.P(project.description, className="text-gray-600 mb-2"),
                        # Technologies
                        html.Div([
                            html.Span(", ".join(project.technologies), className="text-sm text-gray-500")
                        ], className="text-center")
                    ], className=f"p-6 rounded-lg shadow-lg border {project.color_scheme['accent']} mb-8")
                for project in self.config.projects
                ])
            ], className="grid grid-cols-1 md:grid-cols-2 gap-8")
        ])

    def experience_page(self):
        return html.Div([
            html.H2("Professional Experience", className="text-4xl font-bold text-center mb-12 text-gray-800"),
            html.Div([
                html.Div([
                    html.H3(exp.company, className="text-2xl font-bold mb-2"),
                    html.P(exp.role, className="text-lg text-gray-600 mb-1"),
                    html.P(exp.duration, className="text-sm text-gray-500 mb-4"),
                    html.Ul([
                        html.Li(highlight, className="text-gray-600") for highlight in exp.highlights
                    ])
                ], className=f"p-6 rounded-lg shadow-lg border {exp.color_scheme['accent']} mb-8")
                for exp in self.config.experiences
            ], className="grid grid-cols-1 md:grid-cols-2 gap-8")
        ])

    def contact_page(self):
        return html.Div([
            html.H2("Get in Touch", className="text-4xl font-bold text-center mb-6"),
            html.P("I would love to connect! Reach out via email or connect with me on LinkedIn.", className="text-lg text-center mb-4"),
            html.A("Email Me", href="mailto:your-email@example.com", className="text-blue-500"),
            html.Br(),
            html.A("LinkedIn", href="https://www.linkedin.com/in/your-profile", className="text-blue-500")
        ])

    def run(self):
        self.app.run_server(debug=True)

if __name__ == "__main__":
    portfolio = PortfolioApp()
    portfolio.run()
