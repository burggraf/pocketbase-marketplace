# PocketBase API Rules Reference

## API Rule Structure

API rules define who can access collections and what operations they can perform. Each rule specifies conditions for create, read, update, and delete operations.

## Rule Types

### Public Access
- `"public"` - Anyone can access without authentication
- `"verified"` - Only verified email users can access

### Owner Access
- `"@request.auth.id != \"\" && @request.auth.id = owner"` - Only record owner can access
- `"@request.auth.id != \"\" && @request.auth.id = @request.data.owner"` - User matches specified owner field

### Admin Access
- `"@request.auth.role = \"admin\""` - Only admin users can access

### Custom Rules
- Complex conditions using field comparisons
- User role-based access
- Time-based restrictions
- Multi-condition rules

## Common Rule Patterns

### Public Read-Only Collection
```javascript
{
  "create": "false",
  "read": "public",
  "update": "false",
  "delete": "false"
}
```

### Authenticated Users Only
```javascript
{
  "create": "@request.auth.id != \"\"",
  "read": "@request.auth.id != \"\"",
  "update": "@request.auth.id != \"\"",
  "delete": "@request.auth.id != \"\""
}
```

### Owner-Only Access
```javascript
{
  "create": "@request.auth.id != \"\"",
  "read": "@request.auth.id != \"\" && @request.auth.id = owner",
  "update": "@request.auth.id != \"\" && @request.auth.id = owner",
  "delete": "@request.auth.id != \"\" && @request.auth.id = owner"
}
```

### Admin-Only Collection
```javascript
{
  "create": "@request.auth.role = \"admin\"",
  "read": "@request.auth.role = \"admin\"",
  "update": "@request.auth.role = \"admin\"",
  "delete": "@request.auth.role = \"admin\""
}
```

### Mixed Access (Public Read, Owner Write)
```javascript
{
  "create": "@request.auth.id != \"\"",
  "read": "public",
  "update": "@request.auth.id != \"\" && @request.auth.id = owner",
  "delete": "@request.auth.id != \"\" && @request.auth.id = owner"
}
```

### Role-Based Access
```javascript
{
  "create": "@request.auth.role in [\"admin\", \"editor\"]",
  "read": "@request.auth.role != \"\"",
  "update": "@request.auth.role in [\"admin\", \"editor\"] && @request.auth.id = owner",
  "delete": "@request.auth.role = \"admin\""
}
```

### Conditional Access Based on Status
```javascript
{
  "create": "@request.auth.id != \"\"",
  "read": "public && status = \"published\"",
  "update": "@request.auth.id != \"\" && @request.auth.id = owner",
  "delete": "@request.auth.id != \"\" && @request.auth.id = owner"
}
```

## Rule Variables

### Request Variables
- `@request.auth.id` - Authenticated user ID
- `@request.auth.email` - User email
- `@request.auth.role` - User role
- `@request.data.fieldName` - Data being submitted

### Record Variables
- `owner` - Owner field value
- `status` - Status field value
- Any field name can be referenced directly

## Rule Operators

### Comparison Operators
- `=` - Equal
- `!=` - Not equal
- `>` - Greater than
- `>=` - Greater than or equal
- `<` - Less than
- `<=` - Less than or equal

### Logical Operators
- `&&` - AND
- `||` - OR
- `!` - NOT

### Membership
- `in` - Value is in array
- `contains` - Array contains value

## Best Practices

1. **Principle of Least Privilege** - Grant minimum necessary access
2. **Always Use Owner Check** - For user-generated content
3. **Separate Read/Write Rules** - Different access for different operations
4. **Use Role-Based Access** - For complex applications
5. **Test Rules Thoroughly** - Before going to production
6. **Document Your Rules** - For future maintenance