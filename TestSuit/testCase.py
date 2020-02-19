def test_cases(number):
    return testCases[number]

testCases = [
    ['Test1', 'when user goes to main page, page should be loaded'],
    ['Test2', 'In Main page, when user search "dress" button, he should see result for dress'],
    ['Test3', 'In Main page, when user click "Sing up" button, he should see Sign up Page'],
    ['Test4', 'In Login Page, when user login with a valid data, he should see Home Page'],
    ['Test5', "In Login Page, when user login with a invalid data, he shouldn't see Home Page"],
    ['Test6', "In Login Page, when user login with a Google, he should see the Google authorization page"],
    ['Test6', "In Login Page, when user login with a Facebook, he should see the Google authorization page"]
]