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
    gradient: str

@dataclass
class ServiceConfig:
    name: str
    description: str
    icon: str

class PortfolioConfig:
    def __init__(self):
        self.projects = [
            ProjectConfig(
                name="Neural Network Explorer",
                description="Advanced AI-powered data analysis platform",
                technologies=["PyTorch", "React", "Docker"],
                icon="fas fa-brain",
                gradient="from-purple-500 to-pink-500"
            ),
            ProjectConfig(
                name="Quantum Visualization",
                description="Real-time quantum computing simulation",
                technologies=["Qiskit", "D3.js", "WebGL"],
                icon="fas fa-atom",
                gradient="from-blue-500 to-green-500"
            )
        ]

        self.services = [
            ServiceConfig(
                name="Software Engineering",
                description="Cutting-edge solution development",
                icon="fas fa-code"
            ),
            ServiceConfig(
                name="AI Consulting",
                description="Intelligent system design",
                icon="fas fa-robot"
            ),
            ServiceConfig(
                name="Cloud Architecture",
                description="Scalable infrastructure solutions",
                icon="fas fa-cloud"
            )
        ]

class PortfolioApp:
    def __init__(self, server=None):
        # Initialize Dash app with optional Flask server
        self.config = PortfolioConfig()

        # If no server is provided, create a new Flask server
        if server is None:
            server = flask.Flask(__name__)

        # Initialize Dash app with the server
        self.app = dash.Dash(
            __name__,
            server=server,
            external_stylesheets=[
                "https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css",
                "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css"
            ],
            meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}]
        )

        self.app.title = "Quantum Digital Portfolio"
        self.app.layout = self._create_layout()
        self._register_callbacks()

    def _create_layout(self):
        return html.Div([
            # Navigation
            html.Nav([
                html.Div([
                    html.Div([
                        html.Span("AR", className="text-2xl font-bold text-white bg-black px-3 py-1 rounded-full mr-4"),
                        html.Div([
                            html.A("Home", href="/", className="mx-3 text-gray-700 hover:text-black"),
                            html.A("Projects", href="/projects", className="mx-3 text-gray-700 hover:text-black"),
                            html.A("Services", href="/services", className="mx-3 text-gray-700 hover:text-black"),
                            html.A("Contact", href="/contact", className="mx-3 text-gray-700 hover:text-black")
                        ], className="inline-block")
                    ], className="flex items-center justify-between")
                ], className="container mx-auto py-6")
            ], className="border-b border-gray-200"),

            # Dynamic Content
            html.Div(id='page-content', className='min-h-screen'),

            # Footer
            html.Footer([
                html.Div([
                    html.Div([
                        html.Div([
                            html.A(html.I(className="fab fa-github text-2xl mr-4"), href="#"),
                            html.A(html.I(className="fab fa-linkedin text-2xl mr-4"), href="#"),
                            html.A(html.I(className="fab fa-twitter text-2xl"), href="#")
                        ], className="flex justify-center mb-4")
                    ], className="container mx-auto")
                ], className="bg-gray-100 py-8")
            ]),

            # Routing
            dcc.Location(id='url', refresh=False)
        ])

    def _register_callbacks(self):
        @self.app.callback(
            Output('page-content', 'children'),
            [Input('url', 'pathname')]
        )
        def display_page(pathname):
            page_routes = {
                '/': self.home_page,
                '/projects': self.projects_page,
                '/services': self.services_page,
                '/contact': self.contact_page
            }
            return page_routes.get(pathname, self.home_page)()

    def home_page(self):
        return html.Div([
            html.Div([
                html.Div([
                    html.H1("Alex Rodriguez", className="text-6xl font-bold mb-4"),
                    html.H2("Quantum Software Architect", className="text-2xl text-gray-600 mb-8"),
                    html.P("Bridging the gap between innovative technology and transformative solutions.",
                           className="text-xl text-gray-500 mb-12"),
                    html.Div([
                        html.A("View Projects", href="/projects",
                               className="px-8 py-3 bg-black text-white rounded-full mr-4 hover:bg-gray-800"),
                        html.A("Download CV", href="#",
                               className="px-8 py-3 border-2 border-black text-black rounded-full hover:bg-black hover:text-white")
                    ])
                ], className="text-center max-w-2xl mx-auto")
            ], className="flex items-center justify-center min-h-screen")
        ])

    def projects_page(self):
        return html.Div([
            html.Div([
                html.H2("Featured Projects", className="text-4xl font-bold text-center mb-16"),
                html.Div([
                    html.Div([
                        html.Div([
                            html.I(className=f"{project.icon} text-5xl mb-6 bg-clip-text text-transparent bg-gradient-to-r {project.gradient}"),
                            html.H3(project.name, className="text-2xl font-bold mb-4"),
                            html.P(project.description, className="text-gray-600 mb-6"),
                            html.Div([
                                html.Span(tech, className="bg-gray-100 px-3 py-1 rounded-full text-sm mr-2 mb-2")
                                for tech in project.technologies
                            ], className="flex flex-wrap")
                        ], className="p-8 border border-gray-200 rounded-lg hover:shadow-lg transition-all")
                    ], className="mb-8") for project in self.config.projects
                ], className="grid md:grid-cols-2 gap-8")
            ], className="container mx-auto py-20")
        ])

    def services_page(self):
        return html.Div([
            html.Div([
                html.H2("Professional Services", className="text-4xl font-bold text-center mb-16"),
                html.Div([
                    html.Div([
                        html.Div([
                            html.I(className=f"{service.icon} text-5xl mb-6 text-black"),
                            html.H3(service.name, className="text-2xl font-bold mb-4"),
                            html.P(service.description, className="text-gray-600")
                        ], className="text-center p-8 border border-gray-200 rounded-lg hover:shadow-lg transition-all")
                     ]) for service in self.config.services
                ], className="grid md:grid-cols-3 gap-8")
            ], className="container mx-auto py-20")
        ])

    def contact_page(self):
        return html.Div([
            html.Div([
                html.H2("Get In Touch", className="text-4xl font-bold text-center mb-16"),
                html.Div([
                    dcc.Input(id='contact-name', placeholder="Your Name", className="input input-bordered w-full mb-4"),
                    dcc.Input(id='contact-email', placeholder="Your Email", type="email", className="input input-bordered w-full mb-4"),
                    dcc.Textarea(id='contact-message', placeholder="Your Message", className="textarea textarea-bordered w-full mb-4"),
                    html.Button("Send Message", id='send-button', className="btn bg-black text-white hover:bg-gray-800")
                ], className="bg-white p-8 border border-gray-200 rounded-lg shadow-lg")
            ], className="container mx-auto py-20")
        ])

if __name__ == "__main__":
    app = PortfolioApp()
    app.app.run_server(debug=True)
