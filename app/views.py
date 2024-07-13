from flask import Blueprint, render_template, request
from app import data

views = Blueprint('views', __name__, template_folder='templates')


# Hero Page
@views.route('/')
def hero():
    return render_template('hero.html')

# About Me
@views.route('/aboutme')
def about_me():
    return render_template('routes/aboutme/about_me.html', navbar=data.NavBarItems, footer=data.FooterItems, timeline=data.WorkExperience)

# Blogs
@views.route('/hobbies')
def blog():
    return render_template('routes/hobbies/hobbies.html', navbar=data.NavBarItems, footer=data.FooterItems, data=data.HobbyHeader, hobbies=data.Hobby)

# Projects
@views.route('/projects')
def project():
    return render_template('routes/projects/projects.html', navbar=data.NavBarItems, footer=data.FooterItems, data=data.ProjectsHeader, projects=data.Projects )

@views.route('/experience')
def experience():
    return render_template('routes/experience/experience.html', navbar=data.NavBarItems, footer=data.FooterItems, timeline=data.WorkExperience)

@views.route('/map')
def map():
    return render_template('routes/map/map.html', navbar=data.NavBarItems, footer=data.FooterItems)

@views.route('/timeline')
def timeline():
    return render_template('routes/timeline/timeline.html')