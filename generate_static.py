#!/usr/bin/env python3
"""
Generate static HTML files from Flask templates for GitHub Pages deployment
"""

from app import app, PROFILE_DATA, SKILLS, EXPERIENCE, EDUCATION, PROJECTS, PUBLICATIONS
from flask import url_for
import os
import shutil

def generate_static_site():
    """Generate static HTML files"""
    
    # Create output directory
    output_dir = 'docs'  # GitHub Pages can serve from docs/ folder
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)
    
    # Copy static files
    if os.path.exists('static'):
        shutil.copytree('static', os.path.join(output_dir, 'static'))
    
    with app.test_client() as client:
        with app.app_context():
            # Generate index.html
            print("Generating index.html...")
            response = client.get('/')
            with open(os.path.join(output_dir, 'index.html'), 'w', encoding='utf-8') as f:
                f.write(response.get_data(as_text=True))
            
            # Generate contact.html
            print("Generating contact.html...")
            response = client.get('/contact')
            with open(os.path.join(output_dir, 'contact.html'), 'w', encoding='utf-8') as f:
                f.write(response.get_data(as_text=True))
            
            # Generate projects.html
            print("Generating projects.html...")
            response = client.get('/projects')
            with open(os.path.join(output_dir, 'projects.html'), 'w', encoding='utf-8') as f:
                f.write(response.get_data(as_text=True))
    
    # Update links in HTML files to work with static hosting
    update_static_links(output_dir)
    
    print(f"Static site generated in '{output_dir}' directory!")
    print("Ready for GitHub Pages deployment!")

def update_static_links(output_dir):
    """Update Flask URL links to work with static hosting"""
    
    files_to_update = [
        os.path.join(output_dir, 'index.html'),
        os.path.join(output_dir, 'contact.html'), 
        os.path.join(output_dir, 'projects.html')
    ]
    
    replacements = [
        # Update Flask routes to static paths
        ('href="/contact"', 'href="contact.html"'),
        ('href="/projects"', 'href="projects.html"'),
        ('href="/"', 'href="index.html"'),
        ('action="/api/contact"', 'action="#"'),  # Disable form submission for static
        # Update static file paths to be relative
        ('href="/static/', 'href="static/'),
        ('src="/static/', 'src="static/'),
    ]
    
    for file_path in files_to_update:
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            for old, new in replacements:
                content = content.replace(old, new)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
    
    print("Updated links for static hosting!")

if __name__ == "__main__":
    generate_static_site()
