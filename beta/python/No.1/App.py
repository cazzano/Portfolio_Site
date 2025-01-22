import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class ProjectConfig:
    name: str
    description: str
    technologies: List[str]
    icon: str
    color: str

@dataclass
class SkillConfig:
    category: str
    skills: List[str]
    icon: str

class PortfolioConfig:
    def __init__(self):
        self.projects = [
            ProjectConfig(
                name="AI Innovation Platform",
                description="Machine learning solution for predictive analytics",
                technologies=["Python", "TensorFlow", "React"],
                icon="fas fa-brain",
                color="bg-indigo-500"
            ),
            ProjectConfig(
                name="Interactive Dashboard",
                description="Real-time data visualization system",
                technologies=["Dash", "Plotly", "D3.js"],
                icon="fas fa-chart-line",
                color="bg-red-500"
            )
        ]

        self.skills = [
            SkillConfig(
                category="Programming",
                skills=["Python", "JavaScript", "TypeScript"],
                icon="fas fa-code"
            ),
            SkillConfig(
                category="Frameworks",
                skills=["Dash", "React", "Django"],
                icon="fas fa-laptop-code"
            ),
            SkillConfig(
                category="DevOps",
                skills=["Docker", "Kubernetes", "CI/CD"],
                icon="fas fa-server"
            )
        ]

