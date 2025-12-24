# Admin API Endpoints Documentation

## Overview

This document provides comprehensive documentation for all administrative API endpoints in the AI Brick Cement Chatbot system. These endpoints are designed for admin users to manage inventory, orders, customers, support tickets, and campaigns.

## Base URL
```
http://localhost:5000/api/admin
```

## Authentication
Admin endpoints require proper authentication and authorization. In production, implement JWT-based authentication with admin role verification.

## Admin Dashboard Endpoints

### GET /api/admin/dashboard
Get comprehensive admin dashboard analytics.

**Query Parameters:**
- `days` (optional): Analysis period in days (default: 7)

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
  "popular_products": [
    {
      "id": "prod_123",
      "name": "Premium Fly Ash Bricks",
      "category": "brick",
      "sales_count": 150,
      "revenue": 12750.00
    }
  ],
  "order_statistics": {
    "completion_rate": 85.5,
    "cancellation_rate": 5.2,
    "orders_per_day": 3.6,
    "status_distribution": {
      "pending": 5,
      "confirmed": 8,
      "shipped": 10,
      "delivered": 20
    }
  },
  "support_metrics": {
    "open_tickets": 8,
    "resolved_today": 12,
    "average_resolution_time": 4.5,
    "customer_satisfaction": 4.2
  },
  "quality_metrics": {
    "assessments_count": 45,
    "average_quality_score": 8.2,
    "defect_rate": 15.5,
    "grade_distribution": {
      "A": 60,
      "B": 30,
      "C": 10
    }
  },
  "timestamp": "2024-01-01T12:00:00Z"
}
```

## Product Management Endpoints

### GET /api/admin/products
Get product inventory analytics and overview.

**Query Parameters:**
- `low_stock_threshold` (optional): Threshold for low stock alert (default: 100)

**Response:**
```json
{
  "inventory_summary": {
    "total_products": 50,
    "low_stock_count": 5,
    "out_of_stock_count": 2,
    "low_stock_threshold": 100
  },
  "low_stock_products": [
    {
      "id": "prod_123",
      "name": "Premium Fly Ash Bricks",
      "category": "brick",
      "stock_quantity": 75,
      "stock_status": "limited",
      "reorder_needed": true
    }
  ],
  "out_of_stock_products": [
    {
      "id": "prod_456",
      "name": "Red Clay Bricks",
      "category": "brick",
      "stock_quantity": 0,
      "stock_status": "out_of_stock"
    }
  ],
  "popular_products": [
    {
      "id": "prod_789",
      "name": "OPC 53 Grade Cement",
      "category": "cement",
      "stock_quantity": 1000,
      "price_per_unit": 350.00,
      "sales_performance": 200
    }
  ],
  "timestamp": "2024-01-01T12:00:00Z"
}
```

### PUT /api/admin/products/{product_id}
Update product information.

**Request Body:**
```json
{
  "price_per_unit": 8.75,
  "stock_quantity": 2000,
  "bulk_discount_percentage": 7.5,
  "description": "Updated premium fly ash bricks description"
}
```

**Response:**
```json
{
  "success": true,
  "product_id": "prod_123",
  "updated_fields": ["price_per_unit", "stock_quantity", "bulk_discount_percentage"],
  "timestamp": "2024-01-01T12:00:00Z"
}
```

### POST /api/admin/stock
Update stock levels for products.

**Request Body:**
```json
{
  "product_id": "prod_123",
  "quantity": 500,
  "operation": "add",
  "reason": "New stock arrival"
}
```

**Operations:**
- `add`: Add stock to current level
- `subtract`: Remove stock from current level
- `set`: Set stock to specific level

**Response:**
```json
{
  "success": true,
  "product_id": "prod_123",
  "operation": "add",
  "quantity": 500,
  "new_stock_level": 1500,
  "timestamp": "2024-01-01T12:00:00Z"
}
```

## Order Management Endpoints

### GET /api/admin/orders
Get order analytics and performance metrics.

**Query Parameters:**
- `days` (optional): Analysis period in days (default: 30)

**Response:**
```json
{
  "period_days": 30,
  "order_analytics": {
    "total_orders": 150,
    "revenue_statistics": {
      "total_revenue": 450000.00,
      "average_order_value": 3000.00,
      "highest_order_value": 25000.00,
      "lowest_order_value": 500.00
    }
  },
  "revenue_trends": {
    "total_revenue": 450000.00,
    "daily_average": 15000.00,
    "highest_order": 25000.00,
    "lowest_order": 500.00
  },
  "performance_metrics": {
    "completion_rate": 85.5,
    "cancellation_rate": 5.2,
    "orders_per_day": 5.0,
    "customer_satisfaction": 4.2
  },
  "status_breakdown": {
    "pending": 10,
    "confirmed": 25,
    "processing": 15,
    "shipped": 30,
    "delivered": 65,
    "cancelled": 5
  },
  "timestamp": "2024-01-01T12:00:00Z"
}
```

### GET /api/admin/orders/manage
Get all orders for admin management view.

**Query Parameters:**
- `status` (optional): Filter by order status
- `start_date` (optional): Filter orders from date (YYYY-MM-DD)
- `end_date` (optional): Filter orders to date (YYYY-MM-DD)
- `page` (optional): Page number (default: 1)
- `per_page` (optional): Items per page (default: 50, max: 100)

**Response:**
```json
{
  "orders": [
    {
      "id": "BCO20240101ABC123",
      "customer_id": "customer_123",
      "status": "pending",
      "order_date": "2024-01-01T12:00:00Z",
      "total_amount": 9027.00,
      "items_count": 2
    }
  ],
  "total": 150,
  "page": 1,
  "per_page": 50,
  "filters": {
    "status": "pending",
    "start_date": "2024-01-01",
    "end_date": "2024-01-31"
  },
  "timestamp": "2024-01-01T12:00:00Z"
}
```

## Customer Management Endpoints

### GET /api/admin/customers
Get customer analytics and segmentation data.

**Response:**
```json
{
  "customer_overview": {
    "total_customers": 500,
    "new_customers_count": 25,
    "active_customers": 120,
    "retention_rate": 78.5
  },
  "customer_segments": {
    "individual": 300,
    "contractor": 150,
    "dealer": 50
  },
  "growth_metrics": {
    "total_customers": 500,
    "new_customers": 25,
    "active_customers": 120,
    "retention_rate": 78.5
  },
  "value_distribution": {
    "vip_customers": 25,
    "bulk_customers": 75,
    "frequent_customers": 150,
    "regular_customers": 250
  },
  "timestamp": "2024-01-01T12:00:00Z"
}
```

### GET /api/admin/customers/{customer_id}
Get detailed customer information and analytics.

**Response:**
```json
{
  "customer_profile": {
    "id": "customer_123",
    "name": "John Doe",
    "user_type": "contractor",
    "registration_date": "2023-06-15T10:30:00Z",
    "last_activity": "2024-01-01T09:15:00Z"
  },
  "analytics": {
    "order_analytics": {
      "total_orders": 15,
      "total_spent": 45000.00,
      "average_order_value": 3000.00,
      "last_order_date": "2023-12-28T14:20:00Z"
    },
    "engagement_metrics": {
      "chat_sessions": 25,
      "quality_assessments": 8,
      "support_tickets": 2
    },
    "loyalty_metrics": {
      "loyalty_points": 4500,
      "tier": "gold",
      "referrals": 3
    }
  },
  "timestamp": "2024-01-01T12:00:00Z"
}
```

### PUT /api/admin/customers/{customer_id}
Update customer profile information.

**Request Body:**
```json
{
  "user_type": "dealer",
  "tier": "platinum",
  "notes": "Upgraded to dealer status due to high volume orders"
}
```

**Response:**
```json
{
  "success": true,
  "customer_id": "customer_123",
  "updated_fields": ["user_type", "tier", "notes"],
  "timestamp": "2024-01-01T12:00:00Z"
}
```

## Support Management Endpoints

### GET /api/admin/support
Get support ticket analytics and performance metrics.

**Query Parameters:**
- `days` (optional): Analysis period in days (default: 30)

**Response:**
```json
{
  "period_days": 30,
  "support_overview": {
    "total_tickets": 150,
    "open_tickets": 8,
    "resolved_period": 142,
    "escalated_tickets": 5
  },
  "ticket_metrics": {
    "total_tickets": 150,
    "open_tickets": 8,
    "resolved_tickets": 142,
    "escalated_tickets": 5
  },
  "performance_metrics": {
    "average_resolution_time": 4.5,
    "first_response_time": 0.8,
    "customer_satisfaction": 4.2,
    "sla_compliance": 92.5
  },
  "category_breakdown": {
    "delivery_issue": 45,
    "quality_complaint": 30,
    "billing_inquiry": 25,
    "product_information": 35,
    "technical_support": 15
  },
  "priority_breakdown": {
    "low": 60,
    "medium": 70,
    "high": 15,
    "critical": 5
  },
  "timestamp": "2024-01-01T12:00:00Z"
}
```

### GET /api/admin/support/tickets
Get support tickets list with filtering.

**Query Parameters:**
- `status` (optional): Filter by ticket status
- `priority` (optional): Filter by priority level
- `category` (optional): Filter by complaint category
- `page` (optional): Page number (default: 1)
- `per_page` (optional): Items per page (default: 20, max: 100)

**Response:**
```json
{
  "tickets": [
    {
      "id": "ticket_123",
      "customer_id": "customer_456",
      "category": "delivery_issue",
      "priority": "high",
      "status": "open",
      "subject": "Late delivery complaint",
      "created_at": "2024-01-01T10:00:00Z",
      "assigned_to": "support_agent_1"
    }
  ],
  "total": 50,
  "page": 1,
  "per_page": 20,
  "total_pages": 3,
  "has_next": true,
  "has_prev": false,
  "filters": {
    "status": "open",
    "priority": "high",
    "category": null
  },
  "timestamp": "2024-01-01T12:00:00Z"
}
```

### PUT /api/admin/support/tickets/{ticket_id}
Update support ticket status and information.

**Request Body:**
```json
{
  "status": "resolved",
  "priority": "medium",
  "assigned_to": "support_agent_2",
  "admin_notes": "Issue resolved by providing delivery tracking information",
  "resolution_notes": "Customer satisfied with explanation and tracking details"
}
```

**Response:**
```json
{
  "success": true,
  "ticket_id": "ticket_123",
  "updated_fields": ["status", "priority", "assigned_to", "admin_notes"],
  "updated_at": "2024-01-01T12:30:00Z"
}
```

## Campaign Management Endpoints

### GET /api/admin/campaigns
Get campaign analytics and performance metrics.

**Response:**
```json
{
  "campaign_overview": {
    "total_campaigns": 12,
    "active_campaigns": [
      {
        "id": "camp_123",
        "name": "Diwali Special Offer",
        "type": "seasonal",
        "status": "active",
        "start_date": "2024-10-20",
        "end_date": "2024-11-05"
      }
    ]
  },
  "performance_metrics": {
    "total_campaigns": 12,
    "active_count": 3,
    "total_reach": 5000,
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
  "name": "New Year Construction Special",
  "type": "seasonal",
  "target_audience": "contractors",
  "message": "Start your new year projects with our premium materials!",
  "discount_percentage": 12,
  "start_date": "2024-01-01",
  "end_date": "2024-01-31",
  "created_by": "admin_user"
}
```

**Response:**
```json
{
  "success": true,
  "campaign_id": "camp_456",
  "campaign_details": {
    "id": "camp_456",
    "name": "New Year Construction Special",
    "status": "active",
    "created_at": "2024-01-01T12:00:00Z"
  },
  "timestamp": "2024-01-01T12:00:00Z"
}
```

## Reports Endpoints

### GET /api/admin/reports
Generate comprehensive admin reports.

**Query Parameters:**
- `type` (required): Report type (`summary` or `financial`)
- `days` (optional): Analysis period in days (default: 30)

**Summary Report Response:**
```json
{
  "report_type": "summary",
  "period_days": 30,
  "generated_at": "2024-01-01T12:00:00Z",
  "order_summary": {
    "total_orders": 150,
    "total_revenue": 450000.00,
    "completion_rate": 85.5
  },
  "customer_summary": {
    "total_customers": 500,
    "new_customers": 25,
    "active_customers": 120
  },
  "support_summary": {
    "total_tickets": 50,
    "open_tickets": 8,
    "resolution_rate": 84.0
  },
  "key_metrics": {
    "total_revenue": 450000.00,
    "total_orders": 150,
    "total_customers": 500,
    "open_tickets": 8
  }
}
```

**Financial Report Response:**
```json
{
  "report_type": "financial",
  "period_days": 30,
  "generated_at": "2024-01-01T12:00:00Z",
  "revenue_analysis": {
    "total_revenue": 450000.00,
    "average_order_value": 3000.00,
    "highest_order_value": 25000.00,
    "lowest_order_value": 500.00
  },
  "order_analysis": {
    "total_orders": 150,
    "completion_rate": 85.5,
    "cancellation_rate": 5.2
  }
}
```

## Error Handling

All admin endpoints follow consistent error response format:

```json
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human readable error message",
    "timestamp": "2024-01-01T12:00:00Z"
  }
}
```

### Common Error Codes

| Code | Description |
|------|-------------|
| `ADMIN_DASHBOARD_ERROR` | Error retrieving dashboard data |
| `ADMIN_PRODUCTS_ERROR` | Error in product management |
| `PRODUCT_NOT_FOUND` | Product with given ID not found |
| `PRODUCT_UPDATE_ERROR` | Error updating product information |
| `STOCK_UPDATE_ERROR` | Error updating stock levels |
| `CUSTOMER_NOT_FOUND` | Customer with given ID not found |
| `CUSTOMER_UPDATE_ERROR` | Error updating customer information |
| `TICKET_UPDATE_ERROR` | Error updating support ticket |
| `CAMPAIGN_CREATION_ERROR` | Error creating campaign |
| `REPORT_GENERATION_ERROR` | Error generating report |
| `MISSING_REQUIRED_FIELD` | Required field missing from request |
| `INVALID_OPERATION` | Invalid operation specified |

## Authentication & Authorization

### Required Headers
```
Authorization: Bearer <admin_jwt_token>
Content-Type: application/json
```

### Admin Permissions
- **Super Admin**: Full access to all endpoints
- **Product Manager**: Access to product and stock management
- **Customer Manager**: Access to customer management
- **Support Manager**: Access to support ticket management
- **Campaign Manager**: Access to campaign management

## Rate Limiting

- Admin endpoints: 200 requests per minute per admin user
- Report generation: 10 requests per minute per admin user
- Bulk operations: 5 requests per minute per admin user

## Usage Examples

### Update Product Price
```bash
curl -X PUT "http://localhost:5000/api/admin/products/prod_123" \
  -H "Authorization: Bearer <admin_token>" \
  -H "Content-Type: application/json" \
  -d '{"price_per_unit": 8.75, "bulk_discount_percentage": 7.5}'
