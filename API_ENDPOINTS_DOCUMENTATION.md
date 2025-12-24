# AI Brick Cement Chatbot - REST API Documentation

## Overview

This document provides comprehensive documentation for all REST API endpoints in the AI Brick Cement Chatbot system. The API follows RESTful principles and returns JSON responses with consistent error handling.

## Base URL
```
http://localhost:5000/api
```

## Authentication
Currently, the API uses customer_id parameter for user identification. In production, implement proper JWT authentication.

## Response Format

### Success Response
```json
{
  "data": {...},
  "timestamp": "2024-01-01T12:00:00Z"
}
```

### Error Response
```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human readable error message",
    "timestamp": "2024-01-01T12:00:00Z"
  }
}
```

## Chat Endpoints

### POST /api/chat/message
Send a message to the AI chatbot.

**Request Body:**
```json
{
  "user_id": "customer_123",
  "message": "I need 1000 bricks for my house",
  "language": "en",
  "context": {
    "location": "Gurgaon",
    "project_type": "residential"
  }
}
```

**Response:**
```json
{
  "response": "I can help you with bricks for your house...",
  "conversation_id": "conv_123",
  "recommendations": [...],
  "timestamp": "2024-01-01T12:00:00Z"
}
```

### GET /api/chat/history/{user_id}
Get conversation history for a user.

**Parameters:**
- `limit` (optional): Number of conversations to return (default: 20)

**Response:**
```json
{
  "conversations": [...],
  "total": 50,
  "user_id": "customer_123",
  "timestamp": "2024-01-01T12:00:00Z"
}
```

## Product Endpoints

### GET /api/products
Get list of products with filtering and pagination.

**Query Parameters:**
- `category`: Product category (brick, cement)
- `type`: Product type (fly_ash, red_clay, etc.)
- `brand`: Product brand
- `stock_status`: Stock status filter
- `search`: Search query
- `customer_id`: For customer-specific pricing
- `page`: Page number (default: 1)
- `per_page`: Items per page (default: 20, max: 100)

**Response:**
```json
{
  "products": [
    {
      "id": "prod_123",
      "name": "Premium Fly Ash Bricks",
      "category": "brick",
      "type": "fly_ash",
      "brand": "BuildMate",
      "price_per_unit": 8.50,
      "customer_price": 7.65,
      "discount_percentage": 10,
      "stock_status": "in_stock",
      "stock_quantity": 5000
    }
  ],
  "total": 150,
  "page": 1,
  "per_page": 20,
  "has_next": true,
  "timestamp": "2024-01-01T12:00:00Z"
}
```

### GET /api/products/{product_id}
Get detailed product information.

**Query Parameters:**
- `customer_id` (optional): For customer-specific pricing

**Response:**
```json
{
  "id": "prod_123",
  "name": "Premium Fly Ash Bricks",
  "category": "brick",
  "specifications": {
    "compressive_strength": "7.5 MPa",
    "water_absorption": "12%",
    "dimensions": "230x110x75 mm"
  },
  "customer_pricing": {
    "customer_price": 7.65,
    "discount_percentage": 10,
    "user_type": "contractor"
  },
  "bulk_pricing_tiers": [
    {
      "min_quantity": 1000,
      "max_quantity": 4999,
      "price_per_unit": 7.65,
      "discount_percentage": 10
    }
  ],
  "timestamp": "2024-01-01T12:00:00Z"
}
```

### GET /api/products/categories
Get available product categories and types.

**Response:**
```json
{
  "categories": [
    {
      "value": "brick",
      "label": "Bricks",
      "types": [
        {"value": "fly_ash", "label": "Fly Ash Bricks"},
        {"value": "red_clay", "label": "Red Clay Bricks"}
      ]
    }
  ],
  "is_standards": [...],
  "stock_statuses": [...],
  "timestamp": "2024-01-01T12:00:00Z"
}
```

### POST /api/pricing/calculate
Calculate pricing for multiple items.

**Request Body:**
```json
{
  "customer_id": "customer_123",
  "items": [
    {
      "product_id": "prod_123",
      "quantity": 1000
    }
  ]
}
```

**Response:**
```json
{
  "customer_id": "customer_123",
  "user_type": "contractor",
  "items": [
    {
      "product_id": "prod_123",
      "quantity": 1000,
      "unit_price": 8.50,
      "customer_price": 7.65,
      "total_price": 7650.00,
      "savings": 850.00
    }
  ],
  "pricing_summary": {
    "subtotal": 7650.00,
    "total_savings": 850.00,
    "final_total": 7650.00,
    "tax_amount": 1377.00,
    "grand_total": 9027.00
  },
  "timestamp": "2024-01-01T12:00:00Z"
}
```

