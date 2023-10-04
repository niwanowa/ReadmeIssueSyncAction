# ReadmeIssueSyncAction
issuesとREADME.mdを同期させ、READMEに一覧を表示させる。

## セットアップ
1. `.github/workflows/`に`update_readme.yml`及び`update_readmeフォルダ`を配置する。
2. Workflow permissionsを変更する。
    1. `Settings` > `Actions` > `General` 　を開く。
    2.  `Workflow permissions`のRead and write permissionsにチェックを入れSaveボタンを押す。
    ![SS](/docs/WorkflowPermissions.png)
3. Sercretsを設定する。
    1. `Settings` > `Secrets and cariables` > `Actions` 　を開く。
    2.  `New repository secret`を押し、以下の4変数を定義する。
    - GH_TOKEN : [参考](https://docs.github.com/ja/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
    - GH_USEREMAIL : コミットするユーザーのメールアドレス
    - GH_USERNAME : コミットするユーザーのアカウント名
    - REPOSITORY : 対象リポジトリ 例: niwanowa/ReadmeIssueSyncAction
    ![SS](/docs/Secrets.png)
4. README.mdのIssueのリストを表示させたい場所に以下の記述を追加する。
    ```
    <!-- ISSUE_LIST_START -->
- [workflowtest！](https://github.com/niwanowa/ReadmeIssueSyncAction/issues/3)
<!-- github actions: Updated on 2023-10-04 13:00:53 UTC-->
<!-- ISSUE_LIST_END -->
    ```
完了!

## 使い方
1. 以下のタイミングでActrionsが実行されます。
- issueが作られたとき
- issueが編集されたとき
- issueがクローズされたとき
- issueが再オープンされたとき


## 動作例
<!-- ISSUE_LIST_START -->
- [workflowtest！](https://github.com/niwanowa/ReadmeIssueSyncAction/issues/3)
- [READMEに必要な設定を記載する。](https://github.com/niwanowa/ReadmeIssueSyncAction/issues/2)
<!-- github actions: Updated on 2023-10-04 08:25:15 UTC-->
