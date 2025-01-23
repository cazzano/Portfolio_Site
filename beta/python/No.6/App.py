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
    accent_color: str

@dataclass
class ExperienceConfig:
    company: str
    role: str
    duration: str
    description: str
    icon: str

class PortfolioConfig:
    def __init__(self):
        self.projects = [
            ProjectConfig(
                name="Quantum Nexus",
                description="Decentralized AI-powered platform",
                technologies=["Rust", "WebAssembly", "GraphQL"],
                icon="fas fa-atom",
                accent_color="text-cyan-400"
            ),
            ProjectConfig(
                name="Cyber Sentinel",
                description="Advanced cybersecurity ecosystem",
                technologies=["Python", "Blockchain", "Machine Learning"],
                icon="fas fa-shield-alt",
                accent_color="text-purple-400"
            )
        ]

        self.experiences = [
            ExperienceConfig(
                company="Innovative Tech Solutions",
                role="Lead Software Architect",
                duration="2021 - Present",
                description="Pioneering next-generation technological solutions",
                icon="fas fa-code"
            ),
            ExperienceConfig(
                company="Quantum Research Labs",
                role="AI Research Engineer",
                duration="2019 - 2021",
                description="Developing cutting-edge machine learning algorithms",
                icon="fas fa-brain"
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

        # Custom CSS for futuristic design
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
                        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
                        color: #fff;
                    }
                    .glitch-text {
                        position: relative;
                        text-shadow:
                            0.05em 0 0 #00fffc,
                            -0.05em -0.025em 0 #fc00ff,
                            -0.025em 0.05em 0 #fffc00;
                        animation: glitch 500ms infinite;
                    }
                    @keyframes glitch {
                        0% {
                            text-shadow:
                                0.05em 0 0 #00fffc,
                                -0.05em -0.025em 0 #fc00ff,
                                -0.025em 0.05em 0 #fffc00;
                        }
                        14% {
                            text-shadow:
                                0.05em 0 0 #00fffc,
                                -0.05em -0.025em 0 #fc00ff,
                                -0.025em 0.05em 0 #fffc00;
                        }
                        15% {
                            text-shadow:
                                -0.05em -0.025em 0 #00fffc,
                                0.025em 0.025em 0 #fc00ff,
                                -0.05em -0.05em 0 #fffc00;
                        }
                        49% {
                            text-shadow:
                                -0.05em -0.025em 0 #00fffc,
                                0.025em 0.025em 0 #fc00ff,
                                -0.05em -0.05em 0 #fffc00;
                        }
                        50% {
                            text-shadow:
                                0.025em 0.05em 0 #00fffc,
                                0.05em 0 0 #fc00ff,
                                0 -0.05em 0 #fffc00;
                        }
                        99% {
                            text-shadow:
                                0.025em 0.05em 0 #00fffc ,
                                0.05em 0 0 #fc00ff,
                                0 -0.05em 0 #fffc00;
                        }
                        100% {
                            text-shadow:
                                -0.025em 0 0 #00fffc,
                                -0.025em -0.025em 0 #fc00ff,
                                -0.025em -0.05em 0 #fffc00;
                        }
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

        self.app.title = "Cyber Quantum Portfolio"
        self.app.layout = self._create_layout()
        self._register_callbacks()

    def _create_layout(self):
        return html.Div([
            # Sidebar Navigation
            html.Div([
                html.Div([
                    # Logo with Glitch Effect
                    html.Div([
                        html.Span("AR", className="glitch-text text-4xl font-bold text-white")
                    ], className="text-center mb-12"),

                    # Navigation Links
                    html.Div([
                        html.A([
                            html.I(className="fas fa-home mr-3"),
                            "Home"
                        ], href="/", className="block py-3 px-4 text-white hover:bg-purple-800 rounded-lg"),
                        html.A([
                            html.I(className="fas fa-project-diagram mr-3"),
                            "Projects"
                        ], href="/projects", className="block py-3 px-4 text-white hover:bg-purple-800 rounded-lg"),
                        html.A([
                            html.I(className="fas fa-briefcase mr-3"),
                            "Experience"
                        ], href="/experience", className="block py-3 px-4 text-white hover:bg-purple-800 rounded-lg"),
                        html.A([
                            html.I(className="fas fa-envelope mr-3"),
                            "Contact"
                        ], href="/contact", className="block py-3 px-4 text-white hover:bg-purple-800 rounded-lg")
                    ], className="space-y-2")
                ], className="p-6")
            ], className="fixed left-0 top-0 h-full w-64 bg-black/50 backdrop-blur-lg"),

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
            html.H1("Welcome to My Portfolio", className="text-5xl font-bold text-center mb-8"),
            html.P("Explore my projects and experiences in the world of technology.", className="text-lg text-center")
        ])

    def projects_page(self):
        return html.Div([
            html.H2("Projects", className="text-4xl font-bold mb-6"),
            html.Div([
                html.Div([
                    html.I(className=project.icon + " text-3xl"),
                    html.H3(project.name, className="text-2xl"),
                    html.P(project.description),
                    html.P("Technologies: " + ", ".join(project.technologies), className="text-sm text-gray-400"),
                ], className="border p-4 rounded-lg mb-4", style={"backgroundColor": project.accent_color})
                for project in self.config.projects
            ])
        ])

    def experience_page(self):
        return html.Div([
            html.H2("Experience", className="text-4xl font-bold mb-6"),
            html.Div([
                html.Div([
                    html.I(className=experience.icon + " text-3xl"),
                    html.H3(experience.role + " at " + experience.company, className="text-2xl"),
                    html.P(experience.description),
                    html.P("Duration: " + experience.duration, className="text-sm text-gray-400"),
                ], className="border p-4 rounded-lg mb-4")
                for experience in self.config.experiences
            ])
        ])

    def contact_page(self):
        return html.Div([
            html.H2("Contact Me", className="text-4xl font-bold mb-6"),
            html.P("Feel free to reach out via email or connect with me on LinkedIn.", className="text-lg"),
            html.A("Email Me", href="mailto:your-email@example.com", className="text-blue-500"),
            html.Br(),
            html.A("LinkedIn", href="https://www.linkedin.com/in/your-profile", className="text-blue-500")
        ])

    def run(self):
        self.app.run_server(debug=True)

if __name__ == "__main__":
    portfolio = PortfolioApp()
    portfolio.run()