### GET /api/stock
Get stock information.

**Query Parameters:**
- `product_id`: Specific product stock
- `status`: Filter by status (low_stock, out_of_stock)
- `threshold`: Low stock threshold (default: 100)

**Response:**
```json
{
  "status": "low_stock",
  "threshold": 100,
  "products": [
    {
      "product_id": "prod_123",
      "product_name": "Premium Fly Ash Bricks",
      "stock_quantity": 50,
      "stock_status": "limited"
    }
  ],
  "total_products": 5,
  "timestamp": "2024-01-01T12:00:00Z"
}
```

### GET /api/pricing/bulk/{customer_id}/{product_id}
Get bulk pricing tiers for specific customer and product.

**Response:**
```json
{
  "customer_id": "customer_123",
  "product_id": "prod_123",
  "user_type": "contractor",
  "base_price": 8.50,
  "pricing_tiers": [
    {
      "min_quantity": 1000,
      "max_quantity": 4999,
      "price_per_unit": 7.65,
      "discount_percentage": 10
    }
  ],
  "timestamp": "2024-01-01T12:00:00Z"
}
```

## Order Endpoints

### POST /api/orders
Create a new order.

**Request Body:**
```json
{
  "customer_id": "customer_123",
  "items": [
    {
      "product_id": "prod_123",
      "quantity": 1000
    }
  ],
  "delivery_address": {
    "street": "123 Main St",
    "city": "Gurgaon",
    "state": "Haryana",
    "pincode": "122001",
    "coordinates": [28.4595, 77.0266]
  },
  "special_instructions": "Deliver in morning hours"
}
```

**Response:**
```json
{
  "success": true,
  "order_id": "BCO20240101ABC123",
  "order_details": {
    "id": "BCO20240101ABC123",
    "status": "pending",
    "total_amount": 9027.00
  },
  "estimated_delivery": "2024-01-05T10:00:00Z",
  "pdf_url": "gs://order-pdfs/BCO20240101ABC123_summary.pdf",
  "timestamp": "2024-01-01T12:00:00Z"
}
```

### GET /api/orders
Get list of orders for a customer.

**Query Parameters:**
- `customer_id` (required): Customer identifier
- `status` (optional): Filter by order status
- `page`: Page number (default: 1)
- `per_page`: Items per page (default: 20)

**Response:**
```json
{
  "orders": [
    {
      "id": "BCO20240101ABC123",
      "status": "pending",
      "order_date": "2024-01-01T12:00:00Z",
      "total_amount": 9027.00,
      "items_count": 1
    }
  ],
  "total": 10,
  "page": 1,
  "has_next": false,
  "timestamp": "2024-01-01T12:00:00Z"
}
```

### GET /api/orders/{order_id}
Get detailed order information.

**Response:**
```json
{
  "id": "BCO20240101ABC123",
  "customer_id": "customer_123",
  "status": "pending",
  "order_date": "2024-01-01T12:00:00Z",
  "delivery_address": {...},
  "items": [
    {
      "product_id": "prod_123",
      "product_name": "Premium Fly Ash Bricks",
      "quantity": 1000,
      "unit_price": 7.65,
      "total_price": 7650.00
    }
  ],
  "subtotal": 7650.00,
  "delivery_charge": 500.00,
  "tax_amount": 1377.00,
  "total_amount": 9027.00,
  "status_history": [...],
  "timestamp": "2024-01-01T12:00:00Z"
}
```

### PUT /api/orders/{order_id}
Update order status.

**Request Body:**
```json
{
  "status": "confirmed",
  "notes": "Order confirmed by admin",
  "updated_by": "admin_user"
}
```

**Response:**
```json
{
  "success": true,
  "order_id": "BCO20240101ABC123",
  "previous_status": "pending",
  "new_status": "confirmed",
  "updated_at": "2024-01-01T13:00:00Z"
}
```

### DELETE /api/orders/{order_id}
Cancel an order.

**Request Body:**
```json
{
  "reason": "Customer request",
  "cancelled_by": "customer_123"
}
```

### GET /api/orders/statistics
Get order statistics.

**Query Parameters:**
- `days`: Number of days to analyze (default: 30)

