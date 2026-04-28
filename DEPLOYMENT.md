# 🚀 Deployment Guide

## Deploy to Railway (Easiest Method!)

Railway is the simplest way to deploy your Django app. It takes ~5 minutes!

### Step 1: Prepare Your Repository

Make sure everything is committed to git:
```bash
git add .
git commit -m "Prepare for production deployment"
git push
```

### Step 2: Create Railway Account

1. Go to: https://railway.app
2. Sign up (free with email or GitHub)
3. Create a new project

### Step 3: Connect Your GitHub Repository

1. Click "Deploy from GitHub"
2. Authorize Railway to access your GitHub
3. Select your `django-weather-app` repository
4. Click "Deploy"

### Step 4: Configure Environment Variables

Railway will automatically detect it's a Django app. Now add these variables:

1. In Railway dashboard, go to **Variables**
2. Add these environment variables:

```
WEATHER_API_KEY=5953976219dffcae0fbd84a9000e0d04
SECRET_KEY=your-secure-random-string-here
DEBUG=False
```

**To generate SECRET_KEY:**
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

Or use an online generator: https://djecrety.ir/

### Step 5: Deploy PostgreSQL Database

Railway will automatically provide PostgreSQL. Just:
1. Add PostgreSQL plugin in Railway dashboard
2. It will set `DATABASE_URL` automatically
3. Django will use PostgreSQL in production, SQLite locally

### Step 6: Auto-Deploy

Done! Railway will:
- ✅ Install dependencies from `requirements.txt`
- ✅ Run migrations (from Procfile: `python manage.py migrate`)
- ✅ Collect static files
- ✅ Start the Gunicorn server
- ✅ Give you a live URL

Your app will be live at: `https://your-app-name.up.railway.app` 🎉

---

## Alternative: Deploy to Render

### Step 1: Connect Repository
1. Go to: https://render.com
2. Sign up/ login
3. Click "New +" → "Web Service"
4. Connect your GitHub repo

### Step 2: Configure Settings
- **Name:** `django-weather-app`
- **Build command:** `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
- **Start command:** `gunicorn weatherproject.wsgi`
- **Plan:** Free tier available

### Step 3: Add Environment Variables
- `WEATHER_API_KEY=your-key`
- `SECRET_KEY=your-secret-key`
- `DEBUG=False`

### Step 4: Deploy
Click "Create Web Service" and wait ~5 minutes for deployment! 

---

## Alternative: Deploy to PythonAnywhere

### Step 1: Sign Up
Go to: https://www.pythonanywhere.com

### Step 2: Upload Code
Use their web interface or git clone your repository

### Step 3: Configure App
- Point to your Django project
- Set Python version to 3.13
- Configure virtual environment

### Step 4: Add Database
Use their PostgreSQL or MySQL integration

---

## Local Testing Before Deployment

Before deploying, test production settings locally:

```bash
# Install new dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Test with Gunicorn
gunicorn weatherproject.wsgi
```

Then visit: `http://127.0.0.1:8000`

---

## Post-Deployment

### 1. Test Your Live App
- Open your deployed URL
- Search for a city
- Check if API calls work
- Test admin panel

### 2. Set Custom Domain (Optional)
- Railway/Render will give you a domain
- Add your custom domain in settings
- Update `ALLOWED_HOSTS` in settings.py

### 3: Monitor Logs
- Railway: Dashboard → Logs
- Render: Dashboard → Logs
- Check for any errors

### 4: Add to README
Update your README.md with:
```markdown
## Live Demo
Visit: https://your-deployed-url.railway.app

## Deployment
Deployed on Railway. See [DEPLOYMENT.md](DEPLOYMENT.md) for details.
```

---

## If Deployment Fails

### Common Issues

**1. "ModuleNotFoundError"**
- Check `requirements.txt` has all packages
- Rebuild deployment

**2. "Database error"**
- Ensure PostgreSQL is added
- Check DATABASE_URL is set
- Run migrations manually if needed

**3. "Static files not loading"**
- Run `collectstatic` command
- Check STATIC_ROOT and STATIC_URL in settings

**4. "API key error"**
- Verify WEATHER_API_KEY environment variable is set
- Check it's active on OpenWeatherMap

**5. "502 Bad Gateway"**
- Check logs for errors
- Ensure Procfile is correctly configured
- Restart the web service

---

## Troubleshooting Commands

For Railway/Render SSH Access:
```bash
# View logs
railway logs

# SSH into container
railway shell

# Run Django shell
python manage.py shell

# View environment variables
env | grep WEATHER_API_KEY
```

---

## Scaling & Optimization

### For Heavy Traffic:
- Add Database replicas
- Use CDN for static files
- Add caching layer (Redis)
- Scale up server resources

### Monitor Performance:
- Check deployment dashboard
- Review error logs
- Monitor database queries
- Use Django Debug Toolbar (locally only!)

---

## Security Checklist

Before going live:

- ✅ `DEBUG = False` in production
- ✅ `SECRET_KEY` is unique and secure
- ✅ `ALLOWED_HOSTS` set to your domain
- ✅ API key not exposed in code
- ✅ HTTPS/SSL enabled (auto on Railway)
- ✅ Database backups enabled
- ✅ Error logging configured

---

## Additional Resources

- Railway Docs: https://docs.railway.app/
- Render Docs: https://render.com/docs
- Django Deployment: https://docs.djangoproject.com/en/stable/howto/deployment/
- Gunicorn: https://gunicorn.org/

---

## Support

If you encounter issues:
1. Check deployment platform's documentation
2. Review error logs carefully
3. Test locally first
4. Ask on Django community forums
5. Create an issue on your GitHub repository

**Your app is ready to go live! 🚀**
