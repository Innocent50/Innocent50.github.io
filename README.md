# Professional Portfolio - Innocent Nzimenyera

A modern, responsive portfolio website built with Flask and Bootstrap, showcasing data science expertise and professional experience.

## 🚀 Features

- **Modern Design**: Clean, professional interface with smooth animations
- **Responsive Layout**: Optimized for all devices and screen sizes
- **Interactive Elements**: Smooth scrolling, hover effects, and dynamic content
- **Contact Form**: Functional contact form with validation
- **SEO Optimized**: Meta tags and structured data for better search visibility
- **Fast Loading**: Optimized assets and efficient code structure
- **Accessibility**: WCAG compliant with keyboard navigation support

## 🛠 Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **CSS Framework**: Bootstrap 5
- **Icons**: Font Awesome
- **Animations**: AOS (Animate On Scroll)
- **Fonts**: Google Fonts (Inter, JetBrains Mono)

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Innocent50/portfolio.git
   cd portfolio
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables** (optional)
   Create a `.env` file in the root directory:
   ```
   FLASK_ENV=development
   SECRET_KEY=your-secret-key-here
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser**
   Navigate to `http://localhost:5000`

## 📁 Project Structure

```
portfolio/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
│
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── index.html        # Home page
│   └── contact.html      # Contact page
│
├── static/              # Static assets
│   ├── css/
│   │   └── style.css    # Custom styles
│   ├── js/
│   │   └── main.js      # JavaScript functionality
│   ├── images/          # Image assets
│   └── files/           # Downloadable files
│       └── CV_Innocent_Nzimenyera.pdf
│
└── .env                 # Environment variables (create manually)
```

## 🎨 Customization

### Personal Information
Update the `PROFILE_DATA` dictionary in `app.py` with your information:

```python
PROFILE_DATA = {
    'name': 'Your Name',
    'title': 'Your Professional Title',
    'email': 'your.email@example.com',
    'linkedin': 'https://linkedin.com/in/yourprofile',
    'github': 'https://github.com/yourusername',
    # ... other fields
}
```

### Skills and Experience
Modify the `SKILLS`, `EXPERIENCE`, `EDUCATION`, and `PROJECTS` dictionaries in `app.py`.

### Styling
Customize colors and styles by modifying CSS variables in `static/css/style.css`:

```css
:root {
    --primary-color: #007bff;
    --primary-dark: #0056b3;
    /* ... other variables */
}
```

### Images
Replace placeholder images in `static/images/` with your own:
- `profile.jpg` - Your profile photo
- `about-image.jpg` - About section image
- `project1.jpg`, `project2.jpg`, etc. - Project screenshots

## 🚀 Deployment

### Heroku Deployment

1. **Install Heroku CLI**
2. **Create a Heroku app**
   ```bash
   heroku create your-portfolio-name
   ```

3. **Create a Procfile**
   ```
   web: gunicorn app:app
   ```

4. **Deploy**
   ```bash
   git add .
   git commit -m "Deploy portfolio"
   git push heroku main
   ```

### Other Deployment Options

- **PythonAnywhere**: Upload files and configure WSGI
- **DigitalOcean App Platform**: Connect your repository
- **AWS Elastic Beanstalk**: Deploy using AWS CLI
- **Google Cloud Platform**: Use App Engine

## 📧 Contact Form Setup

The contact form currently returns a JSON response. To make it functional:

1. **Configure email settings** in `app.py`
2. **Set up SMTP** or use services like SendGrid, Mailgun
3. **Add email sending functionality** to the `/api/contact` route

Example with Flask-Mail:
```python
from flask_mail import Mail, Message

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your-app-password'

mail = Mail(app)
```

## 🔒 Security Considerations

- Change the `SECRET_KEY` in production
- Use environment variables for sensitive data
- Enable HTTPS in production
- Implement rate limiting for contact form
- Add CSRF protection for forms

## 🎯 Performance Optimization

- **Image Optimization**: Compress images and use WebP format
- **Caching**: Implement browser caching headers
- **CDN**: Use a Content Delivery Network for static assets
- **Minification**: Minify CSS and JavaScript files
- **Lazy Loading**: Images load as user scrolls

## 🧪 Testing

Run tests (when implemented):
```bash
python -m pytest tests/
```

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Support

If you have any questions or need help with setup, feel free to reach out:

- **Email**: innocent.nzimenyera@email.com
- **LinkedIn**: [Innocent Nzimenyera](https://linkedin.com/in/innocent-nzimenyera)
- **GitHub**: [Innocent50](https://github.com/Innocent50)

## 🙏 Acknowledgments

- Bootstrap team for the excellent CSS framework
- Font Awesome for the beautiful icons
- AOS library for smooth animations
- Google Fonts for typography options

---

**Made with ❤️ by Innocent Nzimenyera**
