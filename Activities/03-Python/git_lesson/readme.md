# Step 1: Create a Branch

During your project, you’ll have a few distinct ideas in progress that may or may not be ready to go. Branching was created to manage this workflow. When you add a branch in your project, you’re creating an environment for trying out new ideas. Changes you make on a branch won’t affect the master branch, so you’re free to experiment and commit changes, assured that your branch won’t be merged until it is ready for a collaborator’s review.

There are a few ways you can create new branches in Git. The most common follows:
git checkout -b <branch-name>


The above method is used often because it will create a branch from your current branch and will switch you to that branch in a single command line.

Another common option is to use the branch command directly. Note that this command will not automatically switch over to the newly created branch. However, if you do wish to switch, you can use the checkout command.

In the code below, there are two commands. With the first, a branch is created. The second command will “checkout” the branch, and switch you to it.
git branch <branch-name>
git checkout <branch-name>

# Step 2: Add Commits

Once your branch has been created, you can start making changes. Whenever you add, edit, or delete a file, you’re making a commit and adding them to your branch. This process of adding commits keeps track of your progress as you work on a feature branch. Commits also create a transparent history of your work that others can follow to understand what you’ve done and why. Each commit has an associated commit message, which is a description explaining the reason a particular action was made. Moreover, each commit is considered a separate unit of change. This lets you roll back changes if a bug is found, or if you decide to head in a different direction.
git status
git add .
git commit -m 'first commit'

Please note, the git add . command will add all paths to the staged changes if they’re either changed or are new and not ignored. To fully grasp the add command, take a few minutes to read the documentation (https://git-scm.com/docs/git-add).

Once you’ve committed your changes, the natural next step is to push our branch. Remember, do commit and push early and often—creating periodic checkpoints helps you understand how you broke something.

	git push origin <branch-name>

# Step 3: Pull Requests

Pull requests initiate discussion about your commits. Since they’re tightly integrated with the underlying Git repository, anyone can see exactly what changes would be merged if they accept your request. Pull requests can be opened at any point during the development process: when you have little or no code but want to share some screenshots or general ideas, when you're stuck and need help or advice, or when you're ready for someone to review your work. Also, pull requests are useful for contributing to open source projects and for managing changes to shared repositories. If you're using a Fork & Pull Model, pull requests provide a way to notify project maintainers about the changes you'd like them to consider. If you're using a Shared Repository Model, pull requests help start a code review and conversation about proposed changes before they're merged into the master branch.
	git push origin <branch-name>

# Step 4: Review Your Code

Once a pull request has been opened, the person reviewing your changes might have questions or comments. Perhaps the coding style doesn’t match project guidelines, the change is missing unit tests, or maybe everything looks great and props are in order. Pull requests are designed to encourage and capture this type of conversation. Also, you can continue to push to your branch in light of feedback about your commits. If someone comments that you forgot to do something or if there is a bug in the code, you can make corrections in your branch and push up the change. GitHub will show your new commits and any additional feedback you might receive in the unified pull request view.

# Step 5: Deploy for Final Testing

With GitHub, you can deploy from a branch for final testing in production before merging to master. Once your pull request has been reviewed and the branch passes your tests, you can deploy your changes to verify them in production. If your branch causes issues, you can roll it back by deploying the existing master into production.

# Step 6: Merge Your Code

Now that your changes have been verified in production, it is time to merge your code into the master branch. Once merged, pull requests preserve a record of the historical changes to your code. These records are searchable so that anyone can review them easily to understand why and how decision was made.

Before performing a merge, there are a couple of preparation steps to take to ensure the merge is performed smoothly. Open the command line interface, if you have not already, and follow the instructions below:

1. Execute git status to ensure that HEAD is pointing to the correct merge-receiving branch. If needed, execute git checkout <receiving> to switch to the receiving branch or checkout directly to the merge-receiving branch if you know its name.

2. Make sure the receiving branch and the merging branch are up to date with the latest remote changes. Execute git fetch to pull the latest remote commits. Once the fetch is complete, ensure the master branch has the latest updates by executing git pull.

3. Now, a merge can be initiated by executing git merge <branch name>, whereby <branch name> is the name of the branch that will be merged into the receiving branch.

4. Once the merge is completed, deleting the branch you created is not necessary; however, it is best practice to prune unneeded branches.
