# DevOps_Assignment
•	Initialize a local repository and start writing the code and establish its remote counterpart on GitHub
•	Install pytest in your local machine using pip (Pip Installs Packages) which is the package manager for Python.
        Command: pip install pytest
•	Once the code is developed, build Unit Tests to check code quality, reliability of the written code with multiple test cases to check successful, negative, error handling, boundary scenarios.
•	Execute the test cases
		Command: pytest <test_file>
•	Once the test cases are passed, automate the testing to ensure that code changes are thoroughly validated before proceeding to subsequent stages of the pipeline.
•	Local Test automation can be achieved through GitHub hooks. These are scripts that Git automatically runs before or after events like commit and push.
•	We can use pre-commit hook to run the test which prevents us from ever committing code that breaks the test suite.
•	To set it up:
    1.	Install the framework: pip install pre-commit
    2.	Create a configuration file named “.pre-commit-config.yaml” in your project root directory.
    3.	Set up the git hooks: pre-commit install
•	Now, every time we run git commit, the tests (and any other configured checks) will run automatically. If the tests fail, the commit is aborted.
Note: Commit the code changes to the feature branch and then merge the code to master/main branch.
•	Once the testing is completed, commit the changes to the remote repository starting with staging the files from the local repository by “git add .” GIT command.
•	Commit the changes to the local repository with the command git commit -m "commit message".
•	Once all the tests are passed and if there are no issues between the commits, you can proceed to push the code to the remote repository but running git push origin <feature-branch>
