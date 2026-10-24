from playwright.sync_api import Page, expect

def test_add_todo(page: Page):
    page.goto("https://demo.playwright.dev/todomvc/")
    page.get_by_placeholder("What needs to be done?").fill("Испечь хлебный светильник")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    expect(page.get_by_test_id("todo-title")).to_have_text("Испечь хлебный светильник")
    page.screenshot(path="todo.png")