class PortfolioApp:
    def __init__(self):
        self.config = PortfolioConfig()
        self.app = dash.Dash(__name__,
            external_stylesheets=[
                "https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css",
                "https://cdn.jsdelivr.net/npm/daisyui@2.51.6/dist/full.css",
                "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css"
            ],
            meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}]
        )

        self.app.title = "Professional Digital Portfolio"
        self.app.layout = self._create_layout()
        self._register_callbacks()

    def _create_layout(self):
        return html.Div([
            # Responsive Navbar
            self._create_navbar(),

            # Dynamic Content Area
            html.Div(id='page-content', className='min-h-screen bg-gray-50'),

            # Footer
            self._create_footer(),

            # Routing Component
            dcc.Location(id='url', refresh=False)
        ], className="antialiased")

    def _create_navbar(self):
        return html.Nav([
            html.Div([
                html.Div([
                    html.I(className="fas fa-code-branch text-2xl mr-4 text-indigo-600"),
                    html.Span("Alex Rodriguez", className="text-xl font-bold text-gray-800")
                ], className="flex items-center"),

                html.Div([
                    html.A([
                        html.I(className="fas fa-home mr-2"),
                        "Home"
                    ], href="/", className="btn btn-ghost btn-sm text-gray-700 hover:bg-indigo-50"),
                    html.A([
                        html.I(className="fas fa-project-diagram mr-2"),
                        "Projects"
                    ], href="/projects", className="btn btn-ghost btn-sm text-gray-700 hover:bg-indigo-50"),
                    html.A([
                        html.I(className="fas fa-laptop-code mr-2"),
                        "Skills"
                    ], href="/skills", className="btn btn-ghost btn-sm text-gray-700 hover:bg-indigo-50"),
                    html.A([
                        html.I(className="fas fa-envelope mr-2"),
                        "Contact"
                    ], href="/contact", className="btn btn-ghost btn-sm text-gray-700 hover:bg-indigo-50")
                ], className="flex space-x-2")
            ], className="container mx-auto flex justify-between items-center py-4 bg-white")
        ], className="navbar bg-white shadow-md")

    def _create_footer(self):
        return html.Footer([
            html.Div([
                html.Div([
                    html.Div([
                        html.A(html.I(className="fab fa-github text-2xl text-gray-700 hover:text-indigo-600"), href="#", className="btn btn-ghost btn-circle"),
                        html.A(html.I(className="fab fa-linkedin text-2xl text-gray-700 hover:text-blue-600"), href="#", className="btn btn-ghost btn-circle"),
                        html.A(html.I(className="fab fa-twitter text-2xl text-gray-700 hover:text-blue-400"), href="#", className="btn btn-ghost btn-circle")
                    ], className="flex justify-center space-x-4 mb-4"),
                    html.P("© 2023 Alex Rodriguez. All Rights Reserved.", className="text-center text-gray-600")
                ], className="container mx-auto")
            ], className="footer footer-center p-10 bg-gray-100 text-base-content")
        ])

    def _register_callbacks(self):
        @self.app.callback(
            Output('page-content', 'children'),
            [Input('url', 'pathname')]
        )
        def display_page(pathname):
            page_routes = {
                '/': self.home_page,
                '/home': self.home_page,
                '/projects': self.projects_page,
                '/skills': self.skills_page,
                '/contact': self.contact_page
            }
            return page_routes.get(pathname, self.home_page)()

    def home_page(self):
        return html.Div([
            html.Div([
                html.Div([
                    html.I(className="fas fa-code-branch text-6xl mb-6 text-indigo-600"),
                    html.H1("Innovating Digital Solutions",
                            className="text-5xl font-bold mb-4 text-gray-800"),
                    html.P("Transforming complex challenges into elegant technologies",
                           className="text-xl mb-8 text-gray-600"),
                    html.Div([
                        html.A([
                            html.I(className="fas fa-project-diagram mr-2"),
                            "View Projects"
                        ], href="/projects", className="btn btn-indigo"),
                        html.A([
                            html.I(className="fas fa-download mr-2"),
                            "Download CV"
                        ], href="#", className="btn btn-outline btn-indigo ml-4")
                    ], className="flex justify-center space-x-4")
                ], className="text-center max-w-2xl mx-auto py-20")
            ])
        ], className="bg-gray-50")

    def projects_page(self):
        return html.Div([
            html.Div([
                html.H2("Featured Projects", className="text-4xl font-bold text-center mb-12 text-gray-800"),
                html.Div([
                    html.Div([
                        html.Div([
                            html.I(className=f"{project.icon} text-4xl mb-4 {project.color} text-white p-4 rounded-full"),
                        ], className="flex justify-center mb-4"),
                        html.H3(project.name, className="text-2xl font-semibold mb-2 text-center text-gray-800"), html.P(project.description, className="text-gray-600 mb-4 text-center"),
                        html.Div([
                            html.Span(tech, className="badge badge-indigo badge-outline mr-2")
                            for tech in project.technologies
                        ], className="flex justify-center")
                    ], className="bg-white rounded-lg shadow-lg p-6")
                    for project in self.config.projects
                ], className="grid md:grid-cols-2 gap-8")
            ], className="container mx-auto py-20")
        ], className="bg-gray-50")

    def skills_page(self):
        return html.Div([
            html.Div([
                html.H2("Technical Skills", className="text-4xl font-bold text-center mb-12 text-gray-800"),
                html.Div([
                    html.Div([
                        html.Div([
                            html.I(className=f"{skill_group.icon} text-4xl mb-4 text-indigo-600"),
                            html.H3(skill_group.category, className="text-2xl font-semibold mb-6 text-gray-800")
                        ], className="flex flex-col items-center"),
                        html.Div([
                            html.Span(skill, className="badge badge-indigo badge-outline mr-2")
                            for skill in skill_group.skills
                        ], className="flex justify-center")
                    ], className="bg-white p-6 rounded-lg shadow-lg")
                    for skill_group in self.config.skills
                ], className="grid md:grid-cols-3 gap-8")
            ], className="container mx-auto py-20")
        ], className="bg-gray-50")

    def contact_page(self):
        return html.Div([
            html.Div([
                html.H2("Get In Touch", className="text-4xl font-bold text-center mb-12 text-gray-800"),
                html.Div([
                    dcc.Input(id='contact-name', placeholder="Name", className="input input-bordered w-full mb-4"),
                    dcc.Input(id='contact-email', placeholder="Email", type="email", className="input input-bordered w-full mb-4"),
                    dcc.Textarea(id='contact-message', placeholder="Your Message", className="textarea textarea-bordered w-full mb-4"),
                    html.Button([
                        html.I(className="fas fa-paper-plane mr-2"),
                        "Send Message"
                    ], id='send-button', className="btn btn-indigo")
                ], className="bg-white p-6 rounded-lg shadow-lg")
            ], className="container mx-auto py-20")
        ], className="bg-gray-50")

if __name__ == "__main__":
    app = PortfolioApp()
    app.app.run_server(debug=True)
