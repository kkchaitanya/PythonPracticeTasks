CREATE TABLE projects (
    id UUID PRIMARY KEY,
    name VARCHAR(200),
    description TEXT,
    created_at TIMESTAMP
);
CREATE TABLE tasks (
    id UUID PRIMARY KEY,
    project_id UUID REFERENCES projects(id),
    title VARCHAR(255),
    description TEXT,
    priority VARCHAR(20),
    status VARCHAR(20),
    assigned_to VARCHAR(100),
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);