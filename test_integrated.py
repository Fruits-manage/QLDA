"""
Integrated Test Script - Test both Models and Views
Kiểm tra toàn diện cả Model và View layer
"""

import os
import sys
import django
import requests
from datetime import datetime

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fruit_manage.settings')
django.setup()

def check_server_running(base_url="http://127.0.0.1:8000"):
    """Check if Django server is running"""
    try:
        response = requests.get(base_url, timeout=5, allow_redirects=False)
        return True
    except requests.exceptions.RequestException:
        return False

def test_integration():
    """Run integration tests"""
    print("🚀 FRUIT MANAGEMENT SYSTEM - INTEGRATED TEST SUITE")
    print("=" * 80)
    print(f"🕐 Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    
    # Test 1: Model Level Tests
    print("\n🔍 PHASE 1: MODEL LEVEL TESTS")
    print("-" * 50)
    
    try:
        from test_simple_crud import SimpleCRUDTest
        model_test = SimpleCRUDTest()
        model_results = model_test.run_all_tests()
        model_success = all(model_results.values())
        
        if model_success:
            print("\n✅ MODEL TESTS: ALL PASSED")
        else:
            print("\n❌ MODEL TESTS: SOME FAILED")
            failed_modules = [k for k, v in model_results.items() if not v]
            print(f"Failed modules: {', '.join(failed_modules)}")
            
    except Exception as e:
        print(f"\n❌ MODEL TESTS: CRITICAL ERROR - {str(e)}")
        model_success = False
    
    # Test 2: Server Connectivity
    print("\n🔍 PHASE 2: SERVER CONNECTIVITY TEST")
    print("-" * 50)
    
    server_running = check_server_running()
    if server_running:
        print("✅ Django server is running and accessible")
        
        # Test 3: HTTP Views Tests
        print("\n🔍 PHASE 3: HTTP VIEW TESTS")
        print("-" * 50)
        
        try:
            from test_quick_crud import test_urls, test_admin_urls
            url_results = test_urls()
            
            accessible_count = len(url_results['accessible'])
            redirect_count = len(url_results['redirect'])
            total_count = accessible_count + redirect_count + len(url_results['not_accessible'])
            
            if accessible_count + redirect_count == total_count:
                print("✅ HTTP VIEWS: ALL ENDPOINTS ACCESSIBLE")
                view_success = True
            else:
                print("⚠️  HTTP VIEWS: SOME ENDPOINTS HAVE ISSUES")
                view_success = False
                
        except Exception as e:
            print(f"❌ HTTP VIEWS: ERROR - {str(e)}")
            view_success = False
    else:
        print("❌ Django server is not running")
        print("💡 To test HTTP views, run: python manage.py runserver")
        view_success = False
    
    # Final Summary
    print("\n" + "=" * 80)
    print("🎯 INTEGRATION TEST FINAL SUMMARY")
    print("=" * 80)
    
    print(f"📊 Model Layer:     {'✅ PASSED' if model_success else '❌ FAILED'}")
    print(f"📊 Server Status:   {'✅ RUNNING' if server_running else '❌ NOT RUNNING'}")
    
    if server_running:
        print(f"📊 View Layer:      {'✅ PASSED' if view_success else '⚠️  ISSUES'}")
    else:
        print(f"📊 View Layer:      🔄 SKIPPED (Server not running)")
    
    # Overall Status
    if model_success and (not server_running or view_success):
        overall_status = "🎉 EXCELLENT"
        overall_message = "System is working perfectly!"
    elif model_success:
        overall_status = "✅ GOOD"
        overall_message = "Core functionality working. Start server for full testing."
    else:
        overall_status = "❌ ISSUES"
        overall_message = "Critical issues found. Check model layer first."
    
    print(f"\n🏆 OVERALL STATUS: {overall_status}")
    print(f"💬 {overall_message}")
    
    # Recommendations
    print(f"\n💡 RECOMMENDATIONS:")
    if not model_success:
        print("🔧 Fix model layer issues first")
    if not server_running:
        print("🔧 Start Django server: python manage.py runserver")
    if server_running and not view_success:
        print("🔧 Check view implementations and URL patterns")
    
    print("🔧 Run manual tests using test_manual_guide.md")
    print("🔧 For detailed model tests: python test_simple_crud.py")
    print("🔧 For HTTP tests: python test_quick_crud.py (with server running)")
    
    print("=" * 80)
    print(f"🕐 Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    
    return {
        'model_success': model_success,
        'server_running': server_running,
        'view_success': view_success if server_running else None
    }

def main():
    """Main function"""
    print("🧪 FRUIT MANAGEMENT SYSTEM - INTEGRATED TEST RUNNER")
    print("📋 This script tests both database models and HTTP views")
    print("📋 Automatically detects if Django server is running")
    print()
    
    try:
        results = test_integration()
        
        # Exit code based on results
        if results['model_success'] and (not results['server_running'] or results['view_success']):
            return 0  # Success
        else:
            return 1  # Issues found
            
    except KeyboardInterrupt:
        print("\n\n⚠️  Test interrupted by user")
        return 1
    except Exception as e:
        print(f"\n❌ CRITICAL ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == '__main__':
    exit_code = main()
    sys.exit(exit_code)
