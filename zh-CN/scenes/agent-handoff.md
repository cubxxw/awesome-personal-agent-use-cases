# Agent 交接 · 换个会话，项目还能接着做

[首页](../../README.zh-CN.md) · [English](../../scenes/agent-handoff.md)

一份能带走的交接记录，写清现在的产物、已核结果和下一步。

## 先看结果

- **当前产物**。draft-v2.md [H1]。
- **已核**。本地预览能打开，三个内部链接可点 [H2]。
- **下一步**。请求审稿，暂无发布回执 [H3]。

## 手头有材料就能试

复制下面整段。里面的材料都是虚构样例。

```text
写一份下一次能用的交接。留下目标、产物位置、已核结果和范围、未完成事项、下一步以及权限，每项带记录编号。下一步要能复核，对外写入需要重新确认。
H1 | 目标：发布资料页 | 当前产物 draft-v2.md
H2 | 已打开本地预览 | 核对 3 个内部链接
H3 | 等审稿 | 无线上发布回执
```

## 已经接了工具

把交接存到产物旁边。换个会话，只拿这个说明和里面指向的文件开工。检查新工具能读哪里，哪些后续动作还需要授权。

## 怎么验收

下一次能找到 draft-v2.md，说清上回实际检查了什么和还有什么待审。中途停下来也能保住上次的结果。

## 做到哪一步

只交给下一步用得上的资料。迁移了提示词和说明后，仍要单独确认新工具的访问权限。

## 这些案例怎么合在一起

一个 Agent 出简报，另一个负责归档。有时也会把整套流程迁到别的工具。都需要一份双方能看见的交接材料，以及说清后续能做什么。

- 把调研问题和来源清单交给写稿步骤。
- 跨会话接一个项目，只拿必要文件和已经核过的结果开工。

## 来源

- **社区做法**。按角色分工，借共享上下文传递能交接的信息。 [用共享上下文让不同 Agent 接手](https://github.com/hesamsheikh/awesome-openclaw-usecases/blob/659895e58e2105c6db8fbef39f446c8a786a480c/usecases/multi-agent-team.md)
- **合集摘要**。同一份简报经邮件交给另一个 Agent，后者负责落盘到仪表盘。 [Muse 386 - 一个 Agent 产出，另一个归档](https://github.com/jaxxchen003/muse-use-cases/blob/7390b4db83fa2687aa8cefb9ec1420ca9a65eb4a/README.md#L2023-L2028) · [原始发布入口](https://www.threads.com/@sonia.elyss/post/DfvpdVUFOSv)
- **合集摘要**。作者分享把已有 Claude 工作流迁到 Muse 再定时跑，摘要没有运行回执。 [Muse 225 - 把现有工作流改到另一个 Agent 跑](https://github.com/jaxxchen003/muse-use-cases/blob/7390b4db83fa2687aa8cefb9ec1420ca9a65eb4a/README.md#L2515-L2520) · [原始发布入口](https://x.com/NewtonJonesIV/status/2098022398721143207)

## 搭建方法

[复用流程](../usecases/repeatable-workflow.md) · [统一收件箱](../usecases/capture-inbox.md) · [平台怎么选](../BUILDER.md)
