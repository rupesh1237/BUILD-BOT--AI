# AI Brick Cement Chatbot - Deployment Guide

## Overview
This guide provides step-by-step instructions for deploying the AI Brick Cement Chatbot system to production.

## Prerequisites

### 1. Google Cloud Platform Setup
```bash
# Install Google Cloud SDK
curl https://sdk.cloud.google.com | bash
exec -l $SHELL

# Authenticate and set project
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
```

### 2. Required Services
Enable the following Google Cloud APIs:
- Vertex AI API
- Vision API
- Translation API
- Speech-to-Text API
- Maps API
- Firestore API

### 3. Service Account Setup
```bash
# Create service account
gcloud iam service-accounts create brick-cement-chatbot

# Grant necessary roles
gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
    --member="serviceAccount:brick-cement-chatbot@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/aiplatform.user"

gcloud projects add-iam-policy-binding YOUR_PROJECT_ID \
    --member="serviceAccount:brick-cement-chatbot@YOUR_PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/vision.admin"

# Create and download key
gcloud iam service-accounts keys create service-account-key.json \
    --iam-account=brick-cement-chatbot@YOUR_PROJECT_ID.iam.gserviceaccount.com
```

## Environment Configuration

### 1. Environment Variables
Create a `.env` file based on `.env.example`:

```bash
# Flask Configuration
FLASK_ENV=production
SECRET_KEY=your-secret-key-here

# Google Cloud Configuration
GOOGLE_APPLICATION_CREDENTIALS=path/to/service-account-key.json
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_CLOUD_LOCATION=us-central1

# Firebase Configuration
FIREBASE_PROJECT_ID=your-project-id

# Twilio WhatsApp Configuration
TWILIO_ACCOUNT_SID=your-twilio-account-sid
TWILIO_AUTH_TOKEN=your-twilio-auth-token
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886

# Redis Configuration (optional)
REDIS_URL=redis://localhost:6379

# Application Configuration
PORT=8080
```

### 2. Firebase Setup
```bash
# Install Firebase CLI
npm install -g firebase-tools

# Login and initialize
firebase login
firebase init firestore

# Deploy Firestore rules
firebase deploy --only firestore:rules
```

## Local Development Setup

### 1. Python Environment
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run Application
```bash
# Development mode
python app.py

# Production mode with Gunicorn
gunicorn --bind 0.0.0.0:8080 --workers 4 app:app
```

## Docker Deployment

### 1. Build Docker Image
```dockerfile
# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "4", "app:app"]
```

```bash
# Build and run
docker build -t brick-cement-chatbot .
docker run -p 8080:8080 --env-file .env brick-cement-chatbot
```

### 2. Docker Compose
```yaml
# docker-compose.yml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8080:8080"
    env_file:
      - .env
    depends_on:
      - redis
    
  redis:
    image: redis:alpine
    ports:
      - "6379:6379"
```

## Google Cloud Platform Deployment

### 1. Cloud Run Deployment
```bash
# Build and deploy to Cloud Run
gcloud run deploy brick-cement-chatbot \
    --source . \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated \
    --set-env-vars GOOGLE_CLOUD_PROJECT=YOUR_PROJECT_ID
```

### 2. App Engine Deployment
```yaml
# app.yaml
runtime: python39

env_variables:
  GOOGLE_CLOUD_PROJECT: your-project-id
  FLASK_ENV: production

automatic_scaling:
  min_instances: 1
  max_instances: 10
```

```bash
# Deploy to App Engine
gcloud app deploy
```

### 3. Kubernetes Deployment
```yaml
# kubernetes-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: brick-cement-chatbot
spec:
  replicas: 3
  selector:
    matchLabels:
      app: brick-cement-chatbot
  template:
    metadata:
      labels:
        app: brick-cement-chatbot
    spec:
      containers:
      - name: app
        image: gcr.io/YOUR_PROJECT_ID/brick-cement-chatbot
        ports:
        - containerPort: 8080
        env:
        - name: GOOGLE_CLOUD_PROJECT
          value: "YOUR_PROJECT_ID"
---
apiVersion: v1
kind: Service
metadata:
  name: brick-cement-chatbot-service
spec:
  selector:
    app: brick-cement-chatbot
  ports:
  - port: 80
    targetPort: 8080
  type: LoadBalancer
```

## Database Setup

### 1. Firestore Collections
The application will automatically create the following collections:
- `products` - Product catalog
- `customers` - Customer profiles
- `orders` - Order data
- `conversations` - Chat history
- `quality_assessments` - Quality analysis results
- `support_tickets` - Customer support tickets

### 2. Sample Data
```bash
# Run data seeding script
python -c "
from app.services.product_service import ProductService
from app import create_app

app = create_app()
with app.app_context():
    service = ProductService(app.db)
    service.seed_sample_products()
"
```

## WhatsApp Integration Setup

### 1. Twilio WhatsApp Setup
1. Create Twilio account
2. Set up WhatsApp Business API
3. Configure webhook URL: `https://your-domain.com/api/whatsapp/webhook`
4. Add phone numbers to WhatsApp sandbox (development)

