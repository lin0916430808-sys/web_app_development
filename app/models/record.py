import sqlite3
from typing import List, Dict, Any, Optional

# 設定資料庫檔案路徑（依據 ARCHITECTURE.md 的規劃放在 instance 內）
DB_PATH = 'instance/database.db'

class RecordModel:
    @staticmethod
    def get_connection():
        # 建立資料庫連線，並設定 row_factory 讓查詢結果能以 dict 方式存取
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        return conn

    @staticmethod
    def create(type: str, date: str, amount: float, category: str, description: str = None) -> int:
        """新增一筆收支紀錄"""
        conn = RecordModel.get_connection()
        cursor = conn.cursor()
        query = '''
            INSERT INTO record (type, date, amount, category, description)
            VALUES (?, ?, ?, ?, ?)
        '''
        cursor.execute(query, (type, date, amount, category, description))
        conn.commit()
        last_id = cursor.lastrowid
        conn.close()
        return last_id

    @staticmethod
    def get_all() -> List[Dict[str, Any]]:
        """取得所有收支紀錄，按日期遞減排序"""
        conn = RecordModel.get_connection()
        cursor = conn.cursor()
        query = 'SELECT * FROM record ORDER BY date DESC, id DESC'
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    @staticmethod
    def get_by_id(record_id: int) -> Optional[Dict[str, Any]]:
        """根據 ID 取得單筆收支紀錄"""
        conn = RecordModel.get_connection()
        cursor = conn.cursor()
        query = 'SELECT * FROM record WHERE id = ?'
        cursor.execute(query, (record_id,))
        row = cursor.fetchone()
        conn.close()
        return dict(row) if row else None

    @staticmethod
    def update(record_id: int, type: str, date: str, amount: float, category: str, description: str = None) -> bool:
        """更新單筆收支紀錄"""
        conn = RecordModel.get_connection()
        cursor = conn.cursor()
        query = '''
            UPDATE record 
            SET type = ?, date = ?, amount = ?, category = ?, description = ?
            WHERE id = ?
        '''
        cursor.execute(query, (type, date, amount, category, description, record_id))
        conn.commit()
        rowcount = cursor.rowcount
        conn.close()
        return rowcount > 0

    @staticmethod
    def delete(record_id: int) -> bool:
        """刪除單筆收支紀錄"""
        conn = RecordModel.get_connection()
        cursor = conn.cursor()
        query = 'SELECT * FROM record WHERE id = ?'
        cursor.execute('DELETE FROM record WHERE id = ?', (record_id,))
        conn.commit()
        rowcount = cursor.rowcount
        conn.close()
        return rowcount > 0
