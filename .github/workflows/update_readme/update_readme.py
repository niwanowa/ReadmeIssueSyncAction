import os
import json

# 環境変数をからREPOSITORYを取得
repository = os.environ['REPOSITORY']

# repositoryから、githubAPIを用いてIssueのリストを取得
issues = json.loads(os.popen(f'curl -s https://api.github.com/repos/{repository}/issues').read())
for issue in issues:
    print("----")
    print(issue['title'])
    print(issue)

# README.mdの読み込み
with open('../../../README.md', 'r') as f:
    readme_content = f.read()

# # Issueリストの生成
issue_list = [f"- [{issue['title']}]({issue['html_url']})" for issue in issues]

# # README.mdの更新
readme_content = readme_content.replace('<!-- ISSUE_LIST_START -->\n<!-- This section will be automatically updated by the GitHub Action -->\n<!-- ISSUE_LIST_END -->', '<!-- ISSUE_LIST_START -->\n{}\n<!-- ISSUE_LIST_END -->'.format('\n'.join(issue_list)))

# # 更新内容を書き込み
with open('../../../README.md', 'w') as f:
    f.write(readme_content)

print('README.md updated with the latest issues.')