### 2. Production WhatsApp
1. Apply for WhatsApp Business API approval
2. Complete business verification
3. Configure production webhook
4. Update environment variables with production credentials

## Monitoring and Logging

### 1. Google Cloud Logging
```python
# Add to app/__init__.py
import google.cloud.logging

client = google.cloud.logging.Client()
client.setup_logging()
```

### 2. Health Check Endpoint
```python
# Add to app.py
@app.route('/health')
def health_check():
    return {'status': 'healthy', 'timestamp': datetime.utcnow().isoformat()}
```

### 3. Performance Monitoring
```bash
# Install monitoring dependencies
pip install google-cloud-monitoring
```

## Security Configuration

### 1. HTTPS Setup
```bash
# For Cloud Run, HTTPS is automatic
# For custom domains, configure SSL certificate
gcloud compute ssl-certificates create brick-cement-ssl \
    --domains your-domain.com
```

### 2. Firestore Security Rules
```javascript
// firestore.rules
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Products are readable by all, writable by admin
    match /products/{productId} {
      allow read: if true;
      allow write: if request.auth != null && request.auth.token.admin == true;
    }
    
    // Customers can only access their own data
    match /customers/{customerId} {
      allow read, write: if request.auth != null && request.auth.uid == customerId;
    }
    
    // Orders are accessible by owner and admin
    match /orders/{orderId} {
      allow read, write: if request.auth != null && 
        (resource.data.customer_id == request.auth.uid || request.auth.token.admin == true);
    }
  }
}
```

## Performance Optimization

### 1. Caching Strategy
```python
# Redis caching for frequently accessed data
import redis
r = redis.from_url(os.getenv('REDIS_URL', 'redis://localhost:6379'))

# Cache product data
def get_cached_products():
    cached = r.get('products')
    if cached:
        return json.loads(cached)
    
    products = ProductService.get_all_products()
    r.setex('products', 300, json.dumps(products))  # 5 minute cache
    return products
```

### 2. Database Optimization
```bash
# Create Firestore indexes
gcloud firestore indexes composite create \
    --collection-group=products \
    --field-config field-path=category,order=ascending \
    --field-config field-path=price,order=ascending
```

## Backup and Recovery

### 1. Firestore Backup
```bash
# Schedule daily backups
gcloud firestore export gs://your-backup-bucket/firestore-backup-$(date +%Y%m%d)
```

### 2. Application Backup
```bash
# Backup application code and configuration
tar -czf backup-$(date +%Y%m%d).tar.gz app/ templates/ static/ requirements.txt
```

## Testing in Production

### 1. Health Checks
```bash
# Test application health
curl https://your-domain.com/health

# Test API endpoints
curl https://your-domain.com/api/products
```

### 2. WhatsApp Testing
1. Send test message to WhatsApp number
2. Verify webhook receives message
3. Test complete conversation flow

## Troubleshooting

### Common Issues

1. **Google Cloud Authentication**
   ```bash
   # Verify service account permissions
   gcloud auth activate-service-account --key-file=service-account-key.json
   ```

2. **Firestore Connection**
   ```bash
   # Test Firestore connection
   python -c "from google.cloud import firestore; db = firestore.Client(); print('Connected')"
   ```

3. **WhatsApp Webhook**
   ```bash
   # Test webhook endpoint
   curl -X POST https://your-domain.com/api/whatsapp/webhook \
        -H "Content-Type: application/json" \
        -d '{"test": "message"}'
   ```

### Logs and Debugging
```bash
# View Cloud Run logs
gcloud logs read --service=brick-cement-chatbot --limit=50

# View App Engine logs
gcloud app logs tail -s default
```

## Scaling Considerations

### 1. Auto Scaling
- Cloud Run: Automatic scaling based on requests
- App Engine: Configure automatic scaling in app.yaml
- Kubernetes: Horizontal Pod Autoscaler

### 2. Database Scaling
- Firestore: Automatic scaling
- Consider read replicas for heavy read workloads
- Implement connection pooling

### 3. Caching
- Redis for session management
- CDN for static assets
- Application-level caching for expensive operations

## Maintenance

### 1. Regular Updates
```bash
# Update dependencies
pip list --outdated
pip install --upgrade package-name

# Update Docker image
docker build -t brick-cement-chatbot:latest .
```

### 2. Monitoring
- Set up alerts for error rates
- Monitor response times
- Track API usage and costs

### 3. Backup Verification
- Regularly test backup restoration
- Verify data integrity
- Update disaster recovery procedures

## Support and Documentation

### 1. API Documentation
- Available at `/api/docs` (if Swagger is enabled)
- Postman collection for testing
- Integration examples

### 2. User Documentation
- Admin dashboard user guide
- WhatsApp integration guide
- Troubleshooting FAQ

### 3. Developer Documentation
- Code architecture overview
- Service integration guides
- Extension and customization guides

---

**Deployment Status**: Ready for Production  
**Last Updated**: December 24, 2024  
**Version**: 1.0.0