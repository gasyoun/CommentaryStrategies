CREATE TABLE IF NOT EXISTS drafts (
  reviewer TEXT NOT NULL,
  manifest_revision TEXT NOT NULL,
  sarga INTEGER NOT NULL CHECK (sarga BETWEEN 1 AND 68),
  version INTEGER NOT NULL,
  decisions_json TEXT NOT NULL,
  content_hash TEXT NOT NULL,
  updated_at TEXT NOT NULL,
  PRIMARY KEY (reviewer, manifest_revision, sarga)
);
CREATE INDEX IF NOT EXISTS drafts_lookup ON drafts(reviewer, manifest_revision, sarga);
CREATE TABLE IF NOT EXISTS submissions (
  content_hash TEXT PRIMARY KEY,
  reviewer TEXT NOT NULL,
  pr_url TEXT NOT NULL,
  created_at TEXT NOT NULL
);