**Response:**
```json
{
  "statistics": {
    "total_orders": 150,
    "period_days": 30,
    "revenue_statistics": {
      "total_revenue": 450000.00,
      "average_order_value": 3000.00
    },
    "completion_rate": 85.5,
    "cancellation_rate": 5.2
  },
  "timestamp": "2024-01-01T12:00:00Z"
}
```

## Delivery Endpoints

### POST /api/delivery/calculate
Calculate delivery information.

**Request Body:**
```json
{
  "delivery_address": {
    "city": "Gurgaon",
    "state": "Haryana",
    "pincode": "122001",
    "distance_km": 15
  },
  "order_items": [
    {
      "product_id": "prod_123",
      "quantity": 1000,
      "weight": 2500
    }
  ],
  "order_value": 7650.00
}
```

**Response:**
```json
{
  "delivery_charges": {
    "base_charge": 300.00,
    "distance_charge": 200.00,
    "total_charge": 500.00
  },
  "vehicle_suggestion": {
    "recommended_vehicle": "truck",
    "capacity_utilization": 75,
    "multiple_trips_needed": false
  },
  "estimated_delivery": {
    "estimated_hours": 24,
    "delivery_date": "2024-01-02T12:00:00Z"
  },
  "timestamp": "2024-01-01T12:00:00Z"
}
```

## Quality Assessment Endpoints

### POST /api/quality/assess
Analyze brick quality from uploaded image.

**Request (multipart/form-data):**
- `image`: Image file (required)
- `customer_id`: Customer identifier (optional)
- `product_type`: Product type (default: "brick")

**Response:**
```json
{
  "assessment_id": "qa_123",
  "image_url": "gs://quality-images/qa_123.jpg",
  "overall_score": 8.5,
  "grade": "A",
  "defects": [
    {
      "type": "minor_crack",
      "severity": "low",
      "confidence": 0.85,
      "location": {"x": 150, "y": 200},
      "description": "Small surface crack detected"
    }
  ],
  "analysis_details": {
    "color_uniformity": 8.2,
    "surface_quality": 8.8,
    "size_consistency": 8.5
  },
  "recommendations": {
    "overall_recommendation": "APPROVED - Good quality for construction",
    "suitable_applications": ["Load bearing walls", "Partition walls"],
    "improvement_suggestions": ["Monitor crack development"]
  },
  "timestamp": "2024-01-01T12:00:00Z"
}
```

### GET /api/quality/history/{customer_id}
Get quality assessment history for a customer.

**Query Parameters:**
- `limit`: Number of assessments to return (default: 20)

**Response:**
```json
{
  "customer_id": "customer_123",
  "assessments": [
    {
      "assessment_id": "qa_123",
      "overall_score": 8.5,
      "grade": "A",
      "analyzed_at": "2024-01-01T12:00:00Z"
    }
  ],
  "total_assessments": 5,
  "timestamp": "2024-01-01T12:00:00Z"
}
```

## Admin Endpoints

### GET /api/admin/dashboard
Get comprehensive admin dashboard data.

**Query Parameters:**
- `days`: Analysis period in days (default: 7)

**Response:**
```json
{
  "period_days": 7,
  "daily_orders": {
    "count": 25,
    "revenue": 75000.00,
    "average_order_value": 3000.00
  },
  "customer_analytics": {
    "total_customers": 500,
    "new_customers_period": 15,
    "active_customers": 120,
    "vip_customers": 25
  },
  "popular_products": [...],
  "support_metrics": {
    "open_tickets": 8,
    "resolved_today": 12,
    "average_resolution_time": 4.5,
    "customer_satisfaction": 4.2
  },
  "quality_metrics": {
    "assessments_count": 45,
    "average_quality_score": 8.2,
    "defect_rate": 15.5
  },
  "timestamp": "2024-01-01T12:00:00Z"
}
```

### GET /api/admin/products
Get product inventory analytics.

**Query Parameters:**
- `low_stock_threshold`: Threshold for low stock alert (default: 100)

**Response:**
```json
{
  "inventory_summary": {
    "total_products": 50,
    "low_stock_count": 5,
    "out_of_stock_count": 2
  },
  "low_stock_products": [...],
  "out_of_stock_products": [...],
  "popular_products": [...],
  "timestamp": "2024-01-01T12:00:00Z"
}
```

### GET /api/admin/orders
Get order analytics for admin.

**Query Parameters:**
- `days`: Analysis period (default: 30)

