from odoo import models, fields , api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    sale_order_ids = fields.One2many('sale.order', 'partner_id', string='Sale Orders' )
    purchase_order_ids = fields.One2many('purchase.order', 'partner_id', string='Purchase Orders')
    invoice_ids = fields.One2many('account.move', 'partner_id', string='Customer Invoices',domain=[('move_type', '=', 'out_invoice')])
    vendor_bill_ids = fields.One2many('account.move', 'partner_id',string="Vendor Bills",domain=[('move_type', '=', 'in_invoice')])
    incoming_picking_ids = fields.One2many('stock.picking','partner_id',string="Incoming Orders",domain=[('picking_type_code', '=', 'incoming')])
    delivery_picking_ids = fields.One2many('stock.picking','partner_id',string="Delivery Orders",domain=[('picking_type_code', '=', 'outgoing')])
    task_ids = fields.One2many('project.task', string='Tasks')


class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_open_form_view(self):
        self.ensure_one()
        name = 'Vendor Bill' if self.move_type == 'in_invoice' else 'Customer Invoice'
        return {
            'type': 'ir.actions.act_window',
            'name': name,
            'res_model': 'account.move',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'current',
        }

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def action_open_form_view(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Purchase Order',
            'res_model': 'purchase.order',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'current',
        }

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_open_form_view(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Sale Order',
            'res_model': 'sale.order',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'current',
        }

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def action_open_form_view(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Incoming Order',
            'res_model': 'stock.picking',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'current',
        }

class ProjectTask(models.Model):
    _inherit = 'project.task'

    def action_open_form_view(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Task',
            'res_model': 'project.task',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'current',
        }