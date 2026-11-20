# Contribute / 贡献

## English

1. Start with a situation in the [index](README.md). Check whether the material leads to the same result and decision as an existing scene.
2. Add or update a source and its scenario mapping in [data/catalog.json](data/catalog.json). Use one record for the same post and its mirrors. State what you read and whether the record is an author account, published output, recipe or collection summary.
3. To add a scene, write both language entries with a fictional input, sample result, verification step and decision boundary. Reuse a [building block](BUILDER.md) where it fits.
4. Run `python3 scripts/catalog.py` and `python3 scripts/catalog.py --check`. Review generated changes in both languages. If removing a scene, update its links and remove its generated pages in both languages.

For a reproduced setup, include product and version, observed result and the receipt or output. Show what still requires the user to confirm.

## 中文

1. 从[目录](README.zh-CN.md)里找原来的场景。新材料是不是还在回答同一个问题，最终交付和确认点是否一样？
2. 在 [data/catalog.json](data/catalog.json) 里录入来源和对应场景。原帖和镜像只计一条。说明读到了什么，标清作者自述、公开产物、做法或合集摘要。
3. 新增场景时补齐中英文，给虚构输入、样例结果、验收和确认边界。能复用的步骤链接到[搭建方法](zh-CN/BUILDER.md)。
4. 执行 `python3 scripts/catalog.py` 更新页面，再用 `python3 scripts/catalog.py --check` 检查。两个语言版本一起核对。删除场景时也清理对应页与链接。

提交实测时写清产品与版本、看见的结果和对应回执。让读者知道还有哪一步等本人确认。