**Response:**
```json
{
  "period_days": 30,
  "order_analytics": {...},
  "revenue_trends": {
    "total_revenue": 450000.00,
    "daily_average": 15000.00,
    "highest_order": 25000.00
  },
  "performance_metrics": {
    "completion_rate": 85.5,
    "cancellation_rate": 5.2,
    "orders_per_day": 5.2
  },
  "timestamp": "2024-01-01T12:00:00Z"
}
```

### GET /api/admin/customers
Get customer analytics.

**Response:**
```json
{
  "customer_overview": {...},
  "customer_segments": {...},
  "growth_metrics": {
    "total_customers": 500,
    "new_customers": 15,
    "retention_rate": 78.5
  },
  "value_distribution": {
    "vip_customers": 25,
    "bulk_customers": 45,
    "frequent_customers": 120
  },
  "timestamp": "2024-01-01T12:00:00Z"
}
```

### GET /api/admin/support
Get support ticket analytics.

**Query Parameters:**
- `days`: Analysis period (default: 30)

**Response:**
```json
{
  "period_days": 30,
  "support_overview": {...},
  "ticket_metrics": {
    "total_tickets": 150,
    "open_tickets": 8,
    "resolved_tickets": 142
  },
  "performance_metrics": {
    "average_resolution_time": 4.5,
    "customer_satisfaction": 4.2,
    "sla_compliance": 92.5
  },
  "timestamp": "2024-01-01T12:00:00Z"
}
```

### GET /api/admin/campaigns
Get campaign analytics.

**Response:**
```json
{
  "campaign_overview": {...},
  "performance_metrics": {
    "total_campaigns": 12,
    "active_count": 3,
    "conversion_rate": 15.5
  },
  "roi_metrics": {
    "total_revenue": 125000.00,
    "total_cost": 25000.00,
    "roi_percentage": 400.0
  },
  "timestamp": "2024-01-01T12:00:00Z"
}
```

### POST /api/admin/campaigns
Create a new marketing campaign.

**Request Body:**
```json
{
  "name": "Diwali Special Offer",
  "type": "seasonal",
  "target_audience": "all_customers",
  "message": "Special Diwali discount on all products!",
  "discount_percentage": 15,
  "start_date": "2024-10-20",
  "end_date": "2024-11-05",
  "created_by": "admin_user"
}
```

**Response:**
```json
{
  "success": true,
  "campaign_id": "camp_123",
  "campaign_details": {...},
  "timestamp": "2024-01-01T12:00:00Z"
}
```

## Error Codes

| Code | Description |
|------|-------------|
| `MISSING_REQUIRED_FIELD` | Required field is missing from request |
| `INVALID_STATUS` | Invalid order status provided |
| `PRODUCT_NOT_FOUND` | Product with given ID not found |
| `ORDER_NOT_FOUND` | Order with given ID not found |
| `INSUFFICIENT_STOCK` | Not enough stock available |
| `PRICING_CALCULATION_ERROR` | Error calculating pricing |
| `ORDER_CREATION_ERROR` | Error creating order |
| `QUALITY_ASSESSMENT_ERROR` | Error analyzing image quality |
| `DELIVERY_CALCULATION_ERROR` | Error calculating delivery info |
| `ADMIN_DASHBOARD_ERROR` | Error retrieving admin data |

## Rate Limiting

- Chat endpoints: 60 requests per minute per user
- Order creation: 10 requests per minute per user
- Quality assessment: 20 requests per minute per user
- Admin endpoints: 100 requests per minute per admin user

## Testing

Use the provided test data and endpoints to verify functionality:

```bash
# Test product listing
curl -X GET "http://localhost:5000/api/products?category=brick&customer_id=test_customer"

# Test order creation
curl -X POST "http://localhost:5000/api/orders" \
  -H "Content-Type: application/json" \
  -d '{"customer_id":"test_customer","items":[{"product_id":"test_product","quantity":100}],"delivery_address":{"city":"Gurgaon","state":"Haryana","pincode":"122001"}}'

# Test chat
curl -X POST "http://localhost:5000/api/chat/message" \
  -H "Content-Type: application/json" \
  -d '{"user_id":"test_user","message":"I need bricks for construction","language":"en"}'
```

## Production Considerations

1. **Authentication**: Implement JWT-based authentication
2. **Rate Limiting**: Add Redis-based rate limiting
3. **Caching**: Cache frequently accessed data
4. **Monitoring**: Add comprehensive logging and monitoring
5. **Validation**: Add request validation middleware
6. **Documentation**: Generate OpenAPI/Swagger documentation
7. **Testing**: Add comprehensive API tests
8. **Security**: Add HTTPS, input sanitization, and security headers