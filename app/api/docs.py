from flask import Blueprint, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Farm Marketplace API"
    }
)

# app/static/swagger.json
{
    "openapi": "3.0.0",
    "info": {
        "title": "Farm Marketplace API",
        "version": "1.0.0",
        "description": "API documentation for the Farm Marketplace application"
    },
    "servers": [
        {
            "url": "http://localhost:5000/api",
            "description": "Development server"
        }
    ],
    "paths": {
        "/marketplace/products": {
            "post": {
                "tags": ["Marketplace"],
                "summary": "Create a new product listing",
                "security": [
                    {
                        "bearerAuth": []
                    }
                ],
                "requestBody": {
                    "required": True,
                    "content": {
                        "application/json": {
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "name": {
                                        "type": "string"
                                    },
                                    "crop_type": {
                                        "type": "string"
                                    },
                                    "quantity": {
                                        "type": "number"
                                    },
                                    "unit": {
                                        "type": "string"
                                    },
                                    "price_per_unit": {
                                        "type": "number"
                                    },
                                    "quality_grade": {
                                        "type": "string"
                                    },
                                    "harvest_date": {
                                        "type": "string",
                                        "format": "date"
                                    },
                                    "description": {
                                        "type": "string"
                                    }
                                },
                                "required": ["name", "crop_type", "quantity", "unit", "price_per_unit"]
                            }
                        }
                    }
                },
                "responses": {
                    "201": {
                        "description": "Product created successfully"
                    },
                    "401": {
                        "description": "Unauthorized"
                    },
                    "400": {
                        "description": "Invalid input"
                    }
                }
            },
            "get": {
                "tags": ["Marketplace"],
                "summary": "List all available products",
                "parameters": [
                    {
                        "in": "query",
                        "name": "crop_type",
                        "schema": {
                            "type": "string"
                        },
                        "description": "Filter by crop type"
                    },
                    {
                        "in": "query",
                        "name": "sort",
                        "schema": {
                            "type": "string",
                            "enum": ["price_asc", "price_desc", "date_asc", "date_desc"]
                        },
                        "description": "Sort results"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "List of products",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "array",
                                    "items": {
                                        "$ref": "#/components/schemas/Product"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    },
    "components": {
        "securitySchemes": {
            "bearerAuth": {
                "type": "http",
                "scheme": "bearer",
                "bearerFormat": "JWT"
            }
        },
        "schemas": {
            "Product": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer"
                    },
                    "name": {
                        "type": "string"
                    },
                    "crop_type": {
                        "type": "string"
                    },
                    "quantity": {
                        "type": "number"
                    },
                    "unit": {
                        "type": "string"
                    },
                    "price_per_unit": {
                        "type": "number"
                    },
                    "quality_grade": {
                        "type": "string"
                    },
                    "harvest_date": {
                        "type": "string",
                        "format": "date"
                    },
                    "description": {
                        "type": "string"
                    },
                    "available": {
                        "type": "boolean"
                    }
                }
            }
        }
    }
}
