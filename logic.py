class DB_Manager:
    pass
def update_project_status(self, project_id, status):
    cursor = self.conn.cursor()
    cursor.execute(
        "UPDATE projects SET status = ? WHERE id = ?",
        (status, project_id)
    )
    self.conn.commit()


