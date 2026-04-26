from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import RecordModel

# 建立名為 record_bp 的 Blueprint
record_bp = Blueprint('record', __name__)

@record_bp.route('/')
def index():
    """
    處理首頁 (Dashboard)。
    獲取所有紀錄，計算當月總收入與支出，並渲染 index.html。
    """
    pass

@record_bp.route('/records', methods=['GET'])
def history():
    """
    處理歷史明細列表。
    獲取所有收支紀錄並渲染 history.html。
    """
    pass

@record_bp.route('/records', methods=['POST'])
def create_record():
    """
    處理新增收支紀錄的表單提交。
    接收表單資料，寫入資料庫後重導向至首頁。
    """
    pass

@record_bp.route('/records/<int:record_id>/edit', methods=['GET'])
def edit_record(record_id):
    """
    顯示編輯收支紀錄的表單頁面。
    根據 record_id 查詢紀錄，並渲染 edit.html。
    """
    pass

@record_bp.route('/records/<int:record_id>/update', methods=['POST'])
def update_record(record_id):
    """
    處理更新收支紀錄的表單提交。
    接收表單資料並更新資料庫對應紀錄，完成後重導向至歷史明細頁。
    """
    pass

@record_bp.route('/records/<int:record_id>/delete', methods=['POST'])
def delete_record(record_id):
    """
    處理刪除指定收支紀錄的操作。
    從資料庫中刪除對應的 record_id 資料，完成後重導向至歷史明細頁。
    """
    pass
