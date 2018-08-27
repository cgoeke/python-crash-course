# 17-3. Testing python_repos.py: In python_repos.py, we printed the value
# of status_code to make sure the API call was successful. Write a program
# called test_python_repos.py, which uses unittest to assert that the value
# of status_code is 200. Figure out some other assertions you can make—for
# example, that the number of items returned is expected and that the total
# number of repositories is greater than a certain amount.
import unittest
import python_repos as pr

class TestPythonRepos(unittest.TestCase):
    """Tests python_repos.py program."""
    def setUp(self):
        self.r = pr.get_response()
        self.repo_dicts = pr.get_repo_dicts(self.r)
        self.repo_dict = self.repo_dicts[0]
        self.names, self.repo_dicts = pr.get_names_plot_dicts(self.repo_dicts)

    def test_get_response(self):
        self.assertEqual(self.r.status_code, 200)

    def test_get_repo_dicts(self):
        self.assertEqual(len(self.repo_dicts), 30)

        # Repositories should have required keys.
        required_keys = ['name', 'owner', 'stargazers_count', 'html_url']
        for key in required_keys:
            self.assertTrue(key in self.repo_dict.keys())


unittest.main()