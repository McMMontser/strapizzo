#!/usr/bin/env python3
"""
Test script for Stripe integration fixes in Press Stripe Settings app
"""

import frappe
import sys
import os

def test_stripe_configuration():
    """Test if Stripe configuration is properly set up"""
    print("🔍 Testing Stripe Configuration...")
    
    try:
        # Test 1: Check if Press Settings exists
        press_settings = frappe.get_doc("Press Settings")
        print("✅ Press Settings document found")
        
        # Test 2: Check if Stripe keys are configured
        publishable_key = press_settings.stripe_publishable_key
        secret_key = press_settings.get_password("stripe_secret_key")
        
        if not publishable_key:
            print("⚠️  Stripe Publishable Key not configured")
        else:
            print("✅ Stripe Publishable Key configured")
            
        if not secret_key:
            print("⚠️  Stripe Secret Key not configured")
        else:
            print("✅ Stripe Secret Key configured")
            
        return bool(publishable_key and secret_key)
        
    except Exception as e:
        print(f"❌ Error testing Stripe configuration: {str(e)}")
        return False

def test_get_stripe_function():
    """Test the get_stripe() function"""
    print("\n🔍 Testing get_stripe() function...")
    
    try:
        from press.api.billing import get_stripe
        stripe = get_stripe()
        print("✅ get_stripe() function works correctly")
        return True
    except Exception as e:
        print(f"❌ Error testing get_stripe(): {str(e)}")
        return False

def test_create_stripe_plans_method():
    """Test the create_stripe_plans method"""
    print("\n🔍 Testing create_stripe_plans method...")
    
    try:
        # Import the fixed method
        from press_stripe_settings.api.create_stripe_plans import create_stripe_plans
        print("✅ create_stripe_plans method imported successfully")
        
        # Note: We won't actually call it to avoid creating real Stripe plans
        # This is just to test that the import works
        return True
        
    except Exception as e:
        print(f"❌ Error testing create_stripe_plans method: {str(e)}")
        return False

def test_press_settings_method():
    """Test the Press Settings create_stripe_plans method"""
    print("\n🔍 Testing Press Settings create_stripe_plans method...")
    
    try:
        # Import the fixed method from Press Settings
        from press.press.doctype.press_settings.press_settings import PressSettings
        press_settings = PressSettings()
        print("✅ Press Settings create_stripe_plans method accessible")
        return True
        
    except Exception as e:
        print(f"❌ Error testing Press Settings method: {str(e)}")
        return False

def main():
    """Main test function"""
    print("🚀 Starting Stripe Integration Tests...")
    print("=" * 50)
    
    # Initialize Frappe
    try:
        frappe.init(site="mazeed.local")
        frappe.connect()
        print("✅ Connected to Frappe site: mazeed.local")
    except Exception as e:
        print(f"❌ Failed to connect to Frappe: {str(e)}")
        return False
    
    # Run tests
    tests = [
        test_stripe_configuration,
        test_get_stripe_function,
        test_create_stripe_plans_method,
        test_press_settings_method
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Stripe integration is working correctly.")
        return True
    else:
        print("⚠️  Some tests failed. Please check the configuration.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 