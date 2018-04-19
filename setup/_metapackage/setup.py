import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo10-addons-oca-account-financial-tools",
    description="Meta package for oca-account-financial-tools Odoo addons",
    version=version,
    install_requires=[
        'odoo10-addon-account_asset_depr_line_cancel',
        'odoo10-addon-account_asset_disposal',
        'odoo10-addon-account_balance_line',
        'odoo10-addon-account_chart_update',
        'odoo10-addon-account_check_deposit',
        'odoo10-addon-account_credit_control',
        'odoo10-addon-account_credit_control_dunning_fees',
        'odoo10-addon-account_fiscal_month',
        'odoo10-addon-account_fiscal_position_vat_check',
        'odoo10-addon-account_fiscal_year',
        'odoo10-addon-account_invoice_constraint_chronology',
        'odoo10-addon-account_invoice_currency',
        'odoo10-addon-account_invoice_tax_required',
        'odoo10-addon-account_journal_lock_date',
        'odoo10-addon-account_lock_date_update',
        'odoo10-addon-account_move_batch_validate',
        'odoo10-addon-account_move_fiscal_month',
        'odoo10-addon-account_move_fiscal_year',
        'odoo10-addon-account_move_line_payable_receivable_filter',
        'odoo10-addon-account_move_line_tax_editable',
        'odoo10-addon-account_move_locking',
        'odoo10-addon-account_move_template',
        'odoo10-addon-account_netting',
        'odoo10-addon-account_partner_required',
        'odoo10-addon-account_permanent_lock_move',
        'odoo10-addon-account_permanent_lock_move_update',
        'odoo10-addon-account_renumber',
        'odoo10-addon-account_reversal',
        'odoo10-addon-account_tag_category',
        'odoo10-addon-account_type_inactive',
        'odoo10-addon-account_type_menu',
        'odoo10-addon-base_vat_optional_vies',
        'odoo10-addon-currency_rate_update',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
