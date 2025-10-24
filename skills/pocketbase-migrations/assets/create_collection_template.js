/// <reference path="../pb_data/types.d.ts" />

migrate((db) => {
  const collection = new Collection({
    id: "auto_generated_collection_id",
    created: new Date("2024-01-01 00:00:00.000Z"),
    updated: new Date("2024-01-01 00:00:00.000Z"),
    name: "collection_name",
    type: "base",
    system: false,
    schema: [
      // Add fields here
    ],
    indexes: [],
    listRule: "@request.auth.id != \"\"",
    viewRule: "@request.auth.id != \"\"",
    createRule: "@request.auth.id != \"\"",
    updateRule: "@request.auth.id != \"\" && @request.auth.id = owner",
    deleteRule: "@request.auth.id != \"\" && @request.auth.id = owner",
    options: {}
  });

  return Dao(db).saveCollection(collection);
}, (db) => {
  // Rollback code here
  const dao = new Dao(db);
  dao.deleteCollection("collection_name_or_id");
});