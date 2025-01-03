# API設計
## 基本方針
- RESTful(リソース＋操作)でサービスを表現する
    - REpresentational State Transfer
        - [参考：AWS RESTful API とは?](https://aws.amazon.com/jp/what-is/restful-api/)
    - 例：GET `/users`
    - 採用しない方式
        - RPC : Remote Procedure Call
            - POST `/getUsers`
            - [参考 : RPC と REST の違いはなんですか?](https://aws.amazon.com/jp/compare/the-difference-between-rpc-and-rest/)
        - BFF : Backend For Frontend
            - GET `/dashboard/users`
- openapi(FastAPIで自動生成)でドキュメンテーションする

## パス設計
- パスは`spinal-case`で記述する
    - パラメータはjs利用前提を考慮する場合、`camelCase`で記述する。
- シングルトンかマルチプルかは単数形か複数形かで正しく表現する
    - 特定の一人のユーザ
        - `user`
    - 複数のユーザ
        - `users`
- リソースをうまく表現する
    - 例：ユーザ同期リソースのステータスプロパティを表現する
        - × `user/sync/status`
            - ユーザ(`user`)が持つ同期(`sync`)が持つステータス(`status`)とも取れる
            - ユーザ同期 ≠ ユーザではないことが分かりにくい。
        - 〇 `user-sync/status`
            - ユーザ同期`userSync`が持つステータス(`status`)を表現するので誤解を与えにくい。
- バージョンはメジャーバージョンのみ記載

## 操作一覧
| 操作名 | コード | HTTPメソッド | 説明                                                                                                            |
| :----- | :----- | :----------- | :-------------------------------------------------------------------------------------------------------------- |
| Get    | 0      | GET          | 単一のリソース（シングルトン）を取得する操作。                                                                  |
| List   | 1      | GET          | 全リソースを絞り込まずに一覧する操作。ページングは動作想定。複雑なフィルタ等行う際はQueryにすることを検討する。 |
| Create | 2      | POST         | リソースを新規に作成する操作。                                                                                  |
| Patch  | 3      | PATCH        | 既存リソースを部分的に変更する操作。                                                                            |
| Upsert | 4      | PUT          | リソース置換操作。既存リソースがなければ作成する操作。                                                          |
| Delete | 5      | DELETE       | リソースを削除する操作。                                                                                        |
| Query  | 7      | POST         | 特定の問い合わせ処理を要求する。フィルタ条件を隠蔽化したいときなど。検索結果などをレスポンスに含めること。      |

<!-- ## HTTPステータスコード
- 実行結果に対して正しいコードでレスポンスすること
- **TBD**

| コード | メッセージ         | GET            | POST           | PATCH          | PUT            | DELETE         |
| ------ | ------------------ | -------------- | -------------- | -------------- | -------------- | -------------- |
| 200    | OK                 | 取得成功       | 投函成功       | 更新成功       | 置換成功       | 削除成功       |
| 400    | Bad Request        | リクエストミス |                |                |                |                |
| 401    | Unauthorized       | 認証が必要     | 認証が必要     | 認証が必要     | 認証が必要     | 認証が必要     |
| 403    | Forbidden          | 権限が必要     | 権限が必要     | 権限が必要     | 権限が必要     | 権限が必要     |
| 404    | Not Found          | リソースがない |                | リソースがない |                | リソースがない |
| 405    | Method Not Allowed | 不許可メソッド | 不許可メソッド | 不許可メソッド | 不許可メソッド | 不許可メソッド |
| 409    | Conflict           | -              |                |                | 競合している   |                |

-->

## 設計例
| APIアクションコード（RRA） | APIアクション | HTTP Method | URI             | 操作       |
| -------------------------- | ------------- | ----------- | --------------- | ---------- |
| 0000                       | GetHealth     | GET         | /health         | ヘルス取得 |
| 1000                       | GetUser       | GET         | /users/{userId} | ユーザ取得 |
| 1002                       | CreateUser    | POST        | /users          | ユーザ作成 |
| 1003                       | PatchUser     | PATCH       | /users          | ユーザ作成 |
| 1005                       | DeleteUser    | DELETE      | /users/{userId} | ユーザ削除 |
| 1007                       | QueryUser     | POST        | /query/users    | ユーザ検索 |
