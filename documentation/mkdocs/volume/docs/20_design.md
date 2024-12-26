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
