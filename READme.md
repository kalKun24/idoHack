# idoHack
``` python
python3 manage.py makemigrations && python3 manage.py migrate
python3 manage.py runserver
```

## TODO-List
### 一般
- [ ] markdownでページを記述できるようにする
- [x] Dockerコンテナ化

### ページ
- [ ] フレキシブルデザイン
- [ ] ぱんくずリスト
- [ ] トップページ
    - [ ] idoHackとは?
    - [x] お知らせ  
    - [ ] 得点ランキング
- [ ] Markdown記述可能(WriteUPs, 教科書)
    - [ ] 投稿者表示
    - [ ] 作成日時表示
    - [ ] 更新日時表示
    - [ ] 投稿検索機能
- [ ] WriteUPsページ
- [ ] 教科書ページ

### ユーザ情報
- [ ] プロフィールページ作成
    - [ ] クリア済み課題表示機能
    - [ ] 正答数表示
    - [ ] バッジコレクション機能
        ※特定の条件をクリアすると貰えるバッジ(n問クリア, n日連続正解...)
- [ ] ユーザ情報変更ページ作成

### 演習
- [ ] 回答済み課題のバッジ表示(done)
- [ ] 回答済み演習のバッジ表示

## Color-Pallete
### [Grayish Coffee Bean Color Palette](https://www.color-hex.com/color-palette/1036065)

### [Coffee Cafe Color Palette](https://www.color-hex.com/color-palette/90420)

## Components
### Button
``` html
<a href="#" class="btn w-100" style="background-color: #b69096;">ボタン</a>
```

## Commit-Message
# Semantic Commit Messages

See how a minor change to your commit message style can make you a better programmer.

Format: `<type>(<scope>): <subject>`

`<scope>` is optional

## Example

## 機能: ハットの揺れを追加]
```
^--^  ^------------^
|     |
|     +-> 現在形での概要。
|
+-------> タイプ: chore（雑務）、docs（ドキュメント）、feat（新機能）、fix（修正）、refactor（リファクタリング）、style（スタイル）、またはtest（テスト）。
```
他の例:

- `feat`: (ユーザー向けの新機能、ビルドスクリプトの新機能ではない)
- `fix`: (ユーザー向けのバグ修正、ビルドスクリプトの修正ではない)
- `docs`: (ドキュメンテーションの変更)
- `style`: (フォーマット、セミコロンの不足など、本番コードの変更はない)
- `refactor`: (本番コードのリファクタリング、例: 変数の名前変更)
- `test`: (不足しているテストの追加、テストのリファクタリング、本番コードの変更はない)
- `chore`: (gruntタスクの更新など、本番コードの変更はない)