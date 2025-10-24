# Example PocketBase Migrations

## Create Users Collection
```javascript
/// <reference path="../pb_data/types.d.ts" />

migrate((db) => {
  const collection = new Collection({
    id: "users_collection_id",
    created: new Date("2024-01-01 00:00:00.000Z"),
    updated: new Date("2024-01-01 00:00:00.000Z"),
    name: "users",
    type: "auth",
    system: false,
    schema: [
      {
        id: "name_field_id",
        name: "name",
        type: "text",
        required: true,
        presentable: true,
        unique: false,
        options: {
          min: 1,
          max: 100,
          pattern: ""
        }
      },
      {
        id: "email_field_id",
        name: "email",
        type: "email",
        required: true,
        presentable: false,
        unique: true,
        options: {}
      },
      {
        id: "verified_field_id",
        name: "verified",
        type: "bool",
        required: false,
        presentable: false,
        unique: false,
        options: {}
      }
    ],
    indexes: [],
    listRule: "@request.auth.id != \"\"",
    viewRule: "@request.auth.id != \"\"",
    createRule: "",
    updateRule: "@request.auth.id != \"\"",
    deleteRule: "@request.auth.id != \"\"",
    options: {
      allowEmailAuth: true,
      allowOAuth2Auth: true,
      allowUsernameAuth: false,
      exceptEmailDomains: null,
      manageRule: null,
      minPasswordLength: 8,
      onlyEmailDomains: null,
      onlyVerified: false,
      requireEmail: false
    }
  });

  return Dao(db).saveCollection(collection);
}, (db) => {
  const dao = new Dao(db);
  dao.deleteCollection("users");
});
```

## Create Posts Collection with Relation
```javascript
/// <reference path="../pb_data/types.d.ts" />

migrate((db) => {
  const collection = new Collection({
    id: "posts_collection_id",
    created: new Date("2024-01-01 00:00:00.000Z"),
    updated: new Date("2024-01-01 00:00:00.000Z"),
    name: "posts",
    type: "base",
    system: false,
    schema: [
      {
        id: "title_field_id",
        name: "title",
        type: "text",
        required: true,
        presentable: true,
        unique: false,
        options: {
          min: 1,
          max: 200,
          pattern: ""
        }
      },
      {
        id: "content_field_id",
        name: "content",
        type: "text",
        required: true,
        presentable: false,
        unique: false,
        options: {
          min: 1,
          max: 5000,
          pattern: ""
        }
      },
      {
        id: "status_field_id",
        name: "status",
        type: "select",
        required: true,
        presentable: false,
        unique: false,
        options: {
          maxSelect: 1,
          values: ["draft", "published", "archived"]
        }
      },
      {
        id: "author_field_id",
        name: "author",
        type: "relation",
        required: true,
        presentable: false,
        unique: false,
        options: {
          collectionId: "users_collection_id",
          maxSelect: 1,
          cascadeDelete: true
        }
      },
      {
        id: "published_at_field_id",
        name: "published_at",
        type: "datetime",
        required: false,
        presentable: false,
        unique: false,
        options: {}
      }
    ],
    indexes: [],
    listRule: "status = \"published\"",
    viewRule: "status = \"published\" || @request.auth.id != \"\" && @request.auth.id = author.id",
    createRule: "@request.auth.id != \"\"",
    updateRule: "@request.auth.id != \"\" && @request.auth.id = author.id",
    deleteRule: "@request.auth.id != \"\" && @request.auth.id = author.id",
    options: {}
  });

  return Dao(db).saveCollection(collection);
}, (db) => {
  const dao = new Dao(db);
  dao.deleteCollection("posts");
});
```

## Add Field to Existing Collection
```javascript
/// <reference path="../pb_data/types.d.ts" />

migrate((db) => {
  const dao = new Dao(db);
  const collection = dao.findCollectionByNameOrId("posts");

  collection.schema.addField({
    id: "tags_field_id",
    name: "tags",
    type: "select",
    required: false,
    presentable: false,
    unique: false,
    options: {
      maxSelect: 5,
      values: ["tech", "design", "business", "tutorial", "news"]
    }
  });

  return dao.saveCollection(collection);
}, (db) => {
  const dao = new Dao(db);
  const collection = dao.findCollectionByNameOrId("posts");

  // Remove the tags field
  collection.schema.removeField("tags_field_id");

  return dao.saveCollection(collection);
});
```

## Remove Field from Collection
```javascript
/// <reference path="../pb_data/types.d.ts" />

migrate((db) => {
  const dao = new Dao(db);
  const collection = dao.findCollectionByNameOrId("posts");

  // Remove the old_status field
  collection.schema.removeField("old_status_field_id");

  return dao.saveCollection(collection);
}, (db) => {
  const dao = new Dao(db);
  const collection = dao.findCollectionByNameOrId("posts");

  // Add back the old_status field
  collection.schema.addField({
    id: "old_status_field_id",
    name: "old_status",
    type: "select",
    required: false,
    presentable: false,
    unique: false,
    options: {
      maxSelect: 1,
      values: ["active", "inactive"]
    }
  });

  return dao.saveCollection(collection);
});
```

## Delete Collection
```javascript
/// <reference path="../pb_data/types.d.ts" />

migrate((db) => {
  const dao = new Dao(db);

  // Delete the old_comments collection
  dao.deleteCollection("old_comments");
}, (db) => {
  const dao = new Dao(db);

  // Recreate the old_comments collection
  const collection = new Collection({
    id: "old_comments_collection_id",
    created: new Date("2024-01-01 00:00:00.000Z"),
    updated: new Date("2024-01-01 00:00:00.000Z"),
    name: "old_comments",
    type: "base",
    system: false,
    schema: [
      {
        id: "content_field_id",
        name: "content",
        type: "text",
        required: true,
        presentable: false,
        unique: false,
        options: {
          min: 1,
          max: 1000,
          pattern: ""
        }
      }
    ],
    indexes: [],
    listRule: "@request.auth.id != \"\"",
    viewRule: "@request.auth.id != \"\"",
    createRule: "@request.auth.id != \"\"",
    updateRule: "@request.auth.id != \"\" && @request.auth.id = owner",
    deleteRule: "@request.auth.id != \"\" && @request.auth.id = owner",
    options: {}
  });

  return dao.saveCollection(collection);
});
```