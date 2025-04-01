# routes.py
from flask import Blueprint, request, jsonify
from models_forms import db, Item, ItemForm
from werkzeug.exceptions import BadRequest

routes_bp = Blueprint("routes", __name__)


# ✅ **Get all items with Pagination using path variables**
@routes_bp.route("/items/<int:page>/<int:pagesize>", methods=["GET"])
def get_items(page, pagesize):
    if page < 1 or pagesize < 1:
        raise BadRequest("Page and pageSize must be positive integers.")

    # Paginate the results
    items_paginated = Item.query.paginate(page=page, per_page=pagesize, error_out=False)

    items = items_paginated.items

    # Prepare response data
    response = {
        "items": [{"id": item.id, "name": item.name, "quantity": item.quantity} for item in items],
        "total": items_paginated.total,  # Total number of items in the database
        "page": page,
        "per_page": pagesize,
        "pages": items_paginated.pages  # Total number of pages
    }

    return jsonify(response)


@routes_bp.route("/item/<int:id>", methods=["GET"])
def get_item(id):
    item = Item.query.get_or_404(id, "Item was not found")
    return jsonify({"id": item.id, "name": item.name, "quantity": item.quantity})


@routes_bp.route("/item", methods=["POST"])
def add_item():
    data = request.get_json()
    if not data:
        raise BadRequest("Invalid JSON data")

    form = ItemForm(data=data)
    if form.validate():
        new_item = Item(name=form.name.data, quantity=form.quantity.data)
        db.session.add(new_item)
        db.session.commit()
        return jsonify({"message": "Item created successfully"}), 201
    else:
        raise BadRequest(form.errors)


@routes_bp.route("/item/<int:id>", methods=["DELETE"])
def delete_item(id):
    item = Item.query.get_or_404(id, "Item was not found")
    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "Item deleted successfully"})


@routes_bp.route("/item/<int:id>", methods=["PUT"])
def update_item(id):
    data = request.get_json()
    item = Item.query.get_or_404(id, "Item was not found")

    form = ItemForm(data=data)
    if form.validate():
        item.name = form.name.data
        item.quantity = form.quantity.data
        db.session.commit()
        return jsonify({"message": "Item updated successfully"})
    else:
        raise BadRequest(form.errors)
