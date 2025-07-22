frappe.ui.form.on('Press Settings', {
  create_stripe_plans(frm) {
    frm.call('press_stripe_settings.api.create_stripe_plans.create_stripe_plans');
  },
}); 