#!/usr/bin/env python3
"""
Professional Portfolio Website for Innocent Nzimenyera
Built with Flask - A modern, responsive data scientist portfolio
"""

from flask import Flask, render_template, send_from_directory, jsonify
import os
from datetime import datetime

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-change-in-production'

# Portfolio Data
PROFILE_DATA = {
    'name': 'Innocent Nzimenyera',
    'title': 'AI and Data Analyst | Data Engineering Specialist',
    'tagline': 'Digital and data leader with expertise in designing scalable data pipelines, managing databases, and building cloud-based architectures',
    'bio': """Digital and data leader with expertise in designing scalable data pipelines, managing databases, and building cloud-based architectures. Skilled in SQL, Python, and data integration to support advanced analytics and decision-making. Strong background in automation, ETL processes, and data governance with experience delivering solutions for international organizations, governments, and research institutions. Adept at bridging data engineering with applied AI and statistical methods to improve efficiency, data quality, and stakeholder impact.""",
    'location': 'Kigali, Rwanda',
    'email': 'innocent.nzimenyera@email.com',  # Update with actual email from CV if needed
    'linkedin': 'https://linkedin.com/in/innocent-nzimenyera',  # Update with actual LinkedIn
    'github': 'https://github.com/Innocent50',  # Update with actual GitHub
    'phone': '+250 781 946 105'
}

SKILLS = {
    'Data Engineering & Databases': ['SQL', 'PostgreSQL', 'Oracle', 'Access', 'Data Warehousing', 'ETL Pipelines'],
    'Programming Languages': ['Python', 'JavaScript', 'Vue.js', 'C/C++', 'Java', 'R'],
    'Cloud & Infrastructure': ['Linux', 'Git', 'Bash', 'Docker', 'GitHub/GitLab', 'Kubernetes', 'Spark', 'Terraform', 'AWS/GCP'],
    'Analytics & Visualization': ['Tableau', 'Power BI', 'MATLAB', 'Stata', 'SPSS', 'Advanced Excel'],
    'Machine Learning & AI': ['TensorFlow', 'PyTorch', 'Scikit-learn', 'Keras', 'CNNs', 'RNNs', 'NLP'],
    'Languages': ['Kinyarwanda (Native)', 'English (Fluent)', 'French (Basic)', 'Swahili (Basic)']
}

EXPERIENCE = [
    {
        'title': 'AI and Data Analyst',
        'company': 'Global Green Growth Institute (GGGI)',
        'duration': 'Nov 2024 - Present',
        'location': 'Seoul, South Korea (Remote)',
        'responsibilities': [
            'Designing and deploying dashboards enabling policymakers to explore the Green Growth Index',
            'Automating ETL pipelines to reduce manual data collection and improve efficiency',
            'Developing an online policy simulation model incorporating dozens of variables using statistical and AI-driven economic models',
            'Training team members on modeling, coding best practices, and reproducible pipelines',
            'Supporting publication of technical reports and policy briefs'
        ]
    },
    {
        'title': 'AI for Good Scholar',
        'company': 'United Nations/International Telecommunication Union (ITU)',
        'duration': 'Apr 2024 - July 2025',
        'location': 'Geneva, Switzerland (Hybrid)',
        'responsibilities': [
            'Conducted research on AI applications for UN Sustainable Development Goals',
            'Analyzed and improved AI use cases for global impact',
            'Collaborated with international use cases authors on AI projects',
            'Communicated findings and insights effectively to stakeholders'
        ]
    },
    {
        'title': 'Data Science Consultant',
        'company': 'Global Green Growth Institute (GGGI)',
        'duration': 'June 2021 - Oct 2024',
        'location': 'Seoul, South Korea (Remote)',
        'responsibilities': [
            'Collaborated with GGPM Team to establish databases, tools, guidelines, and documentation',
            'Conducted data collection, analysis, and reporting for the Green Growth Index and Simulation Tool',
            'Built Python-based data pipelines to extract, clean, and integrate international datasets',
            'Applied statistical methods to enhance data quality and reliability',
            'Supported capacity-building workshops and conferences on data and analytics'
        ]
    },
    {
        'title': 'Graduate Teaching Assistant',
        'company': 'Carnegie Mellon University',
        'duration': 'Aug 2023 - May 2024',
        'location': 'Kigali, Rwanda',
        'responsibilities': [
            'Assisted delivery of advanced data analytics courses using Python',
            'Supported students in data modeling, pipeline development, and coding assignments',
            'Implemented automated grading systems using AI algorithms'
        ]
    },
    {
        'title': 'Digital Ambassador',
        'company': 'Rwanda Ministry of ICT and Innovation',
        'duration': 'Sept 2019 - June 2021',
        'location': 'Kigali, Rwanda',
        'responsibilities': [
            'Facilitated digital literacy training, increasing citizens access to online services',
            'Designed and updated ICT course content to meet community needs',
            'Created user-friendly reporting templates for use by government staff'
        ]
    }
]

