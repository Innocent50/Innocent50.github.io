# Deployment Guide

## Environment Variables

Create a `.env` file in your root directory with the following variables:

```bash
FLASK_ENV=production
SECRET_KEY=your-secure-random-key-here
DEBUG=False

# Optional: Email configuration
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
CONTACT_EMAIL=your-email@example.com
```

## Deployment Options

### 1. Heroku Deployment

1. **Install Heroku CLI**
2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Create a new Heroku app**
   ```bash
   heroku create your-portfolio-name
   ```

4. **Set environment variables**
   ```bash
   heroku config:set FLASK_ENV=production
   heroku config:set SECRET_KEY=your-secure-key
   heroku config:set DEBUG=False
   ```

5. **Deploy**
   ```bash
   git add .
   git commit -m "Deploy to Heroku"
   git push heroku main
   ```

### 2. PythonAnywhere Deployment

1. **Upload files** to your PythonAnywhere account
2. **Install requirements** in a virtual environment
3. **Configure WSGI** file:
   ```python
   import sys
   path = '/home/yourusername/portfolio'
   if path not in sys.path:
       sys.path.append(path)
   
   from app import app as application
   ```

### 3. DigitalOcean App Platform

1. **Connect your GitHub repository**
2. **Configure build settings**:
   - Build Command: `pip install -r requirements.txt`
   - Run Command: `gunicorn app:app`
3. **Set environment variables** in the dashboard
4. **Deploy**

### 4. Railway Deployment

1. **Connect your GitHub repository**
2. **Railway will auto-detect** Flask application
3. **Set environment variables** in dashboard
4. **Deploy automatically** on push

### 5. Vercel Deployment

1. **Install Vercel CLI**
   ```bash
   npm i -g vercel
   ```

2. **Create vercel.json**:
   ```json
   {
     "builds": [
       {
         "src": "app.py",
         "use": "@vercel/python"
       }
     ],
     "routes": [
       {
         "src": "/(.*)",
         "dest": "app.py"
       }
     ]
   }
   ```

3. **Deploy**
   ```bash
   vercel
   ```

## Pre-deployment Checklist

- [ ] Update personal information in `app.py`
- [ ] Replace placeholder images with your own
- [ ] Test contact form functionality
- [ ] Set secure SECRET_KEY
- [ ] Configure email settings (if using contact form)
- [ ] Update social media links
- [ ] Test on different devices and browsers
- [ ] Optimize images for web
- [ ] Set up analytics (Google Analytics, etc.)
- [ ] Configure custom domain (if desired)

## Post-deployment Tasks

- [ ] Test all functionality on production
- [ ] Set up monitoring and error tracking
- [ ] Configure backups (if using database)
- [ ] Set up SSL certificate
- [ ] Submit to search engines
- [ ] Share your portfolio URL!
