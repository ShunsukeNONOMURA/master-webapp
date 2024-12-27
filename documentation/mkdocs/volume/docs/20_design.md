# 全体設計
| レイヤ             | 設計                          |
| ------------------ | ----------------------------- |
| 全体アーキテクチャ | DDD（オニオンアーキテクチャ） |
| トランザクション   | Unit of Work                  |
| クエリ             | **検討**：CQRS                |

## 全体構成
![](./resource/ddd_flow.dio.svg)

## 基本フロー
```mermaid
sequenceDiagram
  autonumber

  actor c as client
  participant p as Presentation
  participant a as Application
  participant d as Domain
  participant db as DB
  participant os as Outer Service

  c->>+p : Request
  p->>p: depends : check_access_token
  p->>+a : usecase.execute(InputDTO)

loop ユースケース操作
  alt dbに関する操作 (ここではcommitしない)
    a->>+d : uow.repository.method()
    d->>+db : request
    db->>-d : return result
    d->>-a : domain model
  else ドメインに関する操作
    a->>+d : service.method()
    d->>+os : request
    os->>-d : return result
    d->>-a : domain model
  end
end

opt db永続化実行
  a->>+db : uow.commit()
  db->>-a : return result
end

  a->>-p : OutputDTO
  p->>p: middleware : error handling
  p->>p: middleware : construct response 
  p->>p: middleware : logging
  p->>-c: Response
```

## アプリ開発で主に作成するもの
- `app.core.base`のクラスを継承して実装するものが多い。

| パス                          | 機能                         |
| ----------------------------- | ---------------------------- |
| app.ddd.presentation.endpoint | エンドポイント               |
| app.ddd.presentation.schema   | エンドポイントで使うスキーマ |
| app.ddd.application.usecase   | ユースケース                 |
| app.ddd.application.dto       | ユースケースで使うDTO        |
| app.ddd.application.uow       | ユースケースで使うUOW        |
| app.ddd.domain.repository     | リポジトリ（IF）             |
| app.ddd.domain.model          | ドメインモデル               |
| app.ddd.domain.enum           | ドメインの列挙型             |
| app.ddd.domain.error          | ドメインエラー               |
| app.ddd.infrastructure        | 各実装クラス                 |

## 参考
- [PythonでDDDやってみた](https://techtekt.persol-career.co.jp/entry/tech/231220_02)
    - fastapiでオニオンアーキテクチャする例