```

### Add Stock
```bash
curl -X POST "http://localhost:5000/api/admin/stock" \
  -H "Authorization: Bearer <admin_token>" \
  -H "Content-Type: application/json" \
  -d '{"product_id": "prod_123", "quantity": 500, "operation": "add", "reason": "New stock arrival"}'
```

### Resolve Support Ticket
```bash
curl -X PUT "http://localhost:5000/api/admin/support/tickets/ticket_123" \
  -H "Authorization: Bearer <admin_token>" \
  -H "Content-Type: application/json" \
  -d '{"status": "resolved", "admin_notes": "Issue resolved successfully"}'
```

### Generate Financial Report
```bash
curl -X GET "http://localhost:5000/api/admin/reports?type=financial&days=30" \
  -H "Authorization: Bearer <admin_token>"
```

## Production Considerations

1. **Security**: Implement proper JWT authentication with role-based access control
2. **Audit Logging**: Log all admin actions for compliance and security
3. **Rate Limiting**: Implement Redis-based rate limiting for admin endpoints
4. **Monitoring**: Add comprehensive monitoring and alerting for admin operations
5. **Backup**: Ensure all admin operations are backed up and recoverable
6. **Validation**: Add comprehensive input validation and sanitization
7. **Caching**: Cache frequently accessed admin data for better performance