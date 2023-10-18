db = db.getSiblingDB('ws-auth');  // Sets the new database context
db.createUser({
    user: 'user',
    pwd: 'password',
    roles: [{ role: 'readWrite', db: 'ws-auth' }],
});