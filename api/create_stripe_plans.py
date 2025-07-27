import frappe
import stripe
from press.api.billing import get_stripe

@frappe.whitelist()
def create_stripe_plans():
    doc = frappe.get_doc("Press Settings")
    stripe = get_stripe()
    try:
        product = stripe.Product.create(name="SaaS Subscription Plan")
        price_usd = stripe.Price.create(
            product=product.id,
            unit_amount=1000,
            currency="usd",
            recurring={"interval": "month"},
        )
        price_inr = stripe.Price.create(
            product=product.id,
            unit_amount=80000,
            currency="inr",
            recurring={"interval": "month"},
        )
        doc.stripe_product_id = product.id
        doc.stripe_usd_plan_id = price_usd.id
        doc.stripe_inr_plan_id = price_inr.id
        doc.save()
        frappe.msgprint("Stripe plans created and IDs saved.")
        return {
            "product_id": product.id,
            "usd_plan_id": price_usd.id,
            "inr_plan_id": price_inr.id,
        }
    except Exception as e:
        frappe.log_error(f"Stripe plan creation failed: {str(e)}")
        frappe.throw(f"Stripe plan creation failed: {str(e)}") 