EDUCATION = [
    {
        'degree': 'Master of Science in Information Technology',
        'institution': 'Carnegie Mellon University',
        'duration': 'Aug 2022 - May 2024',
        'location': 'Kigali, Rwanda',
        'details': 'Specialization in Applied Machine Learning and Data Science'
    },
    {
        'degree': 'BSc (Hons) in Computer Science',
        'institution': 'University of Rwanda, College of Science and Technology',
        'duration': 'Sep 2015 - Nov 2019',
        'location': 'Huye and Kigali, Rwanda',
        'details': 'Focus on Computer Science and Software Engineering'
    },
    {
        'degree': 'High School Certificate',
        'institution': 'Group scolaire Remera Rukoma',
        'duration': 'Sep 2012 - Nov 2014',
        'location': 'Kamonyi, Rwanda',
        'details': 'Mathematics, Physics, and Computer Science'
    }
]

PROJECTS = [
    {
        'title': 'Green Growth Index',
        'description': 'Interactive dashboard platform enabling policymakers to explore country performance in achieving sustainability targets including Sustainable Development Goals and Paris Climate Agreement',
        'technologies': ['Python', 'Data Visualization', 'Statistical Analysis', 'Web Development'],
        'github': 'https://github.com/Innocent50/green-growth-index',
        'demo': 'https://ggindex-simtool.gggi.org/',
        'image': '/static/images/green-growth-index.png'
    },
    {
        'title': 'AI-Supported Green Growth Simulation Tool',
        'description': 'Advanced AI-driven simulation tool that assesses Sustainable Development Goal co-benefits using machine learning and statistical economic models for policy impact analysis',
        'technologies': ['Python', 'AI/ML', 'Economic Modeling', 'Policy Simulation'],
        'github': 'https://github.com/Innocent50/ai-simulation-tool',
        'demo': 'https://ggindex-simtool.gggi.org/',
        'image': '/static/images/sim.jpg'
    },
    {
        'title': 'Efficient Connected Components Solution Using DFS',
        'description': 'Research project implementing efficient algorithms for connected components using Depth-First Search with optimized performance',
        'technologies': ['Python', 'C/C++', 'Algorithm Design', 'Graph Theory'],
        'github': 'https://github.com/Innocent50/connected-components-dfs',
        'demo': '#',
        'image': '/static/images/project3.jpg'
    },
    {
        'title': 'National Green Growth Indexes (Kenya & Ghana)',
        'description': 'Developed comprehensive national green growth assessment tools for Kenya and Ghana, measuring sustainability performance and policy effectiveness',
        'technologies': ['Python', 'Statistical Analysis', 'Data Visualization', 'Policy Modeling'],
        'github': 'https://github.com/Innocent50/national-green-indexes',
        'demo': '#',
        'image': '/static/images/project3.jpg'
    },
    {
        'title': 'Learn Python for Machine Learning',
        'description': 'Educational resource and tutorial series for learning Python programming with focus on machine learning applications',
        'technologies': ['Python', 'Jupyter Notebooks', 'Machine Learning', 'Education'],
        'github': 'https://github.com/Innocent50/python-ml-tutorial',
        'demo': '#',
        'image': '/static/images/project-placeholder.jpg'
    }
]

# Routes
@app.route('/')
def index():
    """Main portfolio page"""
    return render_template('index.html', 
                         profile=PROFILE_DATA,
                         skills=SKILLS,
                         experience=EXPERIENCE,
                         education=EDUCATION,
                         projects=PROJECTS)

# Removed separate about page - content is on main page

@app.route('/projects')
def projects():
    """Projects showcase page"""
    return render_template('projects.html', 
                         projects=PROJECTS,
                         profile=PROFILE_DATA)

@app.route('/contact')
def contact():
    """Contact information page"""
    return render_template('contact.html', 
                         profile=PROFILE_DATA)

@app.route('/resume')
def resume():
    """Resume/CV page"""
    return render_template('resume.html',
                         profile=PROFILE_DATA,
                         skills=SKILLS,
                         experience=EXPERIENCE,
                         education=EDUCATION)

@app.route('/api/contact', methods=['POST'])
def api_contact():
    """API endpoint for contact form submissions"""
    # This would typically handle form submissions
    # For now, return a simple response
    return jsonify({'status': 'success', 'message': 'Message received!'})

@app.route('/download/cv')
def download_cv():
    """Download CV/Resume file"""
    try:
        return send_from_directory('static/files', 'CV_Innocent.pdf', as_attachment=True)
    except FileNotFoundError:
        # Fallback if file not found
        return send_from_directory('static/media', 'CV_Innocent.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8